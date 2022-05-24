"""
TODO
- Add functionality to operations and %
- Create history list
- Add memory
- Need to fix the floating point error somehow. Consider using the ASCII method 
"""

from functools import partial
import tkinter as tk
from tkinter import filedialog, Text
import os
import decimal

# class adapted from last comment in this forum post: https://stackoverflow.com/questions/70486666/tkinter-scrollbar-only-scrolls-downwards-and-cuts-off-content 
class ScrolledButtons(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.canvas = tk.Canvas(self)
        self.vsb = tk.Scrollbar(self, command=self.canvas.yview, orient="vertical")
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        for n in range(40):
            x = 2
            y = self.lasty + x
            btn = tk.Button(self.canvas, text=f'Button #{n}', justify="right", command=lambda te=n: self._on_click(te))
            self.canvas.create_window(20, y, anchor="nw", window=btn)
        bbox = self.canvas.bbox("all")
        self.canvas.configure(scrollregion=(0, 0, bbox[2], bbox[3]))

    @property
    def lasty(self):
        bbox = self.canvas.bbox("all")
        lasty = bbox[3] if bbox else 0
        return lasty
    
    def _on_click(text):
        print("will put the text in that button into the calculator again")


decimal.setcontext(decimal.BasicContext)
decimal.getcontext()
# decimal.getcontext().prec = 5

buttons_symbols = ['%', 'CE', 'C', 'BSPC', '1/x', 'x^2', 'sqrt(x)', '/', '7', '8', '9', 'x', '4', '5', '6', '--', '1', '2', '3', '+', '-', '0', '.', '=']
numpad_buttons_symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '.']
history = []


previous_operation = ""
previous_operation_calculated = False
last_action_was_operation = False


def update_history():
    global root



def execute_operation():
    # this function actually fulfills the operation found in previous_operation
    global previous_operation_calculated
    global previous_operation
    # history.append(previous_operation)
    operation_list = previous_operation.split()
    # print("previous_operation = ", previous_operation)
    # print("operation_list = ", operation_list)
    previous_operation_calculated = True
    result = ""
    # print('len(operation_list) = ' + str(len(operation_list)))
    if len(operation_list) == 4:
        # print(operation_list)
        if operation_list[1] == '/':
            # division
            # print(decimal.Decimal(operation_list[0]))
            # print(decimal.Decimal(operation_list[1]))
            result = decimal.Decimal(operation_list[0]) / decimal.Decimal(operation_list[2])
            # print(result)
        elif operation_list[1] == 'x':
            # multiply
            result = decimal.Decimal(operation_list[0]) * decimal.Decimal(operation_list[2])
        elif operation_list[1] == '--':
            result = decimal.Decimal(operation_list[0]) - decimal.Decimal(operation_list[2])
        elif operation_list[1] == '+':
            result = decimal.Decimal(operation_list[0]) + decimal.Decimal(operation_list[2])
        else:
            raise Exception("Major error in compute_operation")
    elif len(operation_list) == 2:
        result = operation_list[0]
    # print(result)
    # print(str(result))
    history.append(previous_operation + " " + str(result))
    print(history)
    update_history(previous_operation + " " + str(result))
    return result
        


def save_operation(text):
    # print("__FUNCTION__save_operation(val)")
    global previous_operation
    global last_action_was_operation
    last_action_was_operation = True
    previous_operation = text
    prev_display_label.config(text=text)


def print_last_display():
    # print("__FUNCTION__print_last_display()")
    # print("     previous_operation=", previous_operation)
    global previous_operation
    if previous_operation != "":
        prev_display_label.config(text=previous_operation)


