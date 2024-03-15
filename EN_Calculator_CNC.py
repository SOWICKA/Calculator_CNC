import tkinter as tk
from tkinter import Label, Entry, Button, Text, filedialog

width1 = 97
width2 = 93
width3 = 112

def show_table(option):
    global options_frame, back_button, save_button, current_operation
    options_frame.destroy()

    current_operation = option

    for widget in app.winfo_children():
        if isinstance(widget, (Entry, Label, Button)):
            widget.destroy()

    table = ""
    if option == "MILLING":
        table = get_milling_table()
    elif option == "DRILLING":
        table = get_drilling_table()
    elif option == "PLANING":
        table = get_planing_table()
    elif option == "TURNING":
        table = get_turning_table()

    text.delete("1.0", tk.END)
    text.insert(tk.END, table)

    if 'save_button' in globals():
        save_button.destroy()
    back_to_menu()

def get_milling_table():
    Label(app, text="Enter cutting speed Vc in m/min:").pack()
    vc_entry = Entry(app)
    vc_entry.pack()

    Label(app, text="Enter tool diameter Ø in mm:").pack()
    diameter_entry = Entry(app)
    diameter_entry.pack()

    Label(app, text="Enter number of cutting teeth Z:").pack()
    z_entry = Entry(app)
    z_entry.pack()

    Label(app, text="Enter feed per tooth fz:").pack()
    fz_entry = Entry(app)
    fz_entry.pack()

    def calculations():
        try:
            vc_value = vc_entry.get().replace(",", ".")
            diameter_value = diameter_entry.get().replace(",", ".")
            z_value = z_entry.get()
            fz_value = fz_entry.get().replace(",", ".")

            if 0 < float(vc_value) and 0 < float(diameter_value) and 0 < float(fz_value) and 0 < int(z_value):
                revolutions = (float(vc_value) * 1000) / (float(diameter_value) * 3.1416)
                revolutions_result.config(text=f"Calculated revolutions: {int(revolutions)} RPM")
                feed = int(revolutions) * float(fz_value) * int(z_value)
                feed_result.config(text=f"Calculated feed: {int(feed)} mm/min")
            else:
                revolutions_result.config(text="Incorrect data, please check the entered values.")
                feed_result.config(text="")
        except ValueError:
            revolutions_result.config(text="Oops.. You entered the data incorrectly")
            feed_result.config(text="")
        except Exception as e:
            revolutions_result.config(text=f"Error: {str(e)}")
            feed_result.config(text="")

    Button(app, text="Calculate", command=calculations).pack()

    revolutions_result = Label(app, text="")
    revolutions_result.pack()

    feed_result = Label(app, text="")
    feed_result.pack()

    return (
        f"-{'-'*width1}-\n"
        f"|      AUXILIARY TABLE OF INITIAL PARAMETERS NEEDED FOR CALCULATIONS FOR INDIVIDUAL MATERIALS     |\n"
        f"-{'-'*width1}-\n"
        f"|              {option}  - PARAMETERS SELECTED FOR TOOLS MADE OF SINTERED CARBIDE                  |\n"
        f"*{'*' * width1}*\n"
        f"| WL10(WYK) | W(Profitool) | TZM(WYK) | Mo(WYK) | STAINLESS(HPC) | Ta (WYK) |   ALU   | SYNTHETIC |\n"
        f"-{'-'*width1}-\n"
        f"|    80     |     55-60    |    90    |   110   |     110        |    65    |   300   |   50-200  |Vc [m/min]\n"
        f"-{'-'*width1}-\n"
        f"|   0.02    |      0.04    |   0.03   |   0.03  |     0.05       |   0.03   |  0.06   |  0.1-0.5  |fz [mm]\n"
        f"*{'*' * width1}*\n"
    )

