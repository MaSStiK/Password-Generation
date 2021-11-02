import datetime
import os
from Password import Password

from rich import print, box
from rich.layout import Layout
from rich.console import Console, Group
from rich.panel import Panel
from rich.text import Text

Password_Generator = Password(input("Введите блину пароля: "))

# print(f"""Приложение версии: {Password_Generator.VERSION}
# Длина пароля: {Password_Generator.length}
# Доступно символов: {len(Password_Generator.SYMBOLS)}
# Возможных вариантов: {Password_Generator.variants}""")

password = Password_Generator.generate()
# print(f"Сгенерированый пароль: {password}")

replace_symbols = ["-", ":", ".", " "]  # Символы которые надо заменить
text_time = str(datetime.datetime.now())  # Текущее время
for i in replace_symbols:
    text_time = text_time.replace(i, "_")

if not os.path.exists("passwords"):  # Создаем папку если ее еще нету
    os.mkdir("passwords")
with(open(f"passwords/{text_time}.txt", "a")) as file:  # Сохраняем
    file.write(f"{password}\n")

console = Console()
Layout = Layout(name="info")

p_length = Text.from_markup(
    f"Длина пароля: {Password_Generator.length}",
    style="bright_green", justify="center"
)

p_symbols_count = Text.from_markup(
    f"Доступно символов: {len(Password_Generator.SYMBOLS)}",
    style="bright_green", justify="center"
)

p_variants = Text.from_markup(
    f"Возможных вариантов: {Password_Generator.variants}",
    style="bright_green", justify="center"
)

p_password = Text.from_markup(
    f"Сгенерированый пароль: {password}",
    style="bright_green", justify="center"
)

Layout.update(
    Panel(
        Group(
            p_length,
            p_symbols_count,
            p_variants,
            p_password
        ),
        box=box.ROUNDED,
        title="Password Generator",
        subtitle=f"Version - {Password_Generator.VERSION}",
        border_style="bright_blue"
    )
)

console.print(Layout)

input("Нажмите enter что бы закрыть приложение...")
