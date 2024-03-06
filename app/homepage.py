from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\izzat\OneDrive\Desktop\HADIR_EXAM\gui\HomePage\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_exam_attendance():
    subprocess.run(["python",r"C:\Users\izzat\OneDrive\Desktop\HADIR.EX\app\examattendance.py"])

    window.destroy()

def open_login():
    subprocess.run(["python",r"C:\Users\izzat\OneDrive\Desktop\HADIR.EX\app\login_page.py"])

    window.destroy()
def open_report():
    subprocess.run(["python",r"C:\Users\izzat\OneDrive\Desktop\HADIR.EX\gui\build\gui.py"])

    window.destroy()


window = Tk()

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
canvas.create_rectangle(
    571.0,
    41.0,
    691.0,
    78.0,
    fill="#FFFFFF",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    386.0,
    215.0,
    image=image_image_1
)

canvas.create_rectangle(
    48.0,
    31.0,
    704.0,
    359.0,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    213.0,
    45.0,
    anchor="nw",
    text="UNIVERSITI TEKNOLOGI MARA\nEXAM ATTENDANCE SYSTEM",
    fill="#000000",
    font=("AbrilFatface Regular", 20 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    371.0,
    207.0,
    image=image_image_2
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=open_exam_attendance,
    relief="flat"
)
button_2.place(
    x=487.0,
    y=120.0,
    width=166.0,
    height=194.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=open_report,
    relief="flat"
)
button_3.place(
    x=85.0,
    y=126.0,
    width=172.0,
    height=174.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=open_login,
    relief="flat"
)
button_4.place(
    x=575.0,
    y=41.0,
    width=116.0,
    height=31.0
)
window.resizable(False, False)
window.mainloop()
