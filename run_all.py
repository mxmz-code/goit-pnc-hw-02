import os

def меню():
    print("="*60)
    print("Лабораторна робота: Класичні методи шифрування")
    print("="*60)
    print("Оберіть один із варіантів:")
    print("1. Шифр Віженера")
    print("2. Подвійна перестановка")
    print("3. Табличний шифр")
    print("4. Аналіз шифру Віженера (Касіскі, Фрідман)")
    print("5. Комбіноване шифрування: Віженера + Табличний")
    print("0. Вихід")
    print("="*60)

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    меню()
    вибір = input("Ваш вибір: ")

    if вибір == "1":
        os.system("python vigenere_cipher/cipher.py")
    elif вибір == "2":
        os.system("python permutation_cipher/double_permutation.py")
    elif вибір == "3":
        os.system("python matrix_cipher/table_cipher.py")
    elif вибір == "4":
        os.system("python vigenere_cipher/analyzer.py")
    elif вибір == "5":
        os.system("python matrix_cipher/combo_encrypt.py")
    elif вибір == "0":
        print("До побачення!")
        break
    else:
        print("Невірний вибір. Натисніть Enter і спробуйте ще раз.")
        input()
