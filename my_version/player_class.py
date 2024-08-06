from constants import ADMIN_USERNAME


class Player:

    def __init__(self,) -> None:
        self.username = input(
            'Представьтесь, пожалуйста, как Вас зовут?\n').strip()
        if self.admin():
            print(
                '\nДобро пожаловать, создатель! '
                'Во время игры вам доступны команды "stat", "answer"'
            )
        else:
            print(f'\n{self.username}, добро пожаловать в игру!')

    def admin(self):
        if self.username == ADMIN_USERNAME:
            return True
        return False
