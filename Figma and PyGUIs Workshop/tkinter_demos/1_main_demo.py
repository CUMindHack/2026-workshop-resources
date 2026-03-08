import tkinter as tk

# Create the winget surface for all of your widgets as 'root'.
root = tk.Tk()
root.title("Demo 1")
root.geometry("200x200") # Set the window to 200 x 200 pixels.

def main() -> None:
    # Create 3 labels with text that are associated with the 'root'.
    label_1 = tk.Label(root, text="Hello MindHack 2026!")
    label_2 = tk.Label(root, text="This is an example of a simple TKinter program!")
    label_3 = tk.Label(root, text="You can use it to create GUIs with Python!")
    # For each of the labels, format them.
    label_1.pack()
    label_2.pack()
    label_3.pack()

    # Call the loop which maintains the program.
    root.mainloop()

# Call 'main' if and only if this program was meant to be run.
if __name__ == "__main__":
    main()