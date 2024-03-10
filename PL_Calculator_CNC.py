import tkinter as tk
from tkinter import Label, Entry, Button, Text, filedialog

szer1 = 95
szer2 = 93
szer3 = 101


def pokaz_tabele(opcja):
    global opcje_frame, powrot_przycisk, przycisk_zapisu, aktualna_operacja
    opcje_frame.destroy()

    aktualna_operacja = opcja

    for widget in app.winfo_children():
        if isinstance(widget, (Entry, Label, Button)):
            widget.destroy()

    tabela = ""
    if opcja == "FREZOWANIE":
        tabela = get_tabela_frezowanie()
    elif opcja == "WIERCENIE":
        tabela = get_tabela_wiercenie()
    elif opcja == "PLANOWANIE":
        tabela = get_tabela_planowanie()
    elif opcja == "TOCZENIE":
        tabela = get_tabela_toczenie()

    text.delete("1.0", tk.END)
    text.insert(tk.END, tabela)

    if 'przycisk_zapisu' in globals():
        przycisk_zapisu.destroy() 
    powrot_do_menu()

def get_tabela_frezowanie():
    Label(app, text="Podaj predkosc skrawania Vc w m/min:").pack()
    vc_entry = Entry(app)
    vc_entry.pack()

    Label(app, text="Podaj srednice narzedzia Ø w mm:").pack()
    fi_entry = Entry(app)
    fi_entry.pack()

    Label(app, text="Podaj liczbe zebow skrawajacych Z:").pack()
    z_entry = Entry(app)
    z_entry.pack()

    Label(app, text="Podaj posuw na zab fz:").pack()
    fz_entry = Entry(app)
    fz_entry.pack()

    def obliczenia():
        try:
            vc2 = vc_entry.get().replace(",", ".")
            fi2 = fi_entry.get().replace(",", ".")
            z = z_entry.get()
            fz2 = fz_entry.get().replace(",", ".")

            if 0 < float(vc2) and 0 < float(fi2) and 0 < float(fz2) and 0 < int(z):
                obroty = (float(vc2) * 1000) / (float(fi2) * 3.1416)
                wynik_obroty.config(text=f"Wyliczone obroty to: {int(obroty)} U/min")
                posuw = int(obroty) * float(fz2) * int(z)
                wynik_posuw.config(text=f"Wyliczony posuw to: {int(posuw)} mm/min")
            else:
                wynik_obroty.config(text="Błędne dane, sprawdź wprowadzone wartości.")
                wynik_posuw.config(text="")
        except ValueError:
            wynik_obroty.config(text="Ups.. Podales dane w sposob niepoprawny")
            wynik_posuw.config(text="")
        except Exception as e:
            wynik_obroty.config(text=f"Błąd: {str(e)}")
            wynik_posuw.config(text="")


    Button(app, text="Oblicz", command=obliczenia).pack()


    wynik_obroty = Label(app, text="")
    wynik_obroty.pack()

    wynik_posuw = Label(app, text="")
    wynik_posuw.pack()

    return (
        f"-{'-'*szer1}-\n"
        f"| POMOCNICZA TABELA WSTEPNYCH PATAMETROW POTRZEBNYCH DO OBLICZEN DLA POSCZEGOLNYCH MATERIALOW   |\n"
        f"-{'-'*szer1}-\n"
        f"|          {opcja} - PARAMETRY DOBRANE DLA NARZEDZI WYKONANE Z WEGLIKA SPIEKANEGO              |\n"
        f"*{'*' * szer1}*\n"
        f"| WL10(WYK) | W(Profitool) | TZM(WYK) | Mo(WYK) | STAL(HPC) | Ta (WYK) |   ALU   | T.SZTUCZNE   |\n"
        f"-{'-'*szer1}-\n"
        f"|    80     |     55-60    |    90    |   110   |     110   |    65    |   300   |    50-200    |Vc [m/min]\n"
        f"-{'-'*szer1}-\n"
        f"|   0,02    |      0.04    |   0.03   |   0.03  |    0.05   |   0.03   |  0.06   |   0.1-0.5    |fz [mm]\n"
        f"*{'*' * szer1}*\n"
    
    )

