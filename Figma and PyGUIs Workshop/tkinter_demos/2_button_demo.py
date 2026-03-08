import tkinter as tk

# Create the winget surface for all of your widgets as 'root'.
root = tk.Tk()
root.title("Demo 2")
root.geometry("200x200") # Set the window to 200 x 200 pixels.

# Global Variables
x = 0

# Create a label that will display 'x'
label = tk.Label(root, text=f"{x}")

# Create a function associated with a button.
def increment() -> None:
    global x
    x += 1
    label.config(text=f"{x}") # Updates the label.

button = tk.Button(root, text="Add 1", command=increment) # Pass the 'increment' as a function.

# Format label and button.
label.pack()
button.pack()

# Main Method
def main() -> None:
    root.mainloop()

if __name__ == "__main__":
    main()