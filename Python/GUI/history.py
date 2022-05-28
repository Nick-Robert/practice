from asyncio.windows_events import NULL
import tkinter as tk
from config import history

class History(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.hist_mem = tk.Frame(root, height=700, width=700, bg="#263D42")
        self.hist_mem.pack(side=tk.RIGHT, fill="both", expand=True)

        self.hist_label = tk.Label(self.hist_mem, text="History", background="green")
        self.hist_label.pack(fill="both", expand=True)
        self.hist_label.place(relx=0, rely=0, relwidth=1, relheight=0.12)
    

# class adapted from last comment in this forum post: https://stackoverflow.com/questions/70486666/tkinter-scrollbar-only-scrolls-downwards-and-cuts-off-content 
class HistoryButtons(History, tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.buttons = []
        self.canvas = tk.Canvas(self.hist_mem)
        self.vsb = tk.Scrollbar(self.hist_mem, command=self.canvas.yview, orient="vertical")
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

    @property
    def lasty(self):
        # returns the bottom y coordinate
        bbox = self.canvas.bbox("all")
        lasty = bbox[3] if bbox else 0
        return lasty
    
    def _on_click(self, text):
        print(text)
    
    def _remove_all_buttons(self):
        self.canvas.delete("all")
    
    def _add_all_buttons(self):
        for index, operation in enumerate(history):
            x = 20
            y = self.lasty + x
            btn = tk.Button(self.canvas, text=operation, justify="center")
            self.canvas.create_window(20, y, anchor="nw", window=btn)
            self.buttons.append(btn)
        bbox = self.canvas.bbox("all")
        self.canvas.configure(scrollregion=(0, 0, bbox[2], bbox[3]))
