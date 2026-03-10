import copy
from dataclasses import dataclass
import tkinter as tk

"""
'@dataclass' just generates the '__init__' by taking all variables and turning them into
*args or **kwargs for __init__.
```original
@dataclass
class Example:
    arg1: int
    arg2: bool
    kwarg1: str = "hi"
    kwarg2: int = 0
```
```generated
class Example:
    def __init__(self, arg1: int, arg2: bool, kwarg1: str = "hi", kwarg2: int = 0):
        self.arg1 = arg1
        self.arg2 = arg2
        self.kwarg1 = kwarg1
        self.kwarg2 = kwarg2
```
"""

# for 'with' keyword stuff
class Scope():
    def __init__(self, enter, exit):
        self.enter = enter
        self.exit = exit

    def __enter__(self, *args, **kwargs):
        return self.enter()

    def __exit__(self, *args, **kwargs):
        return self.exit()

# for setting the way that ui gets layed out
@dataclass
class UI_Options:
    inline: bool = True
    sticky: str = "w"

# for storing a div level
@dataclass
class UI_DIV:
    frame: tk.Frame
    row: int = 0
    col: int = 0
    options: UI_Options = UI_Options

class UI_State:
    def __init__(self, root, ui_options=UI_Options()):
        self.div_stack = [UI_DIV(root, options=ui_options)]
        self.row = 0
        self.col = 0

    def current_div(self):
        return self.div_stack[-1]

    def open_div(self, ui_options=UI_Options()):
        f = self.new_item(tk.Frame)
        div = UI_DIV(f, options=ui_options)
        self.div_stack.append(div)
        return div

    def close_div(self):
        self.div_stack.pop()

    def scope_div(self, ui_options=UI_Options()):
        x = Scope(
                lambda: self.open_div(ui_options=ui_options),
                self.close_div)
        return x

    def new_item(self, constructor, *args, ui_options=None, **kwargs):
        div = self.current_div()
        opts = div.options
        if ui_options:
            opts = copy.copy(opts) # WARN: shallow copy
            for k, v in vars(ui_options).items():
                setattr(opts, k, v)

        x = constructor(div.frame, *args, **kwargs)
        x.grid(row=div.row, column=div.col, sticky=div.options.sticky)

        if opts.inline:
            div.col += 1
        else:
            div.row += 1
            div.col = 0
        return x

def init_ui():
    root = tk.Tk()
    root.title("Demo 4")
    root.geometry("800x600")
    root.resizable(False, False)
    root.config(padx=16, pady=16)

    base_options = UI_Options()
    ui = UI_State(root, base_options)

    with ui.scope_div(UI_Options(inline=True):
        with ui.scope_div():
            title_label = ui.new_item(tk.Label, text="MindHack Registration Form Demo")
            title_label.grid(columnspan=2)

        with ui.scope_div():
            ui.new_item(tk.Label, text="Name")
            name_entry = ui.new_item(tk.Entry)

        with ui.scope_div():
            ui.new_item(tk.Label, text="Year")
            year_entry = ui.new_item(tk.Entry)

        with ui.scope_div():
            ui.new_item(tk.Label, text="Degree")
            degree_entry = ui.new_item(tk.Entry)

        with ui.scope_div():
            check_var = tk.IntVar()
            ui.new_item(tk.Label, text="Do you consent to photography?")
            consent_checkbutton = ui.new_item(tk.Checkbutton, variable=check_var)

        with ui.scope_div():
            ui.new_item(tk.Label, text="Tell us about yourself.")
            bio_entry = ui.new_item(tk.Text, width=40, height=10)

        with ui.scope_div():
            def handle_submit() -> None:
                data = {
                    "name" : name_entry.get(),
                    "year" : year_entry.get(),
                    "degree" : degree_entry.get(),
                    "consent" : check_var.get(),
                    "bio" : bio_entry.get("1.0", tk.END) # From line 1, char 0 to the end.
                }
                print(data)

            submit_button = ui.new_item(tk.Button, text="Submit", command=handle_submit)
            submit_button.grid(ipadx=30)

    return root

def main() -> None:
    root = init_ui()
    root.mainloop()

if __name__ == "__main__":
    main()
