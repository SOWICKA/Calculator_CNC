import tkinter as tk
from tkinter import Label, Entry, Button, Text, filedialog

breite1 = 95
breite2 = 93
breite3 = 102


def zeige_tabelle(option):
    global optionen_frame, zurück_button, speichern_button, aktuelle_operation
    optionen_frame.destroy()

    aktuelle_operation = option

    for widget in app.winfo_children():
        if isinstance(widget, (Entry, Label, Button)):
            widget.destroy()

    tabelle = ""
    if option == "FRÄSEN":
        tabelle = hole_fräsen_tabelle()
    elif option == "BOHREN":
        tabelle = hole_bohren_tabelle()
    elif option == "PLANEN":
        tabelle = hole_planen_tabelle()
    elif option == "DREHEN":
        tabelle = hole_drehen_tabelle()

    text.delete("1.0", tk.END)
    text.insert(tk.END, tabelle)

    if 'speichern_button' in globals():
        speichern_button.destroy()
    zurück_zum_menu()


def hole_fräsen_tabelle():
    Label(app, text="Geben Sie die Schnittgeschwindigkeit Vc in m/min ein:").pack()
    vc_eingabe = Entry(app)
    vc_eingabe.pack()

    Label(app, text="Geben Sie den Werkzeugdurchmesser Ø in mm ein:").pack()
    fi_eingabe = Entry(app)
    fi_eingabe.pack()

    Label(app, text="Geben Sie die Anzahl der schneidenden Zähne Z ein:").pack()
    z_eingabe = Entry(app)
    z_eingabe.pack()

    Label(app, text="Geben Sie den Vorschub pro Zahn fz ein:").pack()
    fz_eingabe = Entry(app)
    fz_eingabe.pack()

    def berechnungen():
        try:
            vc2 = vc_eingabe.get().replace(",", ".")
            fi2 = fi_eingabe.get().replace(",", ".")
            z = z_eingabe.get()
            fz2 = fz_eingabe.get().replace(",", ".")

            if 0 < float(vc2) and 0 < float(fi2) and 0 < float(fz2) and 0 < int(z):
                umdrehungen = (float(vc2) * 1000) / (float(fi2) * 3.1416)
                ergebnis_umdrehungen.config(text=f"Berechnete Umdrehungen: {int(umdrehungen)} U/min")
                vorschub = int(umdrehungen) * float(fz2) * int(z)
                ergebnis_vorschub.config(text=f"Berechneter Vorschub: {int(vorschub)} mm/min")
            else:
                ergebnis_umdrehungen.config(text="Falsche Daten, überprüfen Sie die eingegebenen Werte.")
                ergebnis_vorschub.config(text="")
        except ValueError:
            ergebnis_umdrehungen.config(text="Ups.. Sie haben die Daten falsch eingegeben.")
            ergebnis_vorschub.config(text="")
        except Exception as e:
            ergebnis_umdrehungen.config(text=f"Fehler: {str(e)}")
            ergebnis_vorschub.config(text="")

    Button(app, text="Berechnen", command=berechnungen).pack()

    ergebnis_umdrehungen = Label(app, text="")
    ergebnis_umdrehungen.pack()

    ergebnis_vorschub = Label(app, text="")
    ergebnis_vorschub.pack()

    return (
        f"-{'-' * breite1}-\n"
        f"|               HILFSTABELLE FÜR DIE VORBRENNPARAMETER FÜR JEDES MATERIAL                       |\n"
        f"-{'-' * breite1}-\n"
        f"|                   FRÄSEN - PARAMETER FÜR WERKZEUGE AUS HARTMETALL                             |\n"
        f"*{'*' * breite1}*\n"
        f"| WL10(WKZ) | W(Profitool) | TZM(WKZ) | Mo(WKZ) |  STAHL (HPC)   | Ta (WKZ) |   ALU  |KUNSTSTOFF|\n"
        f"-{'-' * breite1}-\n"
        f"|    80     |     55-60    |    90    |   110   |      110       |    65    |   300  | 50-200   |Vc [m/min]\n"
        f"-{'-' * breite1}-\n"
        f"|   0.02    |      0.04    |   0.03   |   0.03  |      0.05      |   0.03   |  0.06  | 0.1-0.5  |fz [mm]\n"
        f"*{'*' * breite1}*\n"
    )