def get_tabela_wiercenie():

    Label(app, text="Podaj predkosc skrawania VC w m/min:").pack()
    vc_entry = Entry(app)
    vc_entry.pack()

    Label(app, text="Podaj srednice narzedzia Ø w mm:").pack()
    fi_entry = Entry(app)
    fi_entry.pack()

    Label(app, text="Podaj posuw na obrot f/U w mm:").pack()
    fu_entry = Entry(app)
    fu_entry.pack()

    def obliczenia():
        try:
            vc2 = vc_entry.get().replace(",", ".")
            fi2 = fi_entry.get().replace(",", ".")
            fu2 = fu_entry.get().replace(",", ".")

            if 0 < float(vc2) and 0 < float(fi2) and 0 < float(fu2):
                obroty = (float(vc2) * 1000) / (float(fi2) * 3.1416)
                wynik_obroty.config(text=f"Wyliczone obroty to: {int(obroty)} U/min")
                posuw = int(obroty) * float(fu2)
                wynik_posuw.config(text=f"Wyliczony posuw to: {int(posuw)} mm/min")
            else:
                wynik_obroty.config(text="Błędne dane, sprawdź wprowadzone wartości.")
                wynik_posuw.config(text="")
        except ValueError:
            wynik_obroty.config(text="Ups.. Podales dane w sposob niepoprawny")
            wynik_posuw.config(text="")
        except Exception as e:
            wynik_obroty.config(text=f"Błąd: {str(e)}")
            wynik_posuw.config(text="")

    Button(app, text="Oblicz", command=obliczenia).pack()

    wynik_obroty = Label(app, text="")
    wynik_obroty.pack()

    wynik_posuw = Label(app, text="")
    wynik_posuw.pack()

    return (
        f"{'-' * szer2}\n"
        f"|POMOCNICZA TABELA WSTEPNYCH PATAMETROW POTRZEBNYCH DO OBLICZEN DLA POSCZEGOLNYCH MATERIALOW|\n"
        f"{'-' * szer2}\n"
        f"|         WIERCENIE - PARAMETRY DOBRANE DLA NARZEDZI WYKONANE Z WEGLIKA SPIEKANEGO          |\n"
        f"{'*' * szer2}\n"
        f"|   WL10    |      W10     |   TZM    |    Mo   |  STAL   |    Ta    |   ALU   | T.SZTUCZNE |\n"
        f"{'-' * szer2}\n"
        f"|    30     |      30      |    90    |    90   |   45    |    40    |   150   |     180    |Vc [m/min]\n"
        f"{'-' * szer2}\n"
        f"|   0,02    |     0.04     |   0.03   |   0.03  |   0.1   |   0.03   |   0.2   |     0.15   |f/U [mm]\n"
        f"{'*' * szer2}\n"
    )
   
