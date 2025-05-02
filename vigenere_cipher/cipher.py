import os
import tkinter as tk
from tkinter import messagebox

# Очищення екрану під час запуску
os.system('cls' if os.name == 'nt' else 'clear')

# Абетка латинська
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def розширити_ключ(текст: str, ключ: str) -> str:
    """
    Доповнює ключ до довжини тексту.
    """
    розширений = ключ
    while len(розширений) < len(текст):
        розширений += ключ
    return розширений[:len(текст)]

def зашифрувати(текст: str, ключ: str) -> str:
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

def розшифрувати(текст: str, ключ: str) -> str:
    результат = ""
    текст = текст.upper()
    ключ = розширити_ключ(текст, ключ.upper())
    for i in range(len(текст)):
        if текст[i] in alphabet:
            літера = alphabet[(alphabet.index(текст[i]) - alphabet.index(ключ[i])) % 26]
            результат += літера
        else:
            результат += текст[i]
    return результат

# Інтерфейс
def виконати_дію(дія):
    текст = поле_тексту.get("1.0", tk.END).strip()
    ключ = поле_ключа.get().strip()
    if not текст or not ключ:
        messagebox.showerror("Помилка", "Будь ласка, введіть текст та ключ.")
        return

    if дія == "шифрувати":
        результат = зашифрувати(текст, ключ)
    else:
        результат = розшифрувати(текст, ключ)

    поле_результату.delete("1.0", tk.END)
    поле_результату.insert(tk.END, результат)

вікно = tk.Tk()
вікно.title("Шифр Віженера")

tk.Label(вікно, text="Введіть текст:").pack()
поле_тексту = tk.Text(вікно, height=5, width=50)
поле_тексту.pack()

tk.Label(вікно, text="Ключ:").pack()
поле_ключа = tk.Entry(вікно)
поле_ключа.pack()

tk.Button(вікно, text="Зашифрувати", command=lambda: виконати_дію("шифрувати")).pack()
tk.Button(вікно, text="Розшифрувати", command=lambda: виконати_дію("розшифрувати")).pack()

tk.Label(вікно, text="Результат:").pack()
поле_результату = tk.Text(вікно, height=5, width=50)
поле_результату.pack()

вікно.mainloop()
