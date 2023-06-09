
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\kyler\Desktop\New folder (2)\test\assets\frame4")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class frame1:
    
    window = Tk()

    window.geometry("1440x1024")
    window.configure(bg = "#394867")
    def switch_to_frame2(self):
            self.frame.pack_forget()
            frame2 = frame2(self.parent)

    canvas = Canvas(
            window,
            bg = "#394867",
            height = 1024,
            width = 1440,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
            720.0,
            512.0,
            image=image_image_1
        )

    image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
            721.0,
            514.0,
            image=image_image_2
        )

    image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
            721.0,
            618.0,
            image=image_image_3
        )

    button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
    button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command= switch_to_frame2,
            relief="flat"
        )
    button_1.place(
            x=462.0,
            y=639.0,
            width=495.0,
        height=147.0
    )


 
