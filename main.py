from tkinter import ttk
import tkinter as tk

from user_interface.gui import CardApp

def main():
    # style = ttk.Style()
    # style.theme_use("clam")  # or 'vista', 'xpnative', 'alt', etc.

    root = tk.Tk()
    app = CardApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
