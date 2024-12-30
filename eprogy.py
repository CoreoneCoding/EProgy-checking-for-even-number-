"""Это программа, которая поможет понять тебе является ли число чётным и его частное (рзультат деления), особенно, если оно большое. /
This is a program which can help you to unserstand if number is even number especially it is huge."""

print("""Привет! Пожалуйста, выбери язык программы и введи его цифру. / Hello! Please, choose program's language and type its number).
Список языков и их цифр: русский (1), English (2).""")
choice_language = input("Введи номер языка / type language's number: ")


def program_in_russian():
    user_number = int(input("Введи число: "))
    if user_number % 2 == 0:
        print(f"""Это число является чётным.
Частоное этого числа - {round(user_number / 2)}.""")
    else:
        print("Это число не является чётным.")

def program_in_english():
    user_number = int(input("Type your number: "))
    if user_number % 2 == 0:
        print(f"""It's number is even number.
The quotient number is {round(user_number / 2)}.""")
    else:
        print("It's not even number.")

def check_language():
    if choice_language == "1":
        program_in_russian()
    if choice_language == "2":
        program_in_english()

try:
    check_language()
except ValueError:
    print("""Внимание! Ты ввёл или твоя строчка содержит буквы или другие символы! Пожалуйста, напиши ТОЛЬКО число!
Attention please! Your string has letters or another symbols! Please type ONLY number!""")
    check_language()


# The program's cycle
input()