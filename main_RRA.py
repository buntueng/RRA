#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


class MainUiApp:
    def __init__(self, master=None):
        # build ui
        self.main_toplevel = tk.Tk() if master is None else tk.Toplevel(master)
        self.main_toplevel.configure(height=200, width=200)
        self.main_toplevel.geometry("1024x768")
        self.main_toplevel.title("Research Review Assistance")
        self.top_frame = ttk.Frame(self.main_toplevel)
        self.top_frame.configure(height=200, width=1024)
        self.top_frame.grid(column=0, row=0, sticky="new")
        self.bottom_frame = ttk.Frame(self.main_toplevel)
        self.bottom_frame.configure(height=568, width=200)
        self.bottom_frame.grid(column=0, row=1, sticky="sew")

        # Main widget
        self.mainwindow = self.main_toplevel

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = MainUiApp()
    app.run()
