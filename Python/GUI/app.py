"""
TODO
- Add functionality to %
- Make the default value be 0
- Add memory
- Need to fix the floating point error somehow. Consider using the ASCII method 

DONE
- Refactor code to be OO
- Create history list

"""

from history import HistoryButtons
from display import Numberpad
import tkinter as tk
import decimal
from config import buttons_symbols, numpad_buttons_symbols, history


class StandardCalculator(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.numpad = Numberpad(root)
        self.history_and_mem = HistoryButtons(root)
        # self.history_and_mem.pack(fill="both", expand=True)
        # self.history_and_mem.place(relx=0.5,rely=0.12, relwidth=1, relheight=0.88)
        # self.hist_mem.place(rely=0.12, relwidth=1, relheight=0.88)
        # self.history_and_mem._add_all_buttons()

        # self.hist_label = tk.Label(self.hist_mem, text="History", background="green")
        # self.hist_label.pack(fill="both", expand=True)
        # self.hist_label.place(relx=0, rely=0, relwidth=1, relheight=0.12)

        # self.hist_buttons = HistoryButtons(self.hist_mem)
        # self.hist_buttons.pack(fill="both", expand=True)
        # self.hist_buttons.place(rely=0.12, relwidth=1, relheight=0.88)
        # self.hist_buttons._add_all_buttons()

        self.previous_operation = ""
        self.previous_operation_calculated = False
        self.last_action_was_operation = False

        self.next_row = False
        self.current_row = 2
        self.current_col = 0

        self._configure_numpad_buttons()
    
    def _configure_numpad_buttons(self):
        for index, button in enumerate(self.numpad.buttons):
            btn_text = button['text']
            if btn_text in numpad_buttons_symbols:
                button.config(command=lambda te=btn_text: self._on_numpad_press(te))
            elif btn_text in buttons_symbols:
                button.config(command=lambda te=btn_text: self._on_button_press(te))
            else:
                raise Exception("Error in configure_numpad_buttons")
    
    def _configure_history_buttons(self):
        for index, button in enumerate(self.history_and_mem.buttons):
            btn_text = button['text']
            button.config(command=lambda te=btn_text: self._on_histbutton_press(te))

    def _on_histbutton_press(self, operation):
        op_list = operation.split()
        if len(op_list) > 3:
            op_first_half = op_list[0] + " " + op_list[1] + " " + op_list[2] + " " + op_list[3]
            self.previous_operation_calculated = True
            self.previous_operation = operation
            self.numpad.prev_display_label.config(text=op_first_half)
            self.numpad.display_label.config(text=op_list[4])
        elif len(op_list) == 3:
            op_first_half = op_list[0] + " " + op_list[1]
            self.previous_operation_calculated = True
            self.previous_operation = operation
            self.numpad.prev_display_label.config(text=op_first_half)
            self.numpad.display_label.config(text=op_list[2])
        else:
            raise Exception("Error with history button function")

    def execute_operation(self):
        operation_list = self.previous_operation.split()
        self.previous_operation_calculated = True
        result = ""
        if len(operation_list) == 4:
            if operation_list[1] == '/':
                result = decimal.Decimal(operation_list[0]) / decimal.Decimal(operation_list[2])
            elif operation_list[1] == 'x':
                result = decimal.Decimal(operation_list[0]) * decimal.Decimal(operation_list[2])
            elif operation_list[1] == '--':
                result = decimal.Decimal(operation_list[0]) - decimal.Decimal(operation_list[2])
            elif operation_list[1] == '+':
                result = decimal.Decimal(operation_list[0]) + decimal.Decimal(operation_list[2])
            else:
                raise Exception("Major error in compute_operation")
        elif len(operation_list) == 2:
            result = operation_list[0]
        history.append(self.previous_operation + " " + str(result))
        self.history_and_mem._remove_all_buttons()
        self.history_and_mem._add_all_buttons()
        self._configure_history_buttons()
        return result
            
    def save_operation(self, text):
        self.last_action_was_operation = True
        self.previous_operation = text
        self.numpad.prev_display_label.config(text=text)

    def print_last_display(self):
        if self.previous_operation != "":
            self.numpad.prev_display_label.config(text=self.previous_operation)

    def print_to_display(self, val):
        try:
            if float(val) - int(val) == 0:
                self.numpad.display_label.config(text=str(int(val)))
            else:
                self.numpad.display_label.config(text=str(val))
        except ValueError:
            self.numpad.display_label.config(text=str(val))

    def _on_numpad_press(self, text):
        if self.previous_operation_calculated:
            self.save_operation("")
            self.previous_operation_calculated = False
        if self.last_action_was_operation:
            self.numpad.display_label.config(text='')
            self.last_action_was_operation = False
        current_text = self.numpad.display_label['text']
        if text != '-':
            self.numpad.display_label.config(text=current_text+text)
        elif text == '-' and current_text != "":
            if current_text[0] == '-':
                self.numpad.display_label.config(text=current_text[1:])
            else:
                self.numpad.display_label.config(text='-'+current_text)
        elif text == '-' and current_text == "":
            self.numpad.display_label.config(text="")
        else:
            self.numpad.display_label.config(text="error")

    def _on_button_press(self, text):
        if self.previous_operation_calculated and text != 'CE':
            self.save_operation("")
            self.previous_operation_calculated = False
        current_text = self.numpad.display_label['text']
        if current_text != "":
            if text == 'C':
                self.numpad.display_label.config(text='')
                self.previous_operation = ''
                self.numpad.prev_display_label.config(text='')
                self.previous_operation_calculated = False
            elif text == 'CE':
                self.numpad.display_label.config(text='')
            elif text == 'BSPC':
                self.print_to_display(current_text[:len(current_text) - 1])
            elif text == '%':
                print('%')
            elif text == '1/x':
                try:
                    new_val = 1 / float(current_text)
                except:
                    raise Exception("Error, current_text == " + current_text + " which cannot be made into an int")
                self.print_to_display(new_val)
            elif text == 'x^2':
                try:
                    new_val = decimal.Decimal(current_text) ** decimal.Decimal(2)
                except:
                    raise Exception("Error, current_text == " + current_text + " which cannot be made into an int")
                self.print_to_display(new_val)
            elif text == 'sqrt(x)':
                try:
                    new_val = decimal.Decimal(current_text).sqrt()
                except:
                    raise Exception("Error, current_text == " + current_text + " which cannot be made into an int")
                self.print_to_display(new_val)
            elif text == '/' or text == 'x' or text == '--' or text == '+':
                # if last_action_was_operation, then need to get rid of the last operation and replace it with the new
                if self.last_action_was_operation:
                    self.previous_operation = self.previous_operation[:len(self.previous_operation) - 1]
                self.save_operation(current_text + ' ' + text)
            elif text == '=':
                if self.previous_operation == '' or (len(self.previous_operation.split()) == 2 and self.previous_operation[-1] == '='):
                    self.save_operation(current_text + ' ' + text)
                    value = self.execute_operation()
                    self.print_to_display(value)
                else:
                    self.save_operation(self.numpad.prev_display_label['text'] + ' ' + current_text + ' ' + text)
                    value = self.execute_operation()
                    self.print_to_display(value)
            else:
                # print("here")
                raise Exception("Error, text not recognized")


# decimals in an attempt to get rid of floating point error
decimal.setcontext(decimal.BasicContext)
decimal.getcontext()


root = tk.Tk()
calc = StandardCalculator(root)

root.mainloop()