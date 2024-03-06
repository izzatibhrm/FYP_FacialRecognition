from pathlib import Path
import tkinter as tk
from tkinter import Canvas, Entry, Text, Button, PhotoImage, messagebox, Toplevel, Label
import mysql.connector
#from homepage import homepage
import subprocess

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\izzat\OneDrive\Desktop\HADIR_EXAM\gui\LogIn\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def signup_page():
    print("Button clicked")  # Add your code to handle the button click event here

    subprocess.run(["python", r"C:\Users\izzat\OneDrive\Desktop\HADIR.EX\app\signup.py"])
    login_window.destroy()

def homepage():
    from homepage import homepage as create_homepage
    login_window.withdraw()
    create_homepage()

def login_page():
    global login_window 
    login_window = tk.Tk()
    login_window.geometry("751x400")
    login_window.configure(bg = "#FFFFFF")

    canvas = Canvas(
        login_window,
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
        48.0,
        36.0,
        704.0,
        364.0,
        fill="#D9D9D9",
        outline="")

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        211.0,
        234.0,
        image=entry_image_1
    )
    entry_username = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        show='*'
    )
    entry_username.place(
        x=99.0,
        y=214.0,
        width=224.0,
        height=38.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        211.0,
        155.0,
        image=entry_image_2
    )
    entry_password = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        
    )
    entry_password.place(
        x=99.0,
        y=135.0,
        width=224.0,
        height=38.0
    )

    canvas.create_text(
        94.0,
        113.0,
        anchor="nw",
        text="Username",
        fill="#000000",
        font=("AbrilFatface Regular", 16 * -1)
    )

    canvas.create_text(
        96.0,
        192.0,
        anchor="nw",
        text="Password",
        fill="#000000",
        font=("AbrilFatface Regular", 16 * -1)
    )

    def login():
        username = entry_username.get()
        password = entry_password.get()

        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='examattendance'
            )
            cursor = connection.cursor()

            # Write your login query here
            query = "SELECT * FROM invigilator WHERE InvigUsername=%s AND InvigPassword=%s"
            cursor.execute(query, (username, password))

            user = cursor.fetchone()
            if user:
                # Successful login, navigate to the homepage
                login_window.destroy()
                homepage()
            else:
                # Failed login, show an error message
                messagebox.showinfo(title="Error", message="Invalid username or password.")

        except mysql.connector.Error as err:
            print("Error: ", err)
            messagebox.showinfo(message="Database connection error.")


    #LogIN
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=login,
        relief="flat"
    )
    button_1.place(
        x=140.0,
        y=294.0,
        width=148.0,
        height=34.0
    )

    #Sign up
    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=signup_page,
        relief="flat"
    )
    button_2.place(
        x=154.0,
        y=328.0,
        width=119.0,
        height=19.0
    )

    canvas.create_text(
        127.0,
        51.0,
        anchor="nw",
        text="User Log In",
        fill="#000000",
        font=("AbrilFatface Regular", 32 * -1)
    )

    canvas.create_text(
        382.0,
        293.0,
        anchor="nw",
        text="UNIVERSITI TEKNOLOGI MARA\nEXAM ATTENDANCE SYSTEM",
        fill="#000000",
        font=("AbrilFatface Regular", 20 * -1)
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        536.0,
        170.0,
        image=image_image_2
    )

    
    login_window.resizable(False, False)
    login_window.mainloop()

login_page()