"""
TODO
- Add functionality to operations and %
- Create history list
- Add memory
- Need to fix the floating point error somehow. Consider using the ASCII method 
"""

from functools import partial
from logging import exception
import tkinter as tk
from tkinter import filedialog, Text
import os
from math import sqrt
import decimal

decimal.setcontext(decimal.BasicContext)
decimal.getcontext()
# decimal.getcontext().prec = 5

buttons_symbols = ['%', 'CE', 'C', 'BSPC', '1/x', 'x^2', 'sqrt(x)', '/', '7', '8', '9', 'x', '4', '5', '6', '--', '1', '2', '3', '+', '-', '0', '.', '=']
numpad_buttons_symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '.']
history = []


previous_operation = ""
previous_operation_calculated = False
def execute_operation():
    # this function actually fulfills the operation found in previous_operation
    # should contain three terms
    global previous_operation_calculated
    global previous_operation
    history.append(previous_operation)
    operation_list = previous_operation.split()
    print("previous_operation = ", previous_operation)
    print("operation_list = ", operation_list)
    previous_operation_calculated = True
    if operation_list[1] == '/':
        # division
        return decimal.Decimal(operation_list[0]) / decimal.Decimal(operation_list[2])
    elif operation_list[1] == 'x':
        # multiply
        return decimal.Decimal(operation_list[0]) * decimal.Decimal(operation_list[2])
    elif operation_list[1] == '--':
        return decimal.Decimal(operation_list[0]) - decimal.Decimal(operation_list[2])
    elif operation_list[1] == '+':
        return decimal.Decimal(operation_list[0]) + decimal.Decimal(operation_list[2])
    else:
        raise Exception("Major error in compute_operation")
        


def save_operation(text):
    print("__FUNCTION__save_operation(val)")
    global previous_operation
    previous_operation = text
    prev_display_label.config(text=text)


def print_last_display():
    print("__FUNCTION__print_last_display()")
    # print("     previous_operation=", previous_operation)
    global previous_operation
    if previous_operation != "":
        prev_display_label.config(text=previous_operation)


def print_to_display(val):
    print("__FUNCTION__print_to_display(val)")
    # print_last_display()
    current_text = decimal.Decimal(display_label['text'])
    print(" current_text = ", current_text)
    print(" val = ", val)
    try:
        if float(val) - int(val) == 0:
            # new_text = current_text + '\n' + str(int(val))
            display_label.config(text=str(int(val)))
        else:
            # new_text = current_text + '\n' + str(val)
            display_label.config(text=str(val))
    except ValueError:
        display_label.config(text=str(val))


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
    global previous_operation
    global previous_operation_calculated
    if previous_operation_calculated:
        save_operation("")
        previous_operation_calculated = False
    if current_text != "":
        if text == 'C':
            # display_label.config(text="")
            display_label.config(text='')
            previous_operation = ''
            prev_display_label.config(text='')
        elif text == 'CE':
            # display_label.config(text="")
            display_label.config(text='')
        elif text == 'BSPC':
            # display_label.config(text=current_text[:len(current_text) - 1])
            print_to_display(current_text[:len(current_text) - 1])
        elif text == '%':
            print('%')
        elif text == '1/x':
            try:
                # print(type(current_text))
                new_val = 1 / float(current_text)
            except:
                raise Exception("Error, current_text == " + current_text + " which cannot be made into an int")
            print_to_display(new_val)
        elif text == 'x^2':
            try:
                new_val = decimal.Decimal(current_text) ** decimal.Decimal(2)
            except:
                raise Exception("Error, current_text == " + current_text + " which cannot be made into an int")
            print_to_display(new_val)
        elif text == 'sqrt(x)':
            try:
                new_val = decimal.Decimal(current_text).sqrt()
            except:
                raise Exception("Error, current_text == " + current_text + " which cannot be made into an int")
            print_to_display(new_val)
        elif text == '/' or text == 'x' or text == '--' or text == '+':
            save_operation(current_text + ' ' + text)
        # elif text == 'x':
        #     print(text)
        # elif text == '--':
        #     print(text)
        # elif text == '+':
        #     print(text)
        elif text == '=':
            # print(previous_operation)
            if previous_operation == '' or (len(previous_operation.split()) == 2 and previous_operation[-1] == '='):
                # print(previous_operation)
                # print(previous_operation[-1])
                save_operation(current_text + ' ' + text)
                print_to_display(current_text)
            else:
                save_operation(prev_display_label['text'] + ' ' + current_text + ' ' + text)
                value = execute_operation()
                print_to_display(value)


        else:
            # print("here")
            raise Exception("Error, text not recognized")


# Holds the whole structure. So when you want to attach components, attach it to the root
root = tk.Tk()
# wrapper_canvas = tk.Canvas(root, height=1000, width=1000)
# wrapper_canvas.pack(fill="both", expand=True)


numpad_canvas = tk.Canvas(root, height=700, width=1400, bg="#263D42")
numpad_canvas.pack(fill="both", expand=True)

display = tk.Frame(root, height=600, width=700)
hist_mem = tk.Frame(root)

display_label = tk.Label(root, height=200, width=700, text="", background="white")
prev_display_label = tk.Label(root, height=100, width=700, text="", background="gray")
display_label.pack(fill="both", expand=True)
prev_display_label.pack(fill="both", expand=True)
display_label.place(relx=0, rely=0.1, relwidth=0.495, relheight=0.12)
prev_display_label.place(relx=0, rely=0, relwidth=0.495, relheight= 0.12)

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