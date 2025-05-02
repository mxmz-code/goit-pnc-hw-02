import os
from collections import Counter

# Очищення екрану під час запуску
os.system('cls' if os.name == 'nt' else 'clear')

def знайти_відстані_повторень(текст, мін_довжина=3):
    результати = {}
    for довжина in range(мін_довжина, 6):
        tmp = {}
        for i in range(len(текст) - довжина):
            підрядок = текст[i:i + довжина]
            if підрядок in tmp:
                відстань = i - tmp[підрядок]
                результати.setdefault(підрядок, []).append(відстань)
            tmp[підрядок] = i
    return результати

def найпоширені_множники(відстані):
    from math import gcd
    множники = []
    for підрядок, відстані_список in відстані.items():
        if len(відстані_список) > 1:
            дільник = відстані_список[0]
            for відстань in відстані_список[1:]:
                дільник = gcd(дільник, відстань)
            if дільник > 1:
                множники.append(дільник)
    return Counter(множники).most_common()

def тест_фрідмана(текст):
    текст = ''.join([c for c in текст.upper() if c.isalpha()])
    N = len(текст)
    частоти = Counter(текст)
    чисельник = sum(f * (f - 1) for f in частоти.values())
    знаменник = N * (N - 1) if N > 1 else 1
    IC = чисельник / знаменник
    if IC == 0:
        return 0
    return round(0.0265 * N / ((0.065 - IC) + N * (IC - 0.0385)), 2)

if __name__ == "__main__":
    print("Аналіз шифру Віженера")
    шлях = input("Введіть шлях до файлу з шифротекстом [samples/text_input.txt]: ").strip()
    if not шлях:
        шлях = os.path.join("samples", "text_input.txt")

    if not os.path.exists(шлях):
        print("Файл не знайдено.")
    else:
        with open(шлях, "r", encoding="utf-8") as f:
            шифртекст = f.read()

        print("\n[Метод Касіскі]")
        відстані = знайти_відстані_повторень(шифртекст)
        касіскі = найпоширені_множники(відстані)
        for множник, частота in касіскі:
            print(f"Можливий дільник {множник}: {частота} раз(и)")

        print("\n[Тест Фрідмана]")
        довжина_ключа = тест_фрідмана(шифртекст)
        print(f"Оцінена довжина ключа: {довжина_ключа}")

    input("\nНатисніть Enter для повернення в меню...")