def get_drilling_table():
    Label(app, text="Enter cutting speed VC in m/min:").pack()
    vc_entry = Entry(app)
    vc_entry.pack()

    Label(app, text="Enter tool diameter Ø in mm:").pack()
    diameter_entry = Entry(app)
    diameter_entry.pack()

    Label(app, text="Enter feed per revolution f/U in mm:").pack()
    fu_entry = Entry(app)
    fu_entry.pack()

    def calculations():
        try:
            vc_value = vc_entry.get().replace(",", ".")
            diameter_value = diameter_entry.get().replace(",", ".")
            fu_value = fu_entry.get().replace(",", ".")

            if 0 < float(vc_value) and 0 < float(diameter_value) and 0 < float(fu_value):
                revolutions = (float(vc_value) * 1000) / (float(diameter_value) * 3.1416)
                revolutions_result.config(text=f"Calculated revolutions: {int(revolutions)} RPM")
                feed = int(revolutions) * float(fu_value)
                feed_result.config(text=f"Calculated feed: {int(feed)} mm/min")
            else:
                revolutions_result.config(text="Incorrect data, please check the entered values.")
                feed_result.config(text="")
        except ValueError:
            revolutions_result.config(text="Oops.. You entered the data incorrectly")
            feed_result.config(text="")
        except Exception as e:
            revolutions_result.config(text=f"Error: {str(e)}")
            feed_result.config(text="")

    Button(app, text="Calculate", command=calculations).pack()

    revolutions_result = Label(app, text="")
    revolutions_result.pack()

    feed_result = Label(app, text="")
    feed_result.pack()

    return (
        f"{'-' * width2}\n"
        f"|   AUXILIARY TABLE OF INITIAL PARAMETERS NEEDED FOR CALCULATIONS FOR INDIVIDUAL MATERIALS  |\n"
        f"{'-' * width2}\n"
        f"|           DRILLING - PARAMETERS SELECTED FOR TOOLS MADE OF SINTERED CARBIDE               |\n"
        f"{'*' * width2}\n"
        f"|   WL10   |      W10     |   TZM    |    Mo   |  STAINLESS  |    Ta    |   ALU   |SYNTHETIC|\n"
        f"{'-' * width2}\n"
        f"|    30    |      30      |    90    |    90   |     45      |    40    |   150   |   180   |Vc [m/min]\n"
        f"{'-' * width2}\n"
        f"|   0.02   |     0.04     |   0.03   |   0.03  |     0.1     |   0.03   |   0.2   |   0.15  |f/U [mm]\n"
        f"{'*' * width2}\n"
    )

def get_planing_table():
    Label(app, text="Enter cutting speed VC in m/min:").pack()
    vc_entry = Entry(app)
    vc_entry.pack()

    Label(app, text="Enter tool diameter Ø in mm:").pack()
    diameter_entry = Entry(app)
    diameter_entry.pack()

    Label(app, text="Enter number of cutting teeth Z:").pack()
    z_entry = Entry(app)
    z_entry.pack()

    Label(app, text="Enter feed per tooth fz:").pack()
    fz_entry = Entry(app)
    fz_entry.pack()

    def calculations():
        try:
            vc_value = vc_entry.get().replace(",", ".")
            diameter_value = diameter_entry.get().replace(",", ".")
            z_value = z_entry.get()
            fz_value = fz_entry.get().replace(",", ".")

            if 0 < float(vc_value) and 0 < float(diameter_value) and 0 < int(z_value) and 0 < float(fz_value):
                revolutions = (float(vc_value) * 1000) / (float(diameter_value) * 3.1416)
                revolutions_result.config(text=f"Calculated revolutions: {int(revolutions)} RPM")
                feed = int(revolutions) * float(fz_value) * int(z_value)
                feed_result.config(text=f"Calculated feed: {int(feed)} mm/min")
            else:
                revolutions_result.config(text="Incorrect data, please check the entered values.")
                feed_result.config(text="")
        except ValueError:
            revolutions_result.config(text="Oops.. You entered the data incorrectly")
            feed_result.config(text="")
        except Exception as e:
            revolutions_result.config(text=f"Error: {str(e)}")
            feed_result.config(text="")

    Button(app, text="Calculate", command=calculations).pack()

    revolutions_result = Label(app, text="")
    revolutions_result.pack()

    feed_result = Label(app, text="")
    feed_result.pack()

    return (
        f"{'-' * width1}\n"
        f"|     AUXILIARY TABLE OF INITIAL PARAMETERS NEEDED FOR CALCULATIONS FOR INDIVIDUAL MATERIALS    |\n"
        f"{'-' * width1}\n"
        f"|                      PARAMETERS SELECTED FOR PLANING HEADS C270 & A270                        |\n"
        f"{'*' * width1}\n"
        f"|WL10(H210T)|W(H210T)|TZM(H210T)|Mo(H210T)|STAINLESS(GM43)|Ta(H210T)|ALU(H216T)|SYNTHETIC(H216T)|\n"
        f"{'-' * width1}\n"
        f"|    120    |   70   |    160   |   160   |      150      |    90   |    500   |       250      |Vc [m/min]\n"
        f"{'-' * width1}\n"
        f"|    0.08   |   0.11 |    0.12  |   0.12  |      0.1      |   0.06  |    0.15  |     0.1-0.5    |fz [mm]\n"
        f"{'=' * width1}\n"
        f"|                         PARAMETERS SELECTED FOR PLANING HEADS CHSC                            |\n"
        f"{'-' * width1}\n"
        f"|WL10(XDKT) |W(XDKT) |TZM(XDKT) |Mo(XDKT) |STAINLESS(GM43)|Ta(XDKT) | ALU(XDKT) |SYNTHETIC(XDKT)|\n"
        f"{'-' * width1}\n"
        f"|    140    |   85   |    180   |   180   |      150      |    95   |    500    |      260      |Vc [m/min]\n"
        f"{'-' * width1}\n"
        f"|    0.08   |   0.08 |    0.1   |   0.1   |      0.08     |   0.05  |    0.12   |    0.1-0.5    |fz [mm]\n"
        f"{'*' * width1}\n"
    )

