import tkinter as tk

root = tk.Tk()
root.title("Demo 5")
root.geometry("540x350")
root.resizable(False, False)
root.config(padx=16, pady=16)

def main() -> None:
    root.mainloop()

if __name__ == "__main__":
    main()