def get_tabela_planowanie():
    Label(app, text="Podaj predkosc skrawania VC w m/min:").pack()
    vc_entry = Entry(app)
    vc_entry.pack()

    Label(app, text="Podaj srednice narzedzia Ø w mm:").pack()
    fi_entry = Entry(app)
    fi_entry.pack()

    Label(app, text="Podaj liczbe zebow skrawajacych Z:").pack()
    z_entry = Entry(app)
    z_entry.pack()

    Label(app, text="Podaj posuw na zab fz:").pack()
    fz_entry = Entry(app)
    fz_entry.pack()

    def obliczenia():
        try:
            vc2 = vc_entry.get().replace(",", ".")
            fi2 = fi_entry.get().replace(",", ".")
            z = z_entry.get()
            fz2 = fz_entry.get().replace(",", ".")

            if 0 < float(vc2) and 0 < float(fi2) and 0 < int(z) and 0 < float(fz2):
                obroty = (float(vc2) * 1000) / (float(fi2) * 3.1416)
                wynik_obroty.config(text=f"Wyliczone obroty to: {int(obroty)} U/min")
                posuw = int(obroty) * float(fz2) * int(z)
                wynik_posuw.config(text=f"Wyliczony posuw to: {int(posuw)} mm/min")
            else:
                wynik_obroty.config(text="Błędne dane, sprawdź wprowadzone wartości.")
                wynik_posuw.config(text="")
        except ValueError:
            wynik_obroty.config(text="Ups.. Podales dane w sposob niepoprawny")
            wynik_posuw.config(text="")
        except Exception as e:
            wynik_obroty.config(text=f"Błąd: {str(e)}")
            wynik_posuw.config(text="")

    Button(app, text="Oblicz", command=obliczenia).pack()

    wynik_obroty = Label(app, text="")
    wynik_obroty.pack()

    wynik_posuw = Label(app, text="")
    wynik_posuw.pack()
    

    return (
    f"{'-' * szer1}\n"
    f"| POMOCNICZA TABELA WSTEPNYCH PATAMETROW POTRZEBNYCH DO OBLICZEN  DLA POSCZEGOLNYCH MATERIALOW |\n"
    f"{'-' * szer1}\n"
    f"|                   PARAMETRY DOBRANE DLA GLOWIC DO PLANOWANIA  C270 & A270                    |\n"
    f"{'*' * szer1}\n"
    f"|WL10(H210T)| W(H210T) |TZM(H210T)|Mo(H210T)|STAL(GM 43)|Ta(H210T)|ALU(H216T)|T.SZTUCZNE(H216T)|\n"
    f"{'-' * szer1}\n"
    f"|    120    |    70    |    160   |   160   |    150    |    90   |    500   |        250      |Vc [m/min]\n"
    f"{'-' * szer1}\n"
    f"|   0.08    |   0.11   |   0.12   |   0.12  |    0.1    |   0.06   |  0.15   |     0.1-0.5     |fz [mm]\n"
    f"{'=' * szer1}\n"
    f"|                     PARAMETRY DOBRANE DLA GLOWIC DO PLANOWANIA  CHSC                         |\n"
    f"{'-' * szer1}\n"
    f"|WL10(XDKT) | W(XDKT)  |TZM(XDKT) |Mo(XDKT) |STAL(GM 43)| Ta(XDKT) |ALU(XDKT)|T.SZTUCZNE(XDKT) |\n"
    f"{'-' * szer1}\n"
    f"|    140    |    85    |    180   |   180   |    150    |    95   |    500   |        260      |Vc [m/min]\n"
    f"{'-' * szer1}\n"
    f"|   0.08    |   0.08   |    0.1   |   0.1   |    0.08   |   0.05   |  0.12   |     0.1-0.5     |fz [mm]\n"
    f"{'*' * szer1}\n"
    )
    
