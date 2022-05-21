from functools import partial
import tkinter as tk
from tkinter import filedialog, Text
import os


buttons_symbols = ['%', 'CE', 'C', 'BSPC', '1/x', 'x^2', 'sqrt(x)', '/', '7', '8', '9', 'x', '4', '5', '6', '--', '1', '2', '3', '+', '-', '0', '.', '=']
numpad_buttons_symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '.']


def on_numpad_press(text):
    # print("__FUNCTION__on_numpad_press", text)
    current_text = display_label['text']
    if text != '-':
        display_label.config(text=current_text+text)
    elif text == '-' and current_text != "":
        if current_text[0] == '-':
            display_label.config(text=current_text[1:])
        else:
            display_label.config(text='-'+current_text)
    elif text == '-' and current_text == "":
        display_label.config(text="")
    else:
        display_label.config(text="error")


def on_button_press(text):
    # print("__FUNCTION__on_button_press", text)
    current_text = display_label['text']
    if current_text != "":
        if text == 'C':
            display_label.config(text="")


# Holds the whole structure. So when you want to attach components, attach it to the root
root = tk.Tk()
# wrapper_canvas = tk.Canvas(root, height=1000, width=1000)
# wrapper_canvas.pack(fill="both", expand=True)


numpad_canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
numpad_canvas.pack(fill="both", expand=True)

display = tk.Frame(root)

display_label = tk.Label(root, height=200, width=700, text="", background="white")
display_label.pack(fill="both", expand=True)
display_label.place(relx=0, rely=0, relwidth=0.5, relheight=0.24)

# frame = tk.Frame(canvas, bg="white")
# frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

buttons = []
next_row = False
current_row = 2
current_col = 0
for index, symbol in enumerate(buttons_symbols):
    if symbol in numpad_buttons_symbols:
        button = tk.Button(numpad_canvas, text=symbol, command=partial(on_numpad_press, symbol))
        if index % 4 == 0 and index != 0:
            current_row += 1
            current_col = 0
        button.place(relx=(current_col)*0.125, rely=0.125*current_row, relwidth=0.125, relheight=0.125)
        buttons.append(button)
        current_col += 1
    else:
        button = tk.Button(numpad_canvas, text=symbol, command=partial(on_button_press, symbol))
        if index % 4 == 0 and index != 0:
            current_row += 1
            current_col = 0
        button.place(relx=(current_col)*0.125, rely=0.125*current_row, relwidth=0.125, relheight=0.125)
        buttons.append(button)
        current_col += 1

# print(numpad_buttons)

# openFile = tk.Button(root, text="")

# root.mainloop()


# from tkinter import *
from tkinter import ttk
# root = Tk()
frm = ttk.Frame(root, padding=10, height=700, width=700)
# canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
# print(canvas.configure().keys())
# print(frm.configure().keys())
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()