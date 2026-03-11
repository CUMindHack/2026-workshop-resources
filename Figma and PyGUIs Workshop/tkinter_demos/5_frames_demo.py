import tkinter as tk

root = tk.Tk()
root.title("Demo 5")
root.geometry("640x480")
root.resizable(False, False)
root.config(padx=16, pady=16)

for i in range(2): root.grid_rowconfigure(i, weight=1)
for i in range(2): root.grid_columnconfigure(i, weight=1)

frame1 = tk.Frame(root, highlightbackground="#444444", highlightthickness=1)
frame1.grid(row=0, column=0, rowspan=2, sticky="nsew", padx=2, pady=2)

f1_label1 = tk.Label(frame1, text="Frame 1")
f1_label1.pack()

frame2 = tk.Frame(root, highlightbackground="#444444", highlightthickness=1)
frame2.grid(row=0, column=1, sticky="nsew", padx=2, pady=2)

f2_label1 = tk.Label(frame2, text="Frame 2")
f2_label1.pack()

frame3 = tk.Frame(root, highlightbackground="#444444", highlightthickness=1)
frame3.grid(row=1, column=1, sticky="nsew", padx=2, pady=2)

f3_label1 = tk.Label(frame3, text="Frame 3")
f3_label1.pack()

def main() -> None:
    root.mainloop()

if __name__ == "__main__":
    main()
