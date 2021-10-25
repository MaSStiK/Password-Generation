import random
import datetime
import os

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

print(f'Приложение версии 0.0.3')

print(f"Доступно символов: {len(SYMBOLS)}\nВозможных вариантов: {len(SYMBOLS) ** PASSWORD_LENGTH}")

password = gen_password(SYMBOLS, PASSWORD_LENGTH)
print(f"Сгенерированый пароль: {password}")

replace_symbols = ["-", ":", ".", " "]
text_time = str(datetime.datetime.now())

if not os.path.exists("password"):
    os.mkdir("password")

for i in replace_symbols:
    text_time = text_time.replace(i, "_")

with(open(f"password/{text_time}.txt", "a")) as file:
    file.write(f"{password}\n")

input("Нажмите enter что бы закрыть приложение...")