from pathlib import Path
import subprocess
import tkinter as tk
import mysql.connector
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,filedialog
from datetime import datetime
import csv


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\izzat\OneDrive\Desktop\HADIR.EX\gui\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def fetch_attendance_report():
    # Replace with your database credentials
    db_connection = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="your_database"
    )

    query = "SELECT attendance.studID, CONCAT(examinee.studFName, ' ', examinee.studLName) AS name, attendance.timeAttend, attendance.statusAttend FROM attendance INNER JOIN examinee ON attendance.studID = examinee.studID"
    cursor = db_connection.cursor()
    cursor.execute(query)

    attendance_data = cursor.fetchall()
    db_connection.close()

    return attendance_data

def fetch_attendance_report():
    # Replace with your database credentials
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="examattendance"
    )

    query = "SELECT attendance.studID, CONCAT(examinee.studFName, ' ', examinee.studLName) AS name, attendance.timeAttend, attendance.statusAttend FROM attendance INNER JOIN examinee ON attendance.studID = examinee.studID"
    cursor = db_connection.cursor()
    cursor.execute(query)

    attendance_data = cursor.fetchall()
    db_connection.close()

    return attendance_data

def format_time(time_str):
    if time_str is None:
        return "00:00:00"
    
    if isinstance(time_str, datetime):
        formatted_time = time_str.strftime("%H:%M:%S")
    else:
        time_obj = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
        formatted_time = time_obj.strftime("%H:%M:%S")

    return formatted_time

def save_to_csv(attendance_data):
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if file_path:
        with open(file_path, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Student ID", "Name", "Time", "Status"])
            for row in attendance_data:
                formatted_time = format_time(row[2])
                writer.writerow([row[0], row[1], formatted_time, row[3]])

def display_attendance_report():
    attendance_data = fetch_attendance_report()

    # Create a new Tkinter window
    window = tk.Tk()
    window.title("Attendance Report")
    window.geometry("751x400")
    window.configure(bg = "#FFFFFF")


    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 400,
        width = 751,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        386.0,
        215.0,
        image=image_image_1
    )

    canvas.create_rectangle(
        44.0,
        31.0,
        700.0,
        381.0,
        fill="#FFFFFF",
        outline="")
    
    canvas.create_text(
        165.0,
        45.0,
        anchor="nw",
        text="UiTM EXAM ATTENDANCE SYSTEM",
        fill="#000000",
        font=("AbrilFatface Regular", 20 * -1)
    )

    # Create a canvas to place the attendance data
    #canvas = tk.Canvas(window, width=681, height=358)
    #canvas.pack()

    # Name Column
    canvas.create_rectangle(
        219.0,
        78.0,
        385.0,
        358.0,
        fill="#51475C",
        outline=""
    )

    canvas.create_text(
        275.0,
        84.0,
        anchor="nw",
        text="Name",
        fill="#000000",
        font=("AbrilFatface Regular", 20 * -1)
    )

    # TimeAttend column
    canvas.create_rectangle(
        393.0,
        78.0,
        537.0,
        358.0,
        fill="#51475C",
        outline=""
    )

    canvas.create_text(
        442.0,
        84.0,
        anchor="nw",
        text="Time",
        fill="#000000",
        font=("AbrilFatface Regular", 20 * -1)
    )

    # Student ID column
    canvas.create_rectangle(
        65.0,
        78.0,
        212.0,
        358.0,
        fill="#51475C",
        outline=""
    )

    canvas.create_text(
        86.0,
        84.0,
        anchor="nw",
        text="Student ID",
        fill="#000000",
        font=("AbrilFatface Regular", 20 * -1)
    )

    # Attendance status column
    canvas.create_rectangle(
        543.0,
        78.0,
        681.0,
        358.0,
        fill="#51475C",
        outline=""
    )

    canvas.create_text(
        580.0,
        84.0,
        anchor="nw",
        text="Status",
        fill="#000000",
        font=("AbrilFatface Regular", 20 * -1)
    )

    # Add attendance data to the canvas
    y_position = 110
    for row in attendance_data:
        canvas.create_text(
            90.0 + 3,
            y_position,
            anchor="nw",
            text=row[0],
            fill="#000000",
            font=("Arial", 14)
        )

        canvas.create_text(
            220.0 + 3,
            y_position,
            anchor="nw",
            text=row[1],
            fill="#000000",
            font=("Arial", 14)
        )

        
        formatted_time = format_time(row[2])
        canvas.create_text(
            425.0+3,
            y_position,
            anchor="nw",
            text=formatted_time,
            fill="#000000",
            font=("Arial", 14)
        )

        canvas.create_text(
            580.0+3,
            y_position,
            anchor="nw",
            text=row[3],
            fill="#000000",
            font=("Arial", 14)
        )

        y_position += 20

        #return to homepage button
        def return_to_homepage():
            print("Button clicked")  # Add your code to handle the button click event here

            subprocess.run(["python", r"C:\Users\izzat\OneDrive\Desktop\HADIR.EX\app\homepage.py"])
            window.destroy()

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=return_to_homepage,
        relief="flat"
    )
    button_1.place(
        x=580.0,
        y=33.0,
        width=116.0,
        height=31.0
    )

    #Download the presented table into csv
    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: save_to_csv(attendance_data),
        relief="flat"
    )
    button_2.place(
        x=533.0,
        y=35.0,
        width=33.0,
        height=37.0
    )
    window.resizable(False, False)

    # Save the attendance report as an image
    canvas.postscript(file="attendance_report.ps", colormode="color")

    window.mainloop()

if __name__ == "__main__":
    display_attendance_report()



