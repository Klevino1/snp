# Камень, ножницы, бумага.
import sys
import random
import time


class Game():  # Класс писался в порядке игровой логики.
    """Основной класс игры."""

    def __init__(self):
        # Список игровых объектов.
        self.game_objects = ["Камень", "Ножницы", "Бумага"]
        self.player_chose = ""
        self.bot_chose = ""
        self.winstatus = 0

    def player_invitation(self):
        """
        Данная фунция просто выключает игру в случае отказа.
        Если написано yes, то просто пропускает дальше.
        НИЧЕГО НЕ ВОЗВРАЩАЕТ.
        """
        print("Вы хотите играть в эту игру? (yes/no)")
        while True:  # Цикл здесь нужен, что-бы
            self.player_anwser = input()
            if self.player_anwser.lower() == "yes":
                break
            elif self.player_anwser.lower() == "no":
                print("Выход.")
                sys.exit(0)
            else:
                print("Вы ввели не yes или no, пожалуйста, введите заного.")

    def print_game_objects(self):
        """Данная фунцкия просто печатает игровые объекты на экран."""
        print("Выбери одно из трёх.")
        # Данная переменная нужна цля цикла ниже, она будет цифрой выбора объекта.
        self.count = 1
        for self.game_object in self.game_objects:
            print("Нажмите " + str(self.count) +
                  " чтобы выбрать " + self.game_object + ".")
            # Данный оператор нужен, чтобы не так быстро шло перечесление объектов перед игроком.
            time.sleep(0.3)
            self.count += 1

    def player_choice(self):  # Этот метод - адский говнокод.
        """Функия, ответсвенная за выбор игрока."""
        while True:
            self.player_un = input()
            if self.player_un == "1":
                return "Камень"
            elif self.player_un == "2":
                return "Ножницы"
            elif self.player_un == "3":
                return "Бумага"
            else:
                print("вы ввели не 1, 2 либо 3. Введите повторно.")

    def bot_choice(self):
        """Функия выбора ботом"""
        return random.choice(self.game_objects)

    def whowin(self, pc, bc):  # возвращение 0 - НИЧЬЯ 1 - ПОБЕДА ИГРОКА 2-ПОБЕДА БОТА
        """Функция, проверяющая, кто победил."""
        self.pc = pc
        self.bc = bc
        if self.pc == self.bc:
            return 0  # НИЧЬЯ
        elif self.pc == "Камень" and self.bc == "Ножницы":
            return 1
        elif self.pc == "Камень" and self.bc == "Бумага":
            return 2
        elif self.pc == "Ножницы" and self.bc == "Камень":
            return 2
        elif self.pc == "Ножницы" and self.bc == "Бумага":
            return 1
        elif self.pc == "Бумага" and self.bc == "Камень":
            return 1
        elif self.pc == "Бумага" and self.bc == "Ножницы":
            return 2

    def wincheck(self):
        if self.winstatus == 0:
            print("Ничья, опа.")
        elif self.winstatus == 1:
            print("ВЫ ПОБЕДИЛИ. ИБО " + self.player_chose.upper() +
                  " ВЫИГРЫВАЕТ " + self.bot_chose.upper())
        elif self.winstatus == 2:
            print("ВЫ ПРОИГРАЛИ. ИБО " + self.player_chose.upper() +
                  " ПРОИГРЫВАЕТ " + self.bot_chose.upper())


def main():
    """Данная функция основная, она запускает игру."""
    game = Game()
    print("Добро пожаловать в Камень/Ножницы/Бумага.")
    game.player_invitation()
    while True:  # Основной цикл игры.
        game.print_game_objects()
        time.sleep(0.3)
        game.player_chose = game.player_choice()
        game.bot_chose = game.bot_choice()
        print("Бот выбрал " + game.bot_chose)
        time.sleep(0.5)
        game.winstatus = game.whowin(game.player_chose, game.bot_chose)
        game.wincheck()
        game.player_invitation()


if __name__ == "__main__":
    main()
