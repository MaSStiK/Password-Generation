from Password import Password
import time

Password_Generator = Password(input("Введите длину пароля: "))
password = Password_Generator.generate()
print(password)

password_array = [0 for i in range(0, len(Password_Generator.SYMBOLS))]


def next_array(array):
    array_count = [0 for i in range(0, len(array))]
    lenth = len(Password_Generator.SYMBOLS)

    if len(array) == 0:
        return None

    else:
        if array[0] == lenth - 1:
            array[0] = 0
            plus = True

            if len(array) > 1:
                for i in array_count:
                    if i > 0:
                        if plus:
                            if array[i] < lenth - 1:
                                array[i] = array[i] + 1
                                break

                            elif array[i] == lenth - 1:
                                array[i] = 0
                                if i == len(array) - 1:
                                    array.append(0)
                                    break
            else:
                array.append(0)
        elif array[0] < lenth - 1:
            array[0] = array[0] + 1
    return array


print(len(Password_Generator.SYMBOLS))
print(next_array(password_array))


start = time.time()
variants = 0
while True:
    variants += 1
    new_password_array = next_array(password_array)
    password_string = Password_Generator.get_symbols(password_array)
    print(password_string)

    #Добавить проверху хеша
