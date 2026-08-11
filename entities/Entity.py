import random

#родительский класс для всех сущностей
class Entity:
    #определение параметров при создании объекта
    def __init__(self, name = None, type_obj = None, hp = None, defender = None, damage = None):
        self.name = name
        self.type_obj = type_obj
        self.hp = hp
        self.nominal_hp = hp
        self.defender = defender
        self.damage = damage
        self.counter = 0

        #словарь хранящий игровые статусы
        self.status = {
            "bleeding":False
        }

        #словарь хранящий статусы действий
        self.status_action = {
            "attack":False,
            "defender":None,
            "ult":None
        }


    #метод атаки
    def attack(self, entity, executor = None):
        """
        ОЧЕНЬ ВАЖНЫЙ МОМЕНТ В ДАННОМ МЕТОДЕ

        Я реализовал тут логику которая работает на основе срабатывания 2 раз.
        Первый раз: переводит атаку в подготовку действия и тут особо важно указать
        во втором параметре, при вызове метода, объект который исполняет атаку.
        Второй раз: активирует алгоритм атаки и делает это действие и указать нужно только 1 параметр объекта на которого
        нацелена атака

        Из-за логики данного метода, можно легко запутаться, по этому оставляю небольшие указатели
        """

        #Отлов ошибки неверного типа в случае если что-то обработается не так как надо
        try:
            #Первая проверка, которая проверяет статус атаки и исполнителя. При соответствии условию, атака перейдет в готовность
            if self.status_action["attack"] is False and executor == self:
                self.status_action["attack"] = True
                return
            #Вторая проверка, которая уже проверяет готовность атаки. Как было сказано - тут уже есть объект с None и его не меняем
            elif self.status_action["attack"] is True and executor is None:
                #Атака выполнится только при хп выше 0
                if entity.hp > 0:
                    #Если защиты нет, то происходит базовая атака
                    if entity.status_action["defender"] is None:
                        self.counter += 1
                        entity.hp -= self.damage
                        print(f"{self.name} наносит {self.damage} обычной атакой.")
                    #если есть защита, то атака игнорируется
                    elif entity.status_action["defender"] is True:
                        entity.status_action["defender"] = None
                        self.counter = 0
                        entity.hp -= 0
                        print(f"{entity.name} поставил блок. Атака не прошла.")
                    #но если защита не прошла, атака пройдет двойным уроном
                    elif entity.status_action["defender"] is False:
                        entity.status_action["defender"] = None
                        self.counter += 1
                        print(f"{entity.name} применил защиту, но она не прошла. {self.name} наносит атаку с повышенным уроном {self.damage * 2}.")
                        entity.hp -= self.damage * 2
                    #ну и после, статус атаки вернётся в ложь
                    self.status_action["attack"] = False
                elif entity.hp <= 0:
                    entity.hp = 0
        except TypeError:
            print(f"У {entity.name} отсутствует атрибут ХП")

    #метод зашиты (доработать логику)
    def defender_func(self, entity):
        #рандомный шанс
        choice = random.randint(1, 100)
        #проверка урона атакующего и шанса, если шанс будет больше 65% то выполняется защита, а если нет, то двойная атака
        if choice >= 65:
            self.status_action["defender"] = True
            print(f"{self.name} поставил защиту.")
        else:
            self.status_action["defender"] = False
            print(f"{self.name} не удалось поставить защиту.")

        if entity.status_action["defender"] is True:
            self.hp += 5

    #Каркас ультимейта для сущностей
    def ult(self, entity):
        print(f"У {self.name} отсутствует ульта")

    #Каркас метода алгоритма атаки сущностей
    def auto_action(self, enemy):
        pass

    #Метод вывода статистики сущности которая передаётся в качестве параметра
    @staticmethod
    def output_info(entity):
        print(f"""
                Информация {entity.name}
                -HP: {entity.hp}
                -Damage: {entity.damage}
                """)