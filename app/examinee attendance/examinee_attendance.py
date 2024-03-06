from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import mysql.connector 


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\izzat\OneDrive\Desktop\HADIR.EX\gui\examinee attendance\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


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
    58.0,
    37.0,
    anchor="nw",
    text="UiTM EXAM ATTENDANCE SYSTEM",
    fill="#000000",
    font=("AbrilFatface Regular", 20 * -1)
)

canvas.create_cameraplace(
    64.0,
    68.0,
    408.0,
    353.0,
    fill="#1B1919",
    outline="")

canvas.create_name(
    428.0,
    101.0,
    686.0,
    139.0,
    fill="#51475C",
    outline="")

canvas.create_subCode(
    428.0,
    169.0,
    686.0,
    207.0,
    fill="#51475C",
    outline="")

canvas.create_Session(
    428.0,
    232.0,
    686.0,
    270.0,
    fill="#51475C",
    outline="")

canvas.create_Venue(
    428.0,
    295.0,
    686.0,
    333.0,
    fill="#51475C",
    outline="")

canvas.create_text(
    429.0,
    271.0,
    anchor="nw",
    text="Venue",
    fill="#000000",
    font=("AbrilFatface Regular", 20 * -1)
)

canvas.create_text(
    431.0,
    76.0,
    anchor="nw",
    text="Name",
    fill="#000000",
    font=("AbrilFatface Regular", 20 * -1)
)

canvas.create_text(
    431.0,
    206.0,
    anchor="nw",
    text="Session",
    fill="#000000",
    font=("AbrilFatface Regular", 20 * -1)
)

canvas.create_text(
    431.0,
    142.0,
    anchor="nw",
    text="Subject Code",
    fill="#000000",
    font=("AbrilFatface Regular", 20 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
home= Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
home.place(
    x=579.0,
    y=40.0,
    width=116.0,
    height=31.0
)
window.resizable(False, False)
window.mainloop()