def get_tabela_toczenie():
    Label(app, text="Podaj predkosc skrawania VC w m/min:").pack()
    vc_entry = Entry(app)
    vc_entry.pack()

    Label(app, text="Podaj srednice materialu Ø w mm:").pack()
    fi_entry = Entry(app)
    fi_entry.pack()

    Label(app, text="Podaj posuw na obrot f/U w mm:").pack()
    fu_entry = Entry(app)
    fu_entry.pack()

    def obliczenia():
        try:
            vc2 = vc_entry.get().replace(",", ".")
            fi2 = fi_entry.get().replace(",", ".")
            fu2 = fu_entry.get().replace(",", ".")

            if 0 < float(vc2) and 0 < float(fi2) and 0 < float(fu2):
                obroty = (float(vc2) * 1000) / (float(fi2) * 3.1416)
                wynik_obroty.config(text=f"Wyliczone obroty to: {int(obroty)} U/min")
                posuw = int(obroty) * float(fu2)
                wynik_posuw.config(text=f"Wyliczony posuw to: {int(posuw)} mm/min")
            else:
                wynik_obroty.config(text="Błędne dane, sprawdź wprowadzone wartości.")
                wynik_posuw.config(text="")
        except ValueError:
            wynik_obroty.config(text="Ups.. Podales dane w sposob niepoprawny")
            wynik_posuw.config(text="")
        except Exception as e:
            wynik_obroty.config(text=f"Błąd: {str(e)}")
            wynik_posuw.config(text="")

    Button(app, text="Oblicz", command=obliczenia).pack()

    wynik_obroty = Label(app, text="")
    wynik_obroty.pack()

    wynik_posuw = Label(app, text="")
    wynik_posuw.pack()


    return (
    f"{'-' * szer3}\n"
    f"| Potrzebne dane czyli predkosc skrawania VC i posuw na obrot f/U znajdziesz w tabelach parametrow  |\n"
    f"| producenta narzedzi a jako srednice  materialu Ø podaj nawieksza srednice ktora bedzie toczona... |\n"
    f"{'-' * szer3}\n"
        )

def powrot_do_menu():
    global opcje_frame, powrot_przycisk, przycisk_zapisu
    if 'powrot_przycisk' in globals():
        powrot_przycisk.destroy()

    opcje_frame = tk.Frame(app)
    opcje_frame.pack(pady=20)

    for opcja in opcje:
        przycisk = stworz_przycisk(opcja)
        przycisk.pack(side=tk.LEFT, padx=10)

    przycisk_zapisu = tk.Button(app, text="Zapisz do pliku", command=zapisz_do_pliku)
    przycisk_zapisu.pack()

opcje = ["FREZOWANIE", "WIERCENIE", "PLANOWANIE", "TOCZENIE"]

app = tk.Tk()
app.title("Kalkulator Parametrów Skrawania")


opis = (
    "Witaj w Kalkulatorze Parametrów Skrawania!\n\n"
    "Aby rozpocząć, wybierz jedną z opcji: FREZOWANIE, WIERCENIE, PLANOWANIE, TOCZENIE.\n"
    "Wprowadź odpowiednie dane, a program wygeneruje niezbędne parametry skrawania.\n"
    "Masz możliwość zapisu obliczonych wyników klikając ZAPISZ DO PLIKU.\n\n"
    "Autor: Kamil S."
)

text = Text(app, height=20, width=110)
text.pack(pady=20)
text.insert(tk.END, opis)

def stworz_przycisk(opcja):
    return tk.Button(opcje_frame, text=opcja, command=lambda: pokaz_tabele(opcja))

def zapisz_do_pliku():
    opcja = aktualna_operacja if 'aktualna_operacja' in globals() else "brak"
    wynik_obroty = ""
    wynik_posuw = ""
    for widget in app.winfo_children():
        if isinstance(widget, tk.Label) and "Wyliczone obroty" in widget.cget("text"):
            wynik_obroty = widget.cget("text")
        elif isinstance(widget, tk.Label) and "Wyliczony posuw" in widget.cget("text"):
            wynik_posuw = widget.cget("text")

    zawartosc = text.get("1.0", tk.END)
    plik = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Pliki tekstowe", "*.txt")])
    if plik:
        with open(plik, "w", encoding="utf-8") as f:
            f.write(zawartosc)
            f.write("\n\n")
            f.write(f"Operacja: {opcja}\n")
            f.write(f"{wynik_obroty}\n")
            f.write(f"{wynik_posuw}\n")


przycisk_zapisu = tk.Button(app, text="Zapisz do pliku", command=zapisz_do_pliku)

opcje_frame = tk.Frame(app)
opcje_frame.pack(pady=20)

for opcja in opcje:
    przycisk = stworz_przycisk(opcja)
    przycisk.pack(side=tk.LEFT, padx=10)

przycisk_zapisu.pack()

app.mainloop()