from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox, Toplevel, Label
import mysql.connector

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\izzat\OneDrive\Desktop\HADIR_EXAM\gui\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def login_user():
    if entry_LUsername.get()=='' or entry_LPassword.get()=='':
      messagebox.showerror("Error","All Fields are Required")  
    else:
        try:
            connection = mysql.connector.connect(host ='localhost', user = 'root', password ='', database = 'examattendance')
            c = connection.cursor()
        except:
            messagebox.showerror("Error","Connection is not established try again")
            return
        query = 'use examattendance'
        c.execute(query)
        query='select * from invigilator where InvigUsername=%s and InvigPassword=%s'
        c.execute(query,(entry_LUsername.get(),entry_LPassword.get()))
        row=c.fetchone()
        if row==None:
            messagebox.showerror("Error","Invalid username or password")
        else:
            messagebox.showinfo("Welcome", "Login is successful")

window = Tk()

window.geometry("751x400")
window.configure(bg = "#FFFFFF")

connection = mysql.connector.connect(host ='localhost', user = 'root', password ='', database = 'examattendance')
c = connection.cursor()

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
canvas.create_rectangle(
    0.0,
    2.0,
    758.0,
    412.0,
    fill="#FFFFFF",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    384.0,
    207.0,
    image=image_image_1
)

canvas.create_text(
    97.0,
    371.0,
    anchor="nw",
    text="UNIVERSITI TEKNOLOGI MARA EXAM ATTENDANCE SYSTEM",
    fill="#000000",
    font=("yu gothic ui", 20 * -1)
)

canvas.create_rectangle(
    55.0,
    37.0,
    702.0,
    364.0,
    fill="#D9D9D9",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    192.0,
    236.0,
    image=entry_image_1
)
entry_LUsername = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_LUsername.place(
    x=80.0,
    y=216.0,
    width=224.0,
    height=38.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    192.0,
    157.0,
    image=entry_image_2
)
entry_LPassword = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_LPassword.place(
    x=80.0,
    y=137.0,
    width=224.0,
    height=38.0
)

canvas.create_text(
    75.0,
    115.0,
    anchor="nw",
    text="Username",
    fill="#000000",
    font=("yu gothic ui", 16 * -1)
)

canvas.create_text(
    77.0,
    194.0,
    anchor="nw",
    text="Password",
    fill="#000000",
    font=("yu gothic ui", 16 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_LogIn = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=login_user,
    relief="flat"
)
button_LogIn.place(
    x=121.0,
    y=296.0,
    width=148.0,
    height=34.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_ForgotPassword = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: forgot_password(),
    relief="flat"
)
button_ForgotPassword.place(
    x=210.0,
    y=260.0,
    width=99.0,
    height=18.0
)

#got one error on line 186
def forgot_password():
    def change_password():
        if User_entry.get()== "" or newpassword_entry.get()=="":
            messagebox.showerror("Error","All fields are required", parent=window)
        
        else:
            connection = mysql.connector.connect(host ='localhost', user = 'root', password ='', database = 'examattendance')
            mycursor = connection.cursor()
            query = 'select * from invigilator where InvigUsername=%s'
            val = User_entry.get()
            mycursor.execute(query,(val,))
            row = mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Incorrect Username", parent=window)
            else:
                query='update invigilator set InvigPassword=(%s) where InvigUserName=(%s)'
                val = User_entry.get()
                val1= newpassword_entry.get()
                mycursor.execute(query,(val1,val,))
                connection.commit()
                connection.close()
                messagebox.showinfo("Success","Password is reset, please login with new password", parent=window)
                window.destroy()
    
    win = Toplevel()
    window_width = 350
    window_height = 350
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    position_top = int(screen_height / 4 - window_height / 4)
    position_right = int(screen_width / 2 - window_width / 2)
    win.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

    win.title('Forgot Password')
    win.configure(background='#D9D9D9')
    win.resizable(False, False)

    
    User_entry = Entry(win, bg="#9E9999", font=("yu gothic ui semibold", 12), highlightthickness=1, bd=0)
    User_entry.place(x=40, y=80, width=256, height=50)

    Username_label3 = Label(win, text='Username', fg="#FFFFFF", bg='#D9D9D9',
                         font=("yu gothic ui", 13, 'bold'))
    Username_label3.place(x=40, y=50)

    
    newpassword_entry = Entry(win, bg="#9E9999", font=("yu gothic ui semibold", 12), show='•', highlightthickness=1,
                               bd=0)
    newpassword_entry.place(x=40, y=180, width=256, height=50)
    newpassword_entry.config(highlightbackground="#9E9999", highlightcolor="#206DB4")
    newpassword_label = Label(win, text='New Password', fg="#FFFFFF", bg='#D9D9D9',
                               font=("yu gothic ui", 13, 'bold'))
    newpassword_label.place(x=40, y=150)


    update_pass = Button(win, fg='#f8f8f8', text='Update Password', bg='#1D90F5', font=("yu gothic ui", 12, "bold"),
                         cursor='hand2', relief="flat", bd=0, highlightthickness=0, activebackground="#1D90F5", command=change_password)
    update_pass.place(x=40, y=260, width=256, height=45)


canvas.create_text(
    133.0,
    51.0,
    anchor="nw",
    text="User Log In",
    fill="#000000",
    font=("yu gothic ui", 24 * -1)
)

#SignUp
entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    541.5,
    283.5,
    image=entry_image_3
)
entry_Password = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_Password.place(
    x=425.0,
    y=269.0,
    width=233.0,
    height=27.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    541.5,
    230.5,
    image=entry_image_4
)
entry_Username = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_Username.place(
    x=425.0,
    y=216.0,
    width=233.0,
    height=27.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    541.5,
    127.5,
    image=entry_image_5
)
entry_UserID = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_UserID.place(
    x=425.0,
    y=113.0,
    width=233.0,
    height=27.0
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

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    478.0,
    178.0,
    image=entry_image_6
)
entry_FirstName = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_FirstName.place(
    x=425.0,
    y=164.0,
    width=106.0,
    height=26.0
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    600.0,
    178.0,
    image=entry_image_7
)
entry_LastName = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_LastName.place(
    x=547.0,
    y=164.0,
    width=106.0,
    height=26.0
)

canvas.create_text(
    421.0,
    192.0,
    anchor="nw",
    text="Username",
    fill="#000000",
    font=("yu gothic ui", 16 * -1)
)

canvas.create_text(
    421.0,
    141.0,
    anchor="nw",
    text="First name",
    fill="#000000",
    font=("yu gothic ui", 16 * -1)
)

canvas.create_text(
    421.0,
    92.0,
    anchor="nw",
    text="User ID",
    fill="#000000",
    font=("yu gothic ui", 16 * -1)
)

canvas.create_text(
    545.0,
    141.0,
    anchor="nw",
    text="Last Name",
    fill="#000000",
    font=("yu gothic ui", 16 * -1)
)

canvas.create_text(
    421.0,
    245.0,
    anchor="nw",
    text="Password",
    fill="#000000",
    font=("yu gothic ui", 16 * -1)
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=insertData,
    relief="flat"
)
button_3.place(
    x=462.0,
    y=315.0,
    width=148.0,
    height=34.0
)

canvas.create_text(
    466.0,
    51.0,
    anchor="nw",
    text="User Sign Up",
    fill="#000000",
    font=("yu gothic ui", 24 * -1)
)
window.resizable(False, False)
window.mainloop()
