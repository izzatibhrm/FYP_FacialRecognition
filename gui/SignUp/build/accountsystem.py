from pathlib import Path
from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
import mysql.connector

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\izzat\OneDrive\Desktop\HADIR_EXAM\gui\SignUp\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


#Window Size and Placement

window = Tk()
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
height = 400
width = 751
x = (window.winfo_screenwidth()//2) -(width//2)
y = (window.winfo_screenheight()//4) -(height//4)
window.geometry('{}x{}+{}+{}'.format(width,height,x,y))

window.title('ACCOUNT SYSTEM')

# Navigate through windows
sign_in = Frame(window)
sign_up = Frame(window)

for frame in (sign_up, sign_in):
    frame.grid(row=0, column=0, sticky='snew')

def show_frame(frame):
    frame.tkraise()

show_frame(sign_up)

#Sign Page 
sign_up.configure(bg="#525561")

connection = mysql.connector.connect(host ='localhost', user = 'root', password ='', database = 'examattendance')
c = connection.cursor()

canvas1 = Canvas(
    sign_up,
    bg = "#FFFFFF",
    height = 400,
    width = 751,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas1.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas1.create_image(
    386.0,
    215.0,
    image=image_image_1
)

canvas1.create_rectangle(
    48.0,
    36.0,
    704.0,
    364.0,
    fill="#D9D9D9",
    outline="")

canvas1.create_text(
    74.0,
    294.0,
    anchor="nw",
    text="UNIVERSITI TEKNOLOGI MARA\nEXAM ATTENDANCE SYSTEM",
    fill="#000000",
    font=("AbrilFatface Regular", 20 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas1.create_image(
    202.0,
    185.0,
    image=image_image_2
)

entry_Password1 = PhotoImage(
    file=relative_to_assets("Password.png"))
entry_bg_1 = canvas1.create_image(
    554.5,
    260.5,
    image=entry_Password1
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

entry_Username1 = PhotoImage(
    file=relative_to_assets("Username.png"))
entry_bg_2 = canvas1.create_image(
    556.0,
    205.5,
    image=entry_Username1
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

entry_UserID1 = PhotoImage(
    file=relative_to_assets("UserID.png"))
entry_bg_3 = canvas1.create_image(
    555.0,
    96.5,
    image=entry_UserID1
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

def insertData():
    InvigID = entry_UserID.get()
    InvigFName = entry_FirstName.get()
    InvigLName = entry_LastName.get()
    InvigUsername = entry_Username.get()
    InvigPassword = entry_Password.get()

    insert_query = "INSERT INTO `invigilator`(`InvigID`, `InvigFName`, `InvigLName`, `InvigUsername`, `InvigPassword`) VALUES (%s, %s, %s, %s, %s)"
    vals = (InvigID,InvigFName,InvigLName,InvigUsername,InvigPassword)
    c.execute(insert_query,vals)
    connection.commit()
    messagebox.showinfo(title='Register status', message='You have registered')


entry_FirstName1 = PhotoImage(
    file=relative_to_assets("FirstName.png"))
entry_bg_4 = canvas1.create_image(
    492.0,
    154.0,
    image=entry_FirstName1
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

entry_LastName1 = PhotoImage(
    file=relative_to_assets("LastName.png"))
entry_bg_5 = canvas1.create_image(
    620.0,
    154.0,
    image=entry_LastName1
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

canvas1.create_text(
    433.0,
    169.0,
    anchor="nw",
    text="Username",
    fill="#000000",
    font=("AbrilFatface Regular", 16 * -1)
)

canvas1.create_text(
    434.0,
    117.0,
    anchor="nw",
    text="First name",
    fill="#000000",
    font=("AbrilFatface Regular", 16 * -1)
)

canvas1.create_text(
    434.0,
    60.0,
    anchor="nw",
    text="User ID",
    fill="#000000",
    font=("AbrilFatface Regular", 16 * -1)
)

canvas1.create_text(
    562.0,
    117.0,
    anchor="nw",
    text="Last Name",
    fill="#000000",
    font=("AbrilFatface Regular", 16 * -1)
)

canvas1.create_text(
    434.0,
    221.0,
    anchor="nw",
    text="Password",
    fill="#000000",
    font=("AbrilFatface Regular", 16 * -1)
)

button_image_SignUp = PhotoImage(
    file=relative_to_assets("SignUp.png"))
button_SignUp = Button(
    image= button_image_SignUp,
    borderwidth=0,
    highlightthickness=0,
    command=insertData,
    relief="flat"
)
button_SignUp.place(
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
    command=lambda: show_frame(sign_in),
    relief="flat"
)
button_ExistUser.place(
    x=487.0,
    y=322.0,
    width=135.0,
    height=19.0
)

canvas1.create_text(
    130.0,
    42.0,
    anchor="nw",
    text="User Sign Up",
    fill="#000000",
    font=("AbrilFatface Regular", 24 * -1)
)
window.resizable(False,False)


#Login Page

sign_in.configure(bg="#525561")

canvas = Canvas(
    sign_in,
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
    file=relative_to_assets("LUserName.png"))
entry_bg_1 = canvas.create_image(
    211.0,
    234.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=99.0,
    y=214.0,
    width=224.0,
    height=38.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("LPassword.png"))
entry_bg_2 = canvas.create_image(
    211.0,
    155.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
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

button_image_1 = PhotoImage(
    file=relative_to_assets("LogIn.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=140.0,
    y=294.0,
    width=148.0,
    height=34.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("NewUser.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_frame(sign_up),
    relief="flat"
)
button_2.place(
    x=154.0,
    y=328.0,
    width=119.0,
    height=19.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=229.0,
    y=258.0,
    width=99.0,
    height=18.0
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

window.resizable(False,False)
window.mainloop()