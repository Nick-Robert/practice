from functools import partial
from logging import exception
import tkinter as tk
from tkinter import filedialog, Text
import os
from math import sqrt

buttons_symbols = ['%', 'CE', 'C', 'BSPC', '1/x', 'x^2', 'sqrt(x)', '/', '7', '8', '9', 'x', '4', '5', '6', '--', '1', '2', '3', '+', '-', '0', '.', '=']
numpad_buttons_symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '.']
history = []


previous_operation = ""
def save_operation(text):
    print("__FUNCTION__save_operation(val)")
    previous_operation = text


def print_last_display():
    print("__FUNCTION__print_last_display()")
    print("     previous_operation=", previous_operation)
    if previous_operation != "":
        display_label.config(text=previous_operation)


def print_to_display(val):
    print("__FUNCTION__print_to_display(val)")
    print_last_display()
    current_text = display_label['text']
    if val - int(val) == 0:
        new_text = current_text + '\n' + str(int(val))
        display_label.config(text=new_text)
    else:
        new_text = current_text + '\n' + str(val)
        display_label.config(text=str(new_text))


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
            # INCORRECT FUNCTIONALITY RIGHT NOW
            # display_label.config(text="")
            print_to_display('')
        elif text == 'CE':
            # display_label.config(text="")
            print_to_display('')
        elif text == 'BSPC':
            # display_label.config(text=current_text[:len(current_text) - 1])
            print_to_display(int(current_text[:len(current_text) - 1]))
        elif text == '%':
            print('%')
        elif text == '1/x':
            try:
                print(type(current_text))
                new_val = 1 / float(current_text)
            except:
                raise Exception("Error, current_text == " + current_text + " which cannot be made into an int")
            print_to_display(new_val)
        elif text == 'x^2':
            try:
                new_val = float(current_text) ** 2
            except:
                raise Exception("Error, current_text == " + current_text + " which cannot be made into an int")
            print_to_display(new_val)
        elif text == 'sqrt(x)':
            try:
                new_val = sqrt(float(current_text))
            except:
                raise Exception("Error, current_text == " + current_text + " which cannot be made into an int")
            print_to_display(new_val)
        elif text == '/' or text == 'x' or text == '--' or text == '+':
            print("here")
            save_operation(current_text + ' ' + text)
        # elif text == 'x':
        #     print(text)
        # elif text == '--':
        #     print(text)
        # elif text == '+':
        #     print(text)
        elif text == '=':
            print(text)
        else:
            # print("here")
            raise Exception("Error, text not recognized")


# Holds the whole structure. So when you want to attach components, attach it to the root
root = tk.Tk()
# wrapper_canvas = tk.Canvas(root, height=1000, width=1000)
# wrapper_canvas.pack(fill="both", expand=True)


numpad_canvas = tk.Canvas(root, height=700, width=1400, bg="#263D42")
numpad_canvas.pack(fill="both", expand=True)

display = tk.Frame(root, height=700, width=700)
hist_mem = tk.Frame(root)

display_label = tk.Label(root, height=200, width=700, text="", background="white")
display_label.pack(fill="both", expand=True)
display_label.place(relx=0, rely=0, relwidth=0.495, relheight=0.24)

hist_label = tk.Label(root, height=200, width=700, text="History", background="green")
hist_label.pack(fill="both", expand=True)
hist_label.place(relx=0.5, rely=0, relwidth=0.495, relheight=0.124)

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
        button.place(relx=(current_col)*0.124, rely=0.125*current_row, relwidth=0.124, relheight=0.125)
        buttons.append(button)
        current_col += 1
    else:
        button = tk.Button(numpad_canvas, text=symbol, command=partial(on_button_press, symbol))
        if index % 4 == 0 and index != 0:
            current_row += 1
            current_col = 0
        button.place(relx=(current_col)*0.124, rely=0.125*current_row, relwidth=0.124, relheight=0.125)
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