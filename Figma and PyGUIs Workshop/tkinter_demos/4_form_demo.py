import tkinter as tk

root = tk.Tk()
root.title("Demo 4")
root.geometry("540x350")
root.resizable(False, False)
root.config(padx=16, pady=16)

for i in range(5): root.columnconfigure(i, weight=1)

title_label = tk.Label(root, text="MindHack Registration Form Demo")
title_label.grid(row=0, column=0, columnspan=2, sticky="w")

name_label = tk.Label(root, text="Name")
name_label.grid(row=1, column=0, sticky="w")
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1, sticky="w")

year_label = tk.Label(root, text="Year")
year_label.grid(row=2, column=0, sticky="w")
year_entry = tk.Entry(root)
year_entry.grid(row=2, column=1, sticky="w")

degree_label = tk.Label(root, text="Degree")
degree_label.grid(row=3, column=0, sticky="w")
degree_entry = tk.Entry(root)
degree_entry.grid(row=3, column=1, sticky="w")

check_var = tk.IntVar()
consent_label = tk.Label(root, text="Do you consent to photography?")
consent_label.grid(row=4, column=0, sticky="w")
consent_checkbutton = tk.Checkbutton(root, variable=check_var)
consent_checkbutton.grid(row=4, column=1, sticky="w")

bio_label = tk.Label(root, text="Tell us about yourself.")
bio_label.grid(row=5, column=0, sticky="w")
bio_entry = tk.Text(root, width=40, height=10)
bio_entry.grid(row=5, column=1, sticky="w")

def handle_submit() -> None:
    data = {
        "name" : name_entry.get(),
        "year" : year_entry.get(),
        "degree" : degree_entry.get(),
        "consent" : check_var.get(),
        "bio" : bio_entry.get("1.0", tk.END) # From line 1, char 0 to the end.
    }

    print(data)

submit_button = tk.Button(root, text="Submit", command=handle_submit)
submit_button.grid(row=7, column=0, sticky="w",ipadx=30)

def main() -> None:
    root.mainloop()

if __name__ == "__main__":
    main()