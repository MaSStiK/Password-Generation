import datetime
import os
from Password import Password

from rich import print, box
from rich.layout import Layout
from rich.console import Console, Group
from rich.panel import Panel
from rich.text import Text


def filename():
    replace_symbols = ["-", ":", ".", " "]  # Символы которые надо заменить
    name = str(datetime.datetime.now())  # Текущее время
    for i in replace_symbols:
        name = name.replace(i, "_")
    return name


password = Password()

password_length = input("Введите длину пароля: ")
pin_code = input("Введите PINCODE: ")

password.generate(password_length, pin_code)

console = Console()
Layout = Layout(name="info")

p_length = Text.from_markup(
    f"Длина пароля: {password.length}",
    style="bright_green", justify="center"
)

p_symbols_count = Text.from_markup(
    f"Доступно символов: {len(password.SYMBOLS)}",
    style="bright_green", justify="center"
)

p_variants = Text.from_markup(
    f"Возможных вариантов: {password.variants}",
    style="bright_green", justify="center"
)

p_password = Text.from_markup(
    f"Сгенерированый пароль: {password.password}",
    style="bright_green", justify="center"
)

p_check_summa = Text.from_markup(
    f"Ключ пароля: {password.check_summa}",
    style="bright_green", justify="center"
)

Layout.update(
    Panel(
        Group(
            p_length,
            p_symbols_count,
            p_variants,
            p_password,
            p_check_summa
        ),
        box=box.ROUNDED,
        title="Password Generator",
        subtitle=f"Version - {password.VERSION}",
        border_style="bright_blue"
    )
)

console.print(Layout)

if not os.path.exists("passwords"):  # Создаем папку если ее еще нету
    os.mkdir("passwords")
with(open(f"passwords/{filename()}.txt", "a")) as file:  # Сохраняем
    file.write(f"{password.password}\n{password.pin_code}\n{password.check_summa}")

input("Нажмите enter что бы закрыть приложение...")
