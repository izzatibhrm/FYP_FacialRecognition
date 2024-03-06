import tkinter as tk
import cv2
import numpy as np
import mysql.connector
from keras_facenet import FaceNet
from PIL import Image, ImageTk
from numpy import asarray, expand_dims
from scipy.spatial.distance import cosine
from mtcnn.mtcnn import MTCNN
from pathlib import Path
import subprocess
import json
import datetime

# Database configuration
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = ''
DB_NAME = 'examattendance'
ENCODINGS_TABLE = 'encodings'

# FaceNet and MTCNN setup
mtcnn_detector = MTCNN()
model = FaceNet()

# Connect to MySQL database
db_connection = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASS,
    database=DB_NAME
)

# Function to convert JSON-encoded face encodings to float arrays
def parse_face_encoding(face_encoding_json):
    try:
        face_encoding = json.loads(face_encoding_json)
        return np.array(face_encoding, dtype=float)
    except (ValueError, TypeError):
        return None

# Retrieve embeddings and identities from the database
cursor = db_connection.cursor()
cursor.execute(f"SELECT id, encoding FROM {ENCODINGS_TABLE}")
data = cursor.fetchall()
cursor.close()
db_connection.close()

# Convert the data into a dictionary with ids as keys and embeddings as values
embeddings_data = {identity_id: parse_face_encoding(face_encoding_json) for identity_id, face_encoding_json in data}


# GUI setup
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("C:/Users/izzat/OneDrive/Desktop/HADIR.EX/gui/examinee attendance/assets/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def draw_label(frame, face_coords, recognized_id, name_value, sub_code_value, session_value, venue_value):
    x, y, w, h = face_coords

    # Draw a bounding box around the detected face
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the recognized ID above the bounding box
    label = str(recognized_id)
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_thickness = 2
    text_size = cv2.getTextSize(label, font, font_scale, font_thickness)[0]
    text_x = x + (w - text_size[0]) // 2
    text_y = y - 10 if y - 10 > 10 else y + h + 30
    cv2.putText(frame, label, (text_x, text_y), font, font_scale, (0, 255, 0), font_thickness, cv2.LINE_AA)

    # Display the recognized name, subject code, session, and venue values on the GUI
    canvas.create_text(428.0, 101.0, anchor="nw", text=name_value, fill="#000000", font=("AbrilFatface Regular", 20 * -1))
    canvas.create_text(428.0, 169.0, anchor="nw", text=sub_code_value, fill="#000000", font=("AbrilFatface Regular", 20 * -1))
    canvas.create_text(428.0, 232.0, anchor="nw", text=session_value, fill="#000000", font=("AbrilFatface Regular", 20 * -1))
    canvas.create_text(428.0, 295.0, anchor="nw", text=venue_value, fill="#000000", font=("AbrilFatface Regular", 20 * -1))

# Camera setup and face detection loop
cap = cv2.VideoCapture(0)

# Function to calculate cosine similarity
def cosine_similarity(embedding1, embedding2):
    return 1 - cosine(embedding1, embedding2)

# Function to find the closest match for a given test encoding
def find_closest_match(test_encoding, database_data):
    best_match = None
    best_similarity = -1
    for identity, db_encoding in database_data.items():
        if db_encoding is not None:
            # Ensure that both test_encoding and db_encoding are 1-dimensional arrays
            test_encoding_flat = np.ravel(test_encoding)
            db_encoding_flat = np.ravel(db_encoding)

        similarity = cosine_similarity(test_encoding_flat, db_encoding_flat)
        if similarity > best_similarity:
            best_similarity = similarity
            best_match = identity
    return best_match

def mark_attendance(recognized_id):
    # Get the current timestamp
    current_time = datetime.datetime.now()

    # Connect to the database
    db_connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME
    )
    cursor = db_connection.cursor()

    if recognized_id is not None:
        # Update the attendance record for recognized student
        update_query = "UPDATE attendance SET timeattend = %s, statusattend = 'present' WHERE studID = %s"
        cursor.execute(update_query, (current_time, recognized_id))
        print("attendance updated")
    
    db_connection.commit()
    cursor.close()
    db_connection.close()

