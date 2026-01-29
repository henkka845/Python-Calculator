import tkinter as tk

def laske():
    try:
        a = float(eka_luku.get())
        b = float(toka_luku.get())
        lasku = operaatio.get()

        if lasku == "+":
            tulos.set(a + b)
        elif lasku == "-":
            tulos.set(a - b)
        elif lasku == "*":
            tulos.set(a * b)
        elif lasku == "/":
            if b == 0:
                tulos.set("Virhe: nollalla ei voi jakaa")
            else:
                tulos.set(a / b)
    except ValueError:
        tulos.set("Syötä numerot")

# Ikkuna
ikkuna = tk.Tk()
ikkuna.title("Laskin")
ikkuna.geometry("500x500")
ikkuna.configure(bg="#C0B95D", padx=40, pady=40)
ikkuna.option_add("*Font", ("Arial", 13))
ikkuna.resizable(False, False)

# Muuttujat
eka_luku = tk.StringVar()
toka_luku = tk.StringVar()
operaatio = tk.StringVar(value="+")
tulos = tk.StringVar()

# Otsikko
tk.Label(
    ikkuna,
    text="Optimaalinen laskin",
    font=("Arial", 22, "bold"),
    bg="#C0B95D"
).pack(pady=(0, 25))

# Syötekentät
tk.Entry(
    ikkuna,
    textvariable=eka_luku,
    width=25,
    relief="solid",
    bd=2
).pack(pady=10)

tk.Entry(
    ikkuna,
    textvariable=toka_luku,
    width=25,
    relief="solid",
    bd=2
).pack(pady=10)

# Operaation valinta
valikko = tk.OptionMenu(ikkuna, operaatio, "+", "-", "*", "/")
valikko.config(width=6)
valikko.pack(pady=15)

# Laske-nappi
tk.Button(
    ikkuna,
    text="Laske",
    command=laske,
    font=("Arial", 14),
    height=2,
    width=12,
    relief="flat",
    bg="white",
    activebackground="#dddddd"
).pack(pady=20)

# Tulos
tk.Label(
    ikkuna,
    textvariable=tulos,
    bg="white",
    width=22,
    height=2,
    font=("Arial", 16, "bold")
).pack(pady=10)

ikkuna.mainloop()
