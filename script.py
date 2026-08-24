#Подключаем библиотеку для рандомной генерации чисел
import random

#Импортируем сущностей из модулей
from entities.Player import Player
from entities.Shadow import Shadow
from entities.Reaper import Reaper


#Основной класс игры
class Game:
    #При создании игры, сразу создается игрок и переменная для будущего объекта врага
    def __init__(self, Player = Player(), Enemy = None):
        self.Player = Player
        self.Enemy = Enemy

    #Метод для случайного подбора врага из ботов (в разработке)
    def random_enemies(self):
        roulette = random.randint(1, 100)
        if roulette >= 50 and roulette <= 100:
            self.Enemy = Shadow()
        elif roulette >= 15 and roulette < 50:
            self.Enemy = Reaper()
            return
        elif roulette >= 1 and roulette < 15:
            print("Coming soon")
            return

    #меню выбора действий
    def action_menu(self, entity, enemy):
        while True:
            #Отлов ошибки несоответствия типа введённых данных
            try:
                choice = int(input(f"""Меню выбора действий
                        Введите номер действия из списка ниже:
                        1. Атака - наносит {entity.damage} урона.
                        2. Защита - активирует защиту и блокирует атаку врага с вероятностью 35%.
                        3. Ульта - мощная атака по врагу.
                        4. Данные о враге - выводит информацию о враге.
                        5. Личные данные - выводит информацию о ваших характеристиках.
                        Поле ввода: """))
                match choice:
                    case 1:
                        #атака
                        enemy.take_damage(entity.total_dmg(), entity)
                        break
                    case 2:
                        #защита
                        entity.defender_func(entity)
                        break
                    case 3:
                        #ульта
                        entity.ult(enemy)
                        break
                    case 4:
                        #Данные о враге
                        entity.output_info(enemy)
                    case 5:
                        #Личные данные
                        entity.output_info(entity)
                    case _:
                        print("Выберете только то, что перечислено в списке.")
            except ValueError:
                print("Неверный ввод. Ввод должен быть только числовой и из списка.")

    #Метод хода боя
    def battle(self, player, enemy):
        print(f"Ход {player.name}")
        if player.type_obj == "player":
            self.action_menu(player, enemy)
        elif player.type_obj == "entity":
            player.auto_action(enemy)

    #Основной игровой метод, хранящий цикл боя и игры в целом
    def play(self):
        #цикл стартовой настройки игры (будет меняться)
        while True:
            #Отлов ошибки несоответствия типа введёных данных
            try:
                #Выбор врага
                choice = int(input("Вы хотите сыграть против игрока или против врагов со своим интеллектом? Введите 0 если с игроком, и 1 если с ботами: "))
                if choice == 0:
                    print("Вы выбрали игру против другого игрока")
                    self.Enemy = Player()
                    break
                elif choice == 1:
                    #Выбор противника: сущность под управлением бота
                    self.random_enemies()
                    print(f"Ваш противник {self.Enemy.name}. \nВы принимаете бой?")
                    var = input("Да/Нет: ")
                    if var == "Да":
                        break
                    #Тут нужно сделать логику отказа от боя. Детали в ТЗ
                    elif var == "Нет":
                        self.choice_varNo = random.randint(1, 100)
                        break
                else:
                    print("Выберете только те числа которые перечислены.")
            except ValueError:
                print("Неверный ввод: Ввод должен быть только числовой. Просьба ввести только числа которые указаны в инструкции.")

        #Цикл боя
        move = 1
        while self.Player.hp > 0 and self.Enemy.hp > 0:
            match move:
                case 1:
                    self.battle(self.Player, self.Enemy)
                    move = 2

                case 2:
                    self.battle(self.Enemy, self.Player)
                    move = 1

        #объявление победителя
        if self.Player.hp <= 0:
            print(f"{self.Player.name} повержен. Победитель {self.Enemy.name}.")
        elif self.Enemy.hp <= 0:
            print(f"{self.Enemy.name} повержен. Победитель {self.Player.name}.")


My_Game = Game()
My_Game.play()