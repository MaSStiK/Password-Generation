import random

def gen_password(array, length):
    password = ""
    for _ in range(0, length):
        password += random.choice(array)
    return password

SYMBOLS = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$*&")
PASSWORD_LENGTH = int(input("Введите длину пароля: "))
CONST_LENGTH = 4

if PASSWORD_LENGTH <= 0:
    PASSWORD_LENGTH = CONST_LENGTH

print(f'Приложение версии 0.0.1')

print(f"Доступно символов: {len(SYMBOLS)}\nВозможных вариантов: {len(SYMBOLS) ** PASSWORD_LENGTH}")

password = gen_password(SYMBOLS, PASSWORD_LENGTH)
print(f"Сгенерированый пароль: {password}")

with(open("password.txt", "a")) as file:
    file.write(f"{password}\n")