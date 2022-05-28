import tkinter as tk
from config import buttons_symbols, numpad_buttons_symbols


class Display(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.display = tk.Frame(root, height=700, width=700, bg="#263D42")
        self.display.pack(side=tk.LEFT, fill="both", expand=True)

        self.display_label = tk.Label(self.display, text="", background="white")
        self.prev_display_label = tk.Label(self.display, text="", background="gray")
        self.display_label.pack(fill="both", expand=True)
        self.prev_display_label.pack(fill="both", expand=True)
        self.display_label.place(relx=0, rely=0.1, relwidth=1, relheight=0.12)
        self.prev_display_label.place(relx=0, rely=0, relwidth=1, relheight= 0.12)



class Numberpad(Display, tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.buttons = []
        self.next_row = False
        self.current_row = 2
        self.current_col = 0
        for index, symbol in enumerate(buttons_symbols):
            if symbol in numpad_buttons_symbols:
                button = tk.Button(self.display, text=symbol)
                if index % 4 == 0 and index != 0:
                    self.current_row += 1
                    self.current_col = 0
                button.place(relx=(self.current_col)*0.248, rely=0.125*self.current_row, relwidth=0.248, relheight=0.125)
                self.buttons.append(button)
                self.current_col += 1
            else:
                button = tk.Button(self.display, text=symbol)
                if index % 4 == 0 and index != 0:
                    self.current_row += 1
                    self.current_col = 0
                button.place(relx=(self.current_col)*0.248, rely=0.125*self.current_row, relwidth=0.248, relheight=0.125)
                self.buttons.append(button)
                self.current_col += 1
