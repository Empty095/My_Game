import random

#родительский класс для всех сущностей
class Entity:
    #определение параметров при создании объекта
    def __init__(self, name = None, type_obj = None, hp = None, defender = 0, damage = None, inventory = None):
        self.name = name
        self.type_obj = type_obj
        self.hp = hp
        self.nominal_hp = hp
        self.defender = defender
        self.damage = damage
        self.counter = 0
        self.inventory = inventory

        #словарь хранящий игровые статусы
        self.status = {
            "bleeding":False
        }

        #словарь хранящий статусы действий
        self.status_action = {
            "attack":False,
            "defender action":None,
            "ult":None
        }

    def total_dmg(self):
        if self.inventory is not None and self.inventory.items_slots["weapon"] is not None:
            return self.damage + self.inventory.items_slots["weapon"].dmg
        else:
            return self.damage

    def take_damage(self, dmg_received, enemy):
        while True:
            if self.status_action["defender action"] is True:
                print(f"{self.name} заблокировал удар, который должен был нанести {dmg_received} урона.")
                enemy.counter = 0
                self.status_action["defender action"] = None
                return
            elif self.status_action["defender action"] is False:
                break

            choice = int(input(f"{enemy.name} готовится нанести удар, но вы можете заблокировать его. Блокировать? 1 - да, 2 - нет: "))
            if choice == 1:
                self.defender_func(enemy)
            elif choice == 2:
                break
            else:
                print("Неверный ввод. Ведите только представлений выбор.")

        if self.status_action["defender action"] is None:
            self.hp -= dmg_received
            print(f"{enemy.name} наносит {dmg_received} урона. У вас осталось {self.hp} здоровья.")
            enemy.counter += 1
        elif self.status_action["defender action"] is False:
            self.hp -= dmg_received * 2
            print(f"Так как вы не смогли применить защиту, {enemy.name} наносит {dmg_received * 2} урона. У вас осталось {self.hp} здоровья.")
            enemy.counter += 1

    #метод зашиты (доработать логику)
    def defender_func(self, entity):
        #рандомный шанс
        choice = random.randint(1, 100)
        #проверка урона атакующего и шанса, если шанс будет больше 65% то выполняется защита, а если нет, то двойная атака
        if choice >= 65:
            self.status_action["defender action"] = True
            print(f"{self.name} поставил защиту.")
        else:
            self.status_action["defender action"] = False
            print(f"{self.name} не удалось поставить защиту.")

        if entity.status_action["defender action"] is True:
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