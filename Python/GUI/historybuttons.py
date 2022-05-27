import tkinter as tk

# class adapted from last comment in this forum post: https://stackoverflow.com/questions/70486666/tkinter-scrollbar-only-scrolls-downwards-and-cuts-off-content 
class HistoryButtons(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.canvas = tk.Canvas(self)
        self.vsb = tk.Scrollbar(self, command=self.canvas.yview, orient="vertical")
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
        # print("will remove all buttons in the canvas")
        self.canvas.delete("all")
    
    def _add_all_buttons(self):
        # print("will add all buttons according to what's in the history list")
        for n in range(40):
            x = 20
            y = self.lasty + x
            btn = tk.Button(self.canvas, text=f'Button #{n}', justify="right", command=lambda te=n: self._on_click(te))
            self.canvas.create_window(20, y, anchor="nw", window=btn)
        bbox = self.canvas.bbox("all")
        self.canvas.configure(scrollregion=(0, 0, bbox[2], bbox[3]))