def print_to_display(val):
    # print("__FUNCTION__print_to_display(val)")
    # print_last_display()
    # current_text = decimal.Decimal(display_label['text'])
    # print(" current_text = ", current_text)
    # print(" val = ", val)
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
    global last_action_was_operation
    global previous_operation_calculated
    if previous_operation_calculated:
        save_operation("")
        previous_operation_calculated = False
    if last_action_was_operation:
        display_label.config(text='')
        last_action_was_operation = False
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
    global previous_operation
    global previous_operation_calculated
    global last_action_was_operation
    # print("last_action_was_operation = ", last_action_was_operation)
    if previous_operation_calculated and text != 'CE':
        save_operation("")
        previous_operation_calculated = False
    current_text = display_label['text']
    if current_text != "":
        if text == 'C':
            # display_label.config(text="")
            display_label.config(text='')
            previous_operation = ''
            prev_display_label.config(text='')
            previous_operation_calculated = False
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
            # if last_action_was_operation, then need to get rid of the last operation and replace it with the new
            if last_action_was_operation:
                # print(previous_operation)
                previous_operation = previous_operation[:len(previous_operation) - 1]
                # print(previous_operation + ".")
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
                value = execute_operation()
                print_to_display(value)
            else:
                save_operation(prev_display_label['text'] + ' ' + current_text + ' ' + text)
                # print(previous_operation)
                value = execute_operation()
                print_to_display(value)


        else:
            # print("here")
            raise Exception("Error, text not recognized")


# Holds the whole structure. So when you want to attach components, attach it to the root
root = tk.Tk()
# wrapper_canvas = tk.Canvas(root, height=1000, width=1000)
# wrapper_canvas.pack(fill="both", expand=True)

# numpad_canvas = tk.Canvas(root, height=700, width=1400, bg="#263D42")
# numpad_canvas.pack(fill="both", expand=True)

display = tk.Frame(root, height=700, width=700, bg="#263D42")
display.pack(side=tk.LEFT, fill="both", expand=True)
hist_mem = tk.Frame(root, height=700, width=700, bg="#263D42")
hist_mem.pack(side=tk.RIGHT, fill="both", expand=True)

display_label = tk.Label(display, text="", background="white")
prev_display_label = tk.Label(display, text="", background="gray")
display_label.pack(fill="both", expand=True)
prev_display_label.pack(fill="both", expand=True)
display_label.place(relx=0, rely=0.1, relwidth=1, relheight=0.12)
prev_display_label.place(relx=0, rely=0, relwidth=1, relheight= 0.12)

hist_label = tk.Label(hist_mem, text="History", background="green")
hist_label.pack(fill="both", expand=True)
hist_label.place(relx=0, rely=0, relwidth=1, relheight=0.12)

hist_buttons = ScrolledButtons(hist_mem)
hist_buttons.pack(fill="both", expand=True)
hist_buttons.place(rely=0.12, relwidth=1, relheight=0.88)

# hist_frame_scroll = tk.Frame(hist_mem)
# hist_frame_scroll.pack(fill="both", expand=True)
# hist_frame_scroll.place(rely = 0.12, relwidth=1, relheight=1)

# hist_scrollbar = tk.Scrollbar(hist_frame_scroll, activebackground="#194D33", bg="#2F875B")
# hist_scrollbar.pack(side=tk.RIGHT, fill = tk.Y)

# hist_list = tk.Listbox(hist_frame_scroll, bg="#AECCBD", yscrollcommand=hist_scrollbar.set)
# hist_list.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
# # hist_list.place(relheight = 1, relwidth=0.9)

# for line in range(50):
#     hist_list.insert(tk.END, "          This is line number " + str(line))

# hist_scrollbar.config(command = hist_list.yview)

# frame = tk.Frame(canvas, bg="white")
# frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

buttons = []
next_row = False
current_row = 2
current_col = 0
for index, symbol in enumerate(buttons_symbols):
    if symbol in numpad_buttons_symbols:
        button = tk.Button(display, text=symbol, command=partial(on_numpad_press, symbol))
        if index % 4 == 0 and index != 0:
            current_row += 1
            current_col = 0
        button.place(relx=(current_col)*0.248, rely=0.125*current_row, relwidth=0.248, relheight=0.125)
        buttons.append(button)
        current_col += 1
    else:
        button = tk.Button(display, text=symbol, command=partial(on_button_press, symbol))
        if index % 4 == 0 and index != 0:
            current_row += 1
            current_col = 0
        button.place(relx=(current_col)*0.248, rely=0.125*current_row, relwidth=0.248, relheight=0.125)
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