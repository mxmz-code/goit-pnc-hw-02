import os
import tkinter as tk
from tkinter import messagebox

os.system('cls' if os.name == 'nt' else 'clear')

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def розширити_ключ(текст: str, ключ: str) -> str:
    розширений = ключ
    while len(розширений) < len(текст):
        розширений += ключ
    return розширений[:len(текст)]

def шифр_віженера(текст: str, ключ: str) -> str:
    результат = ""
    текст = текст.upper()
    ключ = розширити_ключ(текст, ключ.upper())
    for i in range(len(текст)):
        if текст[i] in alphabet:
            літера = alphabet[(alphabet.index(текст[i]) + alphabet.index(ключ[i])) % 26]
            результат += літера
        else:
            результат += текст[i]
    return результат

def створити_матрицю(ключ: str) -> list:
    алфавіт = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    ключ = "".join(dict.fromkeys(ключ.upper().replace("J", "I")))
    результат = ключ
    for літера in алфавіт:
        if літера not in результат:
            результат += літера
    матриця = [list(результат[i:i+5]) for i in range(0, 25, 5)]
    return матриця

def знайти_координати(літера, матриця):
    for i in range(5):
        for j in range(5):
            if матриця[i][j] == літера:
                return i, j
    return None, None

def табличне_шифрування(текст: str, ключ: str) -> str:
    матриця = створити_матрицю(ключ)
    текст = текст.upper().replace("J", "I")
    результат = ""
    for літера in текст:
        if літера.isalpha():
            рядок, стовпець = знайти_координати(літера, матриця)
            новий_рядок = (рядок + 1) % 5
            результат += матриця[новий_рядок][стовпець]
        else:
            результат += літера
    return результат

def виконати_шифрування():
    текст = поле_тексту.get("1.0", tk.END).strip()
    ключ_в = поле_ключа1.get().strip()
    ключ_т = поле_ключа2.get().strip()

    if not текст or not ключ_в or not ключ_т:
        messagebox.showerror("Помилка", "Введіть текст і обидва ключі.")
        return

    проміжний = шифр_віженера(текст, ключ_в)
    результат = табличне_шифрування(проміжний, ключ_т)

    поле_результату.delete("1.0", tk.END)
    поле_результату.insert(tk.END, результат)

вікно = tk.Tk()
вікно.title("Комбіноване шифрування: Віженера + Табличний")

tk.Label(вікно, text="Введіть текст:").pack()
поле_тексту = tk.Text(вікно, height=5, width=50)
поле_тексту.pack()

tk.Label(вікно, text="Ключ для Віженера:").pack()
поле_ключа1 = tk.Entry(вікно)
поле_ключа1.insert(0, "CRYPTOGRAPHY")
поле_ключа1.pack()

tk.Label(вікно, text="Ключ для Табличного:").pack()
поле_ключа2 = tk.Entry(вікно)
поле_ключа2.insert(0, "CRYPTO")
поле_ключа2.pack()

tk.Button(вікно, text="Зашифрувати", command=виконати_шифрування).pack()

tk.Label(вікно, text="Результат:").pack()
поле_результату = tk.Text(вікно, height=5, width=50)
поле_результату.pack()

вікно.mainloop()
