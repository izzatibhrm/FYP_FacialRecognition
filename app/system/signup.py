from pathlib import Path
import tkinter as tk
from tkinter import Canvas, Entry, Text, Button, PhotoImage, messagebox
import mysql.connector
import subprocess

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\izzat\OneDrive\Desktop\HADIR_EXAM\gui\Register\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def login_page():
    subprocess.run(["python",r"C:\Users\izzat\OneDrive\Desktop\HADIR.EX\app\login_page.py"])
    signup_window_tk.destroy()

def signup_page():
    global signup_window_tk

    signup_window_tk = tk.Tk()
    signup_window_tk.geometry("751x400")
    signup_window_tk.configure(bg = "#FFFFFF")
 
    canvas = Canvas(
        signup_window_tk,
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

    canvas.create_text(
        74.0,
        294.0,
        anchor="nw",
        text="UNIVERSITI TEKNOLOGI MARA\nEXAM ATTENDANCE SYSTEM",
        fill="#000000",
        font=("AbrilFatface Regular", 20 * -1)
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        202.0,
        185.0,
        image=image_image_2
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        554.5,
        260.5,
        image=entry_image_1
    )
    entry_Password = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
        
    )
    entry_Password.place(
        x=439.0,
        y=244.0,
        width=231.0,
        height=31.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        556.0,
        205.5,
        image=entry_image_2
    )
    entry_Username = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_Username.place(
        x=440.0,
        y=190.0,
        width=232.0,
        height=29.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        555.0,
        96.5,
        image=entry_image_3
    )
    entry_UserID = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_UserID.place(
        x=439.0,
        y=81.0,
        width=232.0,
        height=29.0
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        492.0,
        154.0,
        image=entry_image_4
    )
    entry_FirstName = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_FirstName.place(
        x=440.0,
        y=139.0,
        width=104.0,
        height=28.0
    )

    entry_image_5 = PhotoImage(
        file=relative_to_assets("entry_5.png"))
    entry_bg_5 = canvas.create_image(
        620.0,
        154.0,
        image=entry_image_5
    )
    entry_LastName = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_LastName.place(
        x=568.0,
        y=139.0,
        width=104.0,
        height=28.0
    )

    canvas.create_text(
        433.0,
        169.0,
        anchor="nw",
        text="Username",
        fill="#000000",
        font=("AbrilFatface Regular", 16 * -1)
    )

    def signup():
            InvigID = entry_UserID.get()
            InvigFName = entry_FirstName.get()
            InvigLName = entry_LastName.get()
            InvigUsername = entry_Username.get()
            InvigPassword = entry_Password.get()

            connection = mysql.connector.connect(host ='localhost', user = 'root', password ='', database = 'examattendance')
            c = connection.cursor()

            insert_query = "INSERT INTO `invigilator`(`InvigID`, `InvigFName`, `InvigLName`, `InvigUsername`, `InvigPassword`) VALUES (%s, %s, %s, %s, %s)"
            vals = (InvigID,InvigFName,InvigLName,InvigUsername,InvigPassword)
            c.execute(insert_query,vals)
            connection.commit()
            messagebox.showinfo(title='Register status', message='You have registered')
    
    canvas.create_text(
        425.0,
        117.0,
        anchor="nw",
        text="First name",
        fill="#000000",
        font=("AbrilFatface Regular", 16 * -1)
    )

    canvas.create_text(
        414.0,
        60.0,
        anchor="nw",
        text="User ID",
        fill="#000000",
        font=("AbrilFatface Regular", 16 * -1)
    )

    canvas.create_text(
        562.0,
        117.0,
        anchor="nw",
        text="Last Name",
        fill="#000000",
        font=("AbrilFatface Regular", 16 * -1)
    )

    canvas.create_text(
        434.0,
        221.0,
        anchor="nw",
        text="Password",
        fill="#000000",
        font=("AbrilFatface Regular", 16 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command= signup,
        relief="flat"
    )
    button_1.place(
        x=481.0,
        y=287.0,
        width=148.0,
        height=34.0
    )

    button_image_ExistUser = PhotoImage(
        file=relative_to_assets("ExistUser.png"))
    button_ExistUser = Button(
        image=button_image_ExistUser,
        borderwidth=0,
        highlightthickness=0,
        command=login_page,
        relief="flat"
    )
    button_ExistUser.place(
        x=487.0,
        y=322.0,
        width=135.0,
        height=19.0
    )

    canvas.create_text(
        105.0,
        42.0,
        anchor="nw",
        text="User Sign Up",
        fill="#000000",
        font=("AbrilFatface Regular", 24 * -1)
    )
    signup_window_tk.resizable(False, False)
    signup_window_tk.mainloop()


signup_page()