def get_turning_table():
    Label(app, text="Enter cutting speed VC in m/min:").pack()
    vc_entry = Entry(app)
    vc_entry.pack()

    Label(app, text="Enter material diameter Ø in mm:").pack()
    diameter_entry = Entry(app)
    diameter_entry.pack()

    Label(app, text="Enter feed per revolution f/U in mm:").pack()
    fu_entry = Entry(app)
    fu_entry.pack()

    def calculations():
        try:
            vc_value = vc_entry.get().replace(",", ".")
            diameter_value = diameter_entry.get().replace(",", ".")
            fu_value = fu_entry.get().replace(",", ".")

            if 0 < float(vc_value) and 0 < float(diameter_value) and 0 < float(fu_value):
                revolutions = (float(vc_value) * 1000) / (float(diameter_value) * 3.1416)
                revolutions_result.config(text=f"Calculated revolutions: {int(revolutions)} RPM")
                feed = int(revolutions) * float(fu_value)
                feed_result.config(text=f"Calculated feed: {int(feed)} mm/min")
            else:
                revolutions_result.config(text="Incorrect data, please check the entered values.")
                feed_result.config(text="")
        except ValueError:
            revolutions_result.config(text="Oops.. You entered the data incorrectly")
            feed_result.config(text="")
        except Exception as e:
            revolutions_result.config(text=f"Error: {str(e)}")
            feed_result.config(text="")

    Button(app, text="Calculate", command=calculations).pack()

    revolutions_result = Label(app, text="")
    revolutions_result.pack()

    feed_result = Label(app, text="")
    feed_result.pack()

    return (
        f"{'-' * width3}\n"
        f"| Necessary data, i.e., cutting speed VC and feed per revolution f/U,                                          |\n"
        f"| can be found in the tool parameter tables of the tool manufacturer,                                          |\n"
        f"| and as the diameter of the material Ø, enter the largest diameter to be turned...                            |\n"
        f"{'-' * width3}\n"
    )

def back_to_menu():
    global options_frame, back_button, save_button
    if 'back_button' in globals():
        back_button.destroy()

    options_frame = tk.Frame(app)
    options_frame.pack(pady=20)

    for option in options:
        button = create_button(option)
        button.pack(side=tk.LEFT, padx=10)

    save_button = tk.Button(app, text="Save to file", command=save_to_file)
    save_button.pack()

options = ["MILLING", "DRILLING", "PLANING", "TURNING"]

app = tk.Tk()
app.title("Cutting Parameters Calculator")

description = (
    "Welcome to the Cutting Parameters Calculator!\n\n"
    "To get started, select one of the options: MILLING, DRILLING, PLANING, TURNING.\n"
    "Enter the necessary data, and the program will generate the required cutting parameters.\n"
    "You can save the calculated results by clicking SAVE TO FILE.\n\n"
    "Author: Kamil S."
)

text = Text(app, height=20, width=112)
text.pack(pady=20)
text.insert(tk.END, description)


def create_button(option):
    return tk.Button(options_frame, text=option, command=lambda: show_table(option))


def save_to_file():
    option = current_operation if 'current_operation' in globals() else "none"
    revolutions_result = ""
    feed_result = ""
    for widget in app.winfo_children():
        if isinstance(widget, tk.Label) and "Calculated revolutions" in widget.cget("text"):
            revolutions_result = widget.cget("text")
        elif isinstance(widget, tk.Label) and "Calculated feed" in widget.cget("text"):
            feed_result = widget.cget("text")

    content = text.get("1.0", tk.END)
    file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file:
        with open(file, "w", encoding="utf-8") as f:
            f.write(content)
            f.write("\n\n")
            f.write(f"Operation: {option}\n")
            f.write(f"{revolutions_result}\n")
            f.write(f"{feed_result}\n")


save_button = tk.Button(app, text="Save to file", command=save_to_file)

options_frame = tk.Frame(app)
options_frame.pack(pady=20)

for option in options:
    button = create_button(option)
    button.pack(side=tk.LEFT, padx=10)

save_button.pack()

app.mainloop()

