from Password import Password
import time

password_length = input("Введите длину пароля: ")
pin_code = input("Введите PINCODE: ")
password = Password()
password.generate(password_length, pin_code)
print(password.password)
print(password.pin_code)
print(password.check_summa)

max_length = len(password.SYMBOLS)

brute = []
for _ in range(0, password.length):
    brute.append(0)


def return_array(array):
    i = 0
    if array[i] != max_length - 1:
        array[i] += 1
    else:
        array[i] = 0
        try:
            array[i + 1] += 1
        except:
            pass
    return array


for i in range(0, 10000):
    brute = return_array(brute)
    print(brute)

# for i in range(0, len(brute)):
#     element = i  # Какой по счету элемент в массиве
#     number = 0  # Изначально считаем от 0 + 1
#
#     while number != max_length - 1:
#         number += 1
#         brute[i] = number
#
#     for l in range(0, i):
#         brute[l] = 0