def hole_bohren_tabelle():
    Label(app, text="Geben Sie die Schnittgeschwindigkeit VC in m/min ein:").pack()
    vc_eingabe = Entry(app)
    vc_eingabe.pack()

    Label(app, text="Geben Sie den Werkzeugdurchmesser Ø in mm ein:").pack()
    fi_eingabe = Entry(app)
    fi_eingabe.pack()

    Label(app, text="Geben Sie den Vorschub pro Umdrehung f/U in mm ein:").pack()
    fu_eingabe = Entry(app)
    fu_eingabe.pack()

    def berechnungen():
        try:
            vc2 = vc_eingabe.get().replace(",", ".")
            fi2 = fi_eingabe.get().replace(",", ".")
            fu2 = fu_eingabe.get().replace(",", ".")

            if 0 < float(vc2) and 0 < float(fi2) and 0 < float(fu2):
                umdrehungen = (float(vc2) * 1000) / (float(fi2) * 3.1416)
                ergebnis_umdrehungen.config(text=f"Berechnete Umdrehungen: {int(umdrehungen)} U/min")
                vorschub = int(umdrehungen) * float(fu2)
                ergebnis_vorschub.config(text=f"Berechneter Vorschub: {int(vorschub)} mm/min")
            else:
                ergebnis_umdrehungen.config(text="Falsche Daten, überprüfen Sie die eingegebenen Werte.")
                ergebnis_vorschub.config(text="")
        except ValueError:
            ergebnis_umdrehungen.config(text="Ups.. Sie haben die Daten falsch eingegeben.")
            ergebnis_vorschub.config(text="")
        except Exception as e:
            ergebnis_umdrehungen.config(text=f"Fehler: {str(e)}")
            ergebnis_vorschub.config(text="")

    Button(app, text="Berechnen", command=berechnungen).pack()

    ergebnis_umdrehungen = Label(app, text="")
    ergebnis_umdrehungen.pack()

    ergebnis_vorschub = Label(app, text="")
    ergebnis_vorschub.pack()

    return (
        f"-{'-' * breite2}-\n"
        f"|             HILFSTABELLE FÜR DIE VORBRENNPARAMETER FÜR JEDES MATERIAL                     |\n"
        f"-{'-' * breite2}-\n"
        f"|           BOHREN - PARAMETER FÜR AUSGEWÄHLTE WERKZEUGE AUS GEHÄRTETEM STAHL               |\n"
        f"*{'*' * breite2}*\n"
        f"|   WL10    |      W10     |   TZM    |    Mo   |   STAHL   |    Ta    |   ALU   |KUNSTSTOFF|\n"
        f"-{'-' * breite2}-\n"
        f"|    30     |      30      |    90    |    90   |    45     |    40    |   150   |   180    |Vc [m/min]\n"
        f"-{'-' * breite2}-\n"
        f"|   0,02    |     0.04     |   0.03   |   0.03  |    0.1    |   0.03   |   0.2   |   0.15   |f/U [mm]\n"
        f"*{'*' * breite2}*\n"
    )

def hole_planen_tabelle():
    Label(app, text="Geben Sie die Schneidgeschwindigkeit VC in m/min ein:").pack()
    vc_eingabe = Entry(app)
    vc_eingabe.pack()

    Label(app, text="Geben Sie den Werkzeugdurchmesser Ø in mm ein:").pack()
    fi_eingabe = Entry(app)
    fi_eingabe.pack()

    Label(app, text="Geben Sie die Anzahl der schneidenden Zähne Z ein:").pack()
    z_eingabe = Entry(app)
    z_eingabe.pack()

    Label(app, text="Geben Sie den Vorschub pro Zahn fz ein:").pack()
    fz_eingabe = Entry(app)
    fz_eingabe.pack()

    def berechnungen():
        try:
            vc2 = vc_eingabe.get().replace(",", ".")
            fi2 = fi_eingabe.get().replace(",", ".")
            z = z_eingabe.get()
            fz2 = fz_eingabe.get().replace(",", ".")

            if 0 < float(vc2) and 0 < float(fi2) and 0 < int(z) and 0 < float(fz2):
                umdrehungen = (float(vc2) * 1000) / (float(fi2) * 3.1416)
                ergebnis_umdrehungen.config(text=f"Berechnete Umdrehungen: {int(umdrehungen)} U/min")
                vorschub = int(umdrehungen) * float(fz2) * int(z)
                ergebnis_vorschub.config(text=f"Berechneter Vorschub: {int(vorschub)} mm/min")
            else:
                ergebnis_umdrehungen.config(text="Falsche Daten, überprüfen Sie die eingegebenen Werte.")
                ergebnis_vorschub.config(text="")
        except ValueError:
            ergebnis_umdrehungen.config(text="Ups.. Sie haben die Daten falsch eingegeben.")
            ergebnis_vorschub.config(text="")
        except Exception as e:
            ergebnis_umdrehungen.config(text=f"Fehler: {str(e)}")
            ergebnis_vorschub.config(text="")

    Button(app, text="Berechnen", command=berechnungen).pack()

    ergebnis_umdrehungen = Label(app, text="")
    ergebnis_umdrehungen.pack()

    ergebnis_vorschub = Label(app, text="")
    ergebnis_vorschub.pack()

    return (
        f"-{'-' * breite1}-\n"
        f"|            HILFSTABELLE FÜR DIE PLANUNGSVORBEREITUNGSPARAMETER FÜR JEDES MATERIAL           |\n"
        f"-{'-' * breite1}-\n"
        f"|                           PARAMETER FÜR DREHFRÄSKÖPFE C270 & A270                           |\n"
        f"*{'*' * breite1}*\n"
        f"|WL10(H210T)| W(H210T)|TZM(H210T)|Mo(H210T)|STAL(GM 43)|Ta(H210T)|ALU(H216T)|KUNSTSTOFF(H216T)|\n"
        f"-{'-' * breite1}-\n"
        f"|    120    |    70    |    160   |   160   |    150    |    90   |   500   |        250      |Vc [m/min]\n"
        f"-{'-' * breite1}-\n"
        f"|   0.08    |   0.11   |   0.12   |   0.12  |    0.1    |   0.06  |  0.15   |     0.1-0.5     |fz [mm]\n"
        f"={'=' * breite1}=\n"
        f"|                            PARAMETER FÜR DREHFRÄSKÖPFE CHSC                                 |\n"
        f"-{'-' * breite1}-\n"
        f"|WL10(XDKT) | W(XDKT)  |TZM(XDKT) |Mo(XDKT) |STAL(GM 43)|Ta(XDKT) |ALU(XDKT) |KUNSTSTOFF(XDKT)|\n"
        f"-{'-' * breite1}-\n"
        f"|    140    |    85    |    180   |   180   |    150    |    95   |    500   |       260      |Vc [m/min]\n"
        f"-{'-' * breite1}-\n"
        f"|   0.08    |   0.08   |    0.1   |   0.1   |    0.08   |   0.05  |   0.15   |     0.1-0.6     |fz [mm]\n"
        f"={'=' * breite1}=\n"
    )

def hole_drehen_tabelle():
    Label(app, text="Geben Sie die Schnittgeschwindigkeit VC in m/min ein:").pack()
    vc_eingabe = Entry(app)
    vc_eingabe.pack()

    Label(app, text="Geben Sie den Werkzeugdurchmesser Ø in mm ein:").pack()
    fi_eingabe = Entry(app)
    fi_eingabe.pack()

    Label(app, text="Geben Sie den Vorschub pro Umdrehung f/U in mm ein:").pack()
    fu_eingabe = Entry(app)
    fu_eingabe.pack()

    def berechnungen():
        try:
            vc2 = vc_eingabe.get().replace(",", ".")
            fi2 = fi_eingabe.get().replace(",", ".")
            fu2 = fu_eingabe.get().replace(",", ".")

            if 0 < float(vc2) and 0 < float(fi2) and 0 < float(fu2):
                umdrehungen = (float(vc2) * 1000) / (float(fi2) * 3.1416)
                ergebnis_umdrehungen.config(text=f"Berechnete Umdrehungen: {int(umdrehungen)} U/min")
                vorschub = int(umdrehungen) * float(fu2)
                ergebnis_vorschub.config(text=f"Berechneter Vorschub: {int(vorschub)} mm/min")
            else:
                ergebnis_umdrehungen.config(text="Falsche Daten, überprüfen Sie die eingegebenen Werte.")
                ergebnis_vorschub.config(text="")
        except ValueError:
            ergebnis_umdrehungen.config(text="Ups.. Sie haben die Daten falsch eingegeben.")
            ergebnis_vorschub.config(text="")
        except Exception as e:
            ergebnis_umdrehungen.config(text=f"Fehler: {str(e)}")
            ergebnis_vorschub.config(text="")

    Button(app, text="Berechnen", command=berechnungen).pack()

    ergebnis_umdrehungen = Label(app, text="")
    ergebnis_umdrehungen.pack()

    ergebnis_vorschub = Label(app, text="")
    ergebnis_vorschub.pack()

    return (
        f"{'-' * breite3}\n"
        f"| Benötigte Daten, wie Schnittgeschwindigkeit VC und Vorschub pro Umdrehung f/U, finden Sie in den   |\n"
        f"| Tabellen der Werkzeughersteller. Geben Sie als Durchmesser des Materials Ø den größten Durchmesser |\n"
        f"| an, der gedreht wird...                                                                            |\n"
        f"{'-' * breite3}\n"
    )

def zurück_zum_menu():
    global optionen_frame,zurück_button, speichern_button
    if 'zurück_button' in globals():
        zurück_button.pack()

    optionen_frame = tk.Frame(app)
    optionen_frame.pack(pady=20)

    for option in optionen:
        button = erstelle_button(option)
        button.pack(side=tk.LEFT, padx=10)

    speichern_button = tk.Button(app, text="In Datei speichern", command=in_datei_speichern)
    speichern_button.pack()


optionen = ["FRÄSEN", "BOHREN", "PLANEN", "DREHEN"]

app = tk.Tk()
app.title("Schneidparameterrechner")

beschreibung = (
    "Willkommen beim Schneidparameterrechner!\n\n"
    "Um zu beginnen, wählen Sie eine der folgenden Optionen: FRÄSEN, BOHREN, PLANEN, DREHEN.\n"
    "Geben Sie die entsprechenden Daten ein und das Programm wird die erforderlichen Schneidparameter generieren.\n"
    "Sie können die berechneten Ergebnisse speichern, indem Sie auf SPEICHERN KLICKEN.\n\n"
    "Autor: Kamil S."
)

text = Text(app, height=20, width=110)
text.pack(pady=20)
text.insert(tk.END, beschreibung)


def erstelle_button(option):
    return tk.Button(optionen_frame, text=option, command=lambda: zeige_tabelle(option))


def in_datei_speichern():
    option = aktuelle_operation if 'aktuelle_operation' in globals() else "keine"
    ergebnis_drehzahl = ""
    ergebnis_vorschub = ""
    for widget in app.winfo_children():
        if isinstance(widget, tk.Label) and "Berechnete Drehzahl" in widget.cget("text"):
            ergebnis_drehzahl = widget.cget("text")
        elif isinstance(widget, tk.Label) and "Berechneter Vorschub" in widget.cget("text"):
            ergebnis_vorschub = widget.cget("text")

    inhalt = text.get("1.0", tk.END)
    datei = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Textdateien", "*.txt")])
    if datei:
        with open(datei, "w", encoding="utf-8") as f:
            f.write(inhalt)
            f.write("\n\n")
            f.write(f"Operation: {option}\n")
            f.write(f"{ergebnis_drehzahl}\n")
            f.write(f"{ergebnis_vorschub}\n")


speichern_button = tk.Button(app, text="In Datei speichern", command=in_datei_speichern)

optionen_frame = tk.Frame(app)
optionen_frame.pack(pady=20)

for option in optionen:
    button = erstelle_button(option)
    button.pack(side=tk.LEFT, padx=10)

speichern_button.pack()

app.mainloop()