def detect_faces():
    _, gbr1 = cap.read()
    face_coords = mtcnn_detector.detect_faces(gbr1)

    for face_coord in face_coords:
        x1, y1, width, height = face_coord['box']
        x2, y2 = x1 + width, y1 + height

        # Preprocess the detected face for FaceNet (resize and normalize)
        detected_face = gbr1[y1:y2, x1:x2]  # Extract the detected face region
        detected_face = cv2.cvtColor(detected_face, cv2.COLOR_BGR2RGB)
        detected_face = Image.fromarray(detected_face)
        detected_face = detected_face.resize((160, 160))
        detected_face = asarray(detected_face)
        detected_face = detected_face / 255.0  # Normalize pixel values to [0, 1]
        detected_face = expand_dims(detected_face, axis=0)
        
        # Get the face embedding using FaceNet
        signature = model.embeddings(detected_face)

        # Compare the embedding with all the embeddings from the database
        recognized_id = find_closest_match(signature, embeddings_data)

        # Retrieve face details from the database 
        db_connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASS,
            database=DB_NAME
        )
        cursor = db_connection.cursor()
        query = f"SELECT CONCAT(examinee.studFName,' ',examinee.studLName) AS name, examination.Subject, examination.session, examination.venue FROM examination INNER JOIN examinee ON examination.studID=examinee.studID WHERE id=%s"
        cursor.execute(query,(recognized_id,))
        result = cursor.fetchone()
        cursor.close()
        db_connection.close()

        if result:
            name_value, sub_code_value, session_value, venue_value = result
            draw_label(gbr1, face_coord['box'], recognized_id, name_value, sub_code_value, session_value, venue_value)

            print(recognized_id)
            
            # Mark attendance for recognized students and insert attendance details into the database
            mark_attendance(recognized_id)


    # Resize the frame to 344 x 285 for displaying on the canvas
    resized_frame = cv2.resize(gbr1, (344, 285))
    cv2image = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGBA)
    img = ImageTk.PhotoImage(image=Image.fromarray(cv2image))
    canvas.img = img
    canvas.create_image(64.0, 68.0, anchor=tk.NW, image=img)

    # Call the function recursively after a delay (you may adjust the delay as per your requirement)
    window.after(100, detect_faces)

# Tkinter GUI setup
window = tk.Tk()
window.geometry("751x400")
window.configure(bg="#FFFFFF")

canvas = tk.Canvas(
    window,
    bg="#FFFFFF",
    height=400,
    width=751,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

image_image_1 = tk.PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(386.0, 215.0, image=image_image_1)

canvas.create_rectangle(48.0, 31.0, 704.0, 359.0, fill="#FFFFFF", outline="")

canvas.create_text(58.0, 37.0, anchor="nw", text="UiTM EXAM ATTENDANCE SYSTEM", fill="#000000", font=("AbrilFatface Regular", 20 * -1))

# Placeholders for the name, subject code, session, and venue values upon detection
canvas.create_text(429.0, 76.0, anchor="nw", text="Name", fill="#000000", font=("AbrilFatface Regular", 20 * -1))
canvas.create_text(431.0, 142.0, anchor="nw", text="Subject Code", fill="#000000", font=("AbrilFatface Regular", 20 * -1))
canvas.create_text(431.0, 206.0, anchor="nw", text="Session", fill="#000000", font=("AbrilFatface Regular", 20 * -1))
canvas.create_text(429.0, 271.0, anchor="nw", text="Venue", fill="#000000", font=("AbrilFatface Regular", 20 * -1))

# GUI code for the "return to homepage" button
button_image_1 = tk.PhotoImage(file=relative_to_assets("button_1.png"))

def return_to_homepage():
    print("Button clicked")  # Add your code to handle the button click event here

    subprocess.run(["python", r"C:\Users\izzat\OneDrive\Desktop\HADIR.EX\app\homepage.py"])
    window.destroy()
    
home = tk.Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=return_to_homepage,
    relief="flat"
)
home.place(x=579.0, y=40.0, width=116.0, height=31.0)

window.resizable(False, False)

# Start the facial detection process
detect_faces()

window.mainloop()
cap.release()
cv2.destroyAllWindows()
