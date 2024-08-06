from game_parts import game
from player_class import Player


def guess_number() -> None:
    player = Player()
    # Счётчик игр в текущей сессии.
    total_games = 0
    while True:
        total_games += 1
        game(player, total_games)
        play_again = input('\nХотите сыграть ещё? (yes/no) ')
        if play_again.strip().lower() not in ('y', 'yes'):
            break


if __name__ == '__main__':
    print(
        'Вас приветствует игра "Угадай число"!\n'
        'Для выхода нажмите Ctrl+C'
    )
    guess_number()
