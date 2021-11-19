import random
import hashlib


class Password:
    SYMBOLS = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$*&")  # Список символов
    CONST_LENGTH = 3  # Длина пароля при неправильно введенном числе
    VERSION = "0.0.5"

    def __init__(self):
        self.password = ""
        self.pin_code = ""
        self.check_summa = ""
        self.length = 0
        self.variants = 0

    def generate(self, password_length=None, pin_code=None):
        try:
            password_length = int(password_length)
            if password_length <= self.CONST_LENGTH:
                self.length = self.CONST_LENGTH
            else:
                self.length = password_length
        except:
            self.length = self.CONST_LENGTH

        if pin_code is not None:
            self.pin_code = pin_code

        self.variants = len(self.SYMBOLS) ** self.length  # Кол-во вариантов паролей

        password = ""
        for _ in range(0, self.length):
            password += random.choice(self.SYMBOLS)

        self.password = password
        self.check_summa = hashlib.sha512(f"{self.password}{self.pin_code}".encode()).hexdigest()



    # def get_symbol(self, number):
    #     return self.SYMBOLS[number]
    #
    # def get_symbols(self, array):
    #     password = ""
    #     for i in array:
    #         password = password + str(self.get_symbol(i))
    #     return password
