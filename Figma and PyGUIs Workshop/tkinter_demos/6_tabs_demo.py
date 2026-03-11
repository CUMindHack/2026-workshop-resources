import tkinter as tk
from tkinter import ttk # ttk provides extra functionality

root = tk.Tk()
root.title("Demo 5")
root.geometry("640x480")

# Create a 'notebook' which stores our tabs.
notebook = ttk.Notebook()
notebook.pack(expand=True, fill="both")

# Create frames that will serve as our tabs.
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Tab1")

tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Tab2")

tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="Tab3")

def main() -> None:
    root.mainloop()

if __name__ == "__main__":
    main()
