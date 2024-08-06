from datetime import datetime as dt
from random import randint
from constants import UNKNOWN_COMMAND

start_time = dt.now()


def get_statistics(total_games: int, *args, **kwargs) -> None:
    game_time = dt.now() - start_time
    print(f'Общее время игры: {game_time}, текущая игра - №{total_games}')


def get_right_answer(number: int, *args, **kwargs) -> None:
    print(f'Правильный ответ: {number}')


def check_number(player, guess: int, number: int) -> bool:
    # Если число угадано...
    if guess == number:
        print(f'Отличная интуиция, {player.username}! Вы угадали число :)')
        # ...возвращаем True
        return True

    if guess < number:
        print('Ваше число меньше того, что загадано.')
    else:
        print('Ваше число больше того, что загадано.')
    return False


def game(player, total_games: int) -> None:
    # Получаем случайное число в диапазоне от 1 до 100.
    number = randint(1, 100)
    print(
        '\nУгадайте число от 1 до 100.\n'
        'Для выхода из текущей игры введите команду "stop"'
    )
    while True:
        # Получаем пользовательский ввод,
        # отрезаем лишние пробелы и переводим в нижний регистр.
        user_input = input('Введите число или команду: ').strip().lower()

        match user_input:
            case 'stop':
                break
            case 'stat':
                get_statistics(total_games) if player.admin(
                ) else print(UNKNOWN_COMMAND)
            case 'answer':
                get_right_answer(number) if player.admin(
                ) else print(UNKNOWN_COMMAND)
            case _:
                try:
                    guess = int(user_input)
                except ValueError:
                    print(UNKNOWN_COMMAND)
                    continue

                if check_number(player, guess, number):
                    break
