import tkinter as tk

root = tk.Tk()
root.title("Demo 3")
root.geometry("300x100")

fahrenheit = 0

# Notice that we are using 'grid' to format.
title_label = tk.Label(root, text="Celcius to Fahrenheit Converter")
title_label.grid(row=0, column=0, columnspan=3)

fahrenheit_label = tk.Label(root, text="Fahrenheit: 0")
fahrenheit_label.grid(row=3, column=0, columnspan=3)

celcius_label = tk.Label(root, text="Celcius: ").grid(row=1, column=0)
celsius_entry = tk.Entry(root)
celsius_entry.grid(row=1, column=1)

def calculate() -> None:
    global fahrenheit
    fahrenheit = float(celsius_entry.get()) * 9/5 + 32
    fahrenheit_label.config(text=f"Fahrenheit: {fahrenheit}")
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=1, column=2)

def main() -> None:
    root.mainloop()

if __name__ == "__main__":
    main()