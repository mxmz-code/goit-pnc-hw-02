import os
import tkinter as tk
from tkinter import messagebox

# Очищення екрану
os.system('cls' if os.name == 'nt' else 'clear')

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

def табличне_шифрування(текст: str, ключ: str, дія: str) -> str:
    матриця = створити_матрицю(ключ)
    текст = текст.upper().replace("J", "I")
    результат = ""

    for літера in текст:
        if літера.isalpha():
            рядок, стовпець = знайти_координати(літера, матриця)
            if рядок is None or стовпець is None:
                результат += літера
                continue
            if дія == "шифрувати":
                новий_рядок = (рядок + 1) % 5
            else:
                новий_рядок = (рядок - 1) % 5
            результат += матриця[новий_рядок][стовпець]
        else:
            результат += літера

    return результат

def виконати_дію(дія):
    текст = поле_тексту.get("1.0", tk.END).strip()
    ключ = поле_ключа.get().strip()

    if not текст or not ключ:
        messagebox.showerror("Помилка", "Введіть текст і ключ.")
        return

    результат = табличне_шифрування(текст, ключ, дія)

    поле_результату.delete("1.0", tk.END)
    поле_результату.insert(tk.END, результат)

# Інтерфейс
вікно = tk.Tk()
вікно.title("Табличний шифр")

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
