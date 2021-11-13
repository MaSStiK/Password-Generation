import random


class Password:
    SYMBOLS = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$*&")  # Список символов
    CONST_LENGTH = 4  # Длина пароля при неправильно введенном числе
    VERSION = "0.0.4"

    def __init__(self, password_length):
        try:
            password_length = int(password_length)
            if password_length <= self.CONST_LENGTH:
                self.length = self.CONST_LENGTH
            else:
                self.length = password_length
        except:
            self.length = self.CONST_LENGTH
        self.variants = len(self.SYMBOLS) ** self.length  # Кол-во вариантов паролей

    def generate(self):
        result = ""
        for _ in range(0, self.length):
            result += random.choice(self.SYMBOLS)
        return result

    def get_symbol(self, number):
        return self.SYMBOLS[number]

    def get_symbols(self, array):
        password = ""
        for i in array:
            password = password + str(self.get_symbol(i))
        return password
