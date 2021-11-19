from Password import Password
import typer
import time
import os
#python encoder.py 2 0000 a9b0ea81af1de60a66cc8adc5fe85058ee784724df7f7327ef6b5cdd17dbadc30092a9a788c262be7bc004bae1d474cda2afbba9e375b59e89234634e13a03e2

app = typer.Typer()


@app.command()
def random(count_symbols: int, pin_code: str, check_summa: str):
    typer.echo(f'Количество доступных символов: {count_symbols}')
    typer.echo(f'Пин код: {pin_code}')
    typer.echo(f'Ключ пароля: {check_summa}')

    start_time = time.time()
    count_random = 0

    while True:
        count_random += 1
        password = Password()
        password.generate(int(count_symbols), pin_code)

        typer.echo(f'Проверяем пароль: {password.password}')

        if check_summa == password.check_summa:
            typer.echo(f'Совпадение: {password.password}')
            typer.echo(f'Количество пройденных вариантов: {count_random}')
            typer.echo(f'Время перебора составило: {time.time() - start_time}')
            break
        else:
            os.system('cls||clear')


if __name__ == "__main__":
    app()
