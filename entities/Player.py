from entities.Entity import Entity
from entities.seve_items.inventory import Inventory

class Player(Entity):
    def __init__(self, name = None, type_obj = "player", hp = 100, defender = 5, damage = 15, inventory = Inventory(40)):
        super(Player, self).__init__(name, type_obj, hp, defender, damage)
        self.inventory = inventory

#проверка на наличие никак игрока
        if name is None:
            self.name = input("Введите имя игрока:")
        elif name is not None:
            self.name = name

#ультимейт игрока (в будущем будет доработан)
    def ult(self, entity):
        if self.counter >= 4:
            entity.status["defender"] = False
            entity.hp -= self.damage * 4
            print(f"{self.name} выполнил пронзающий удар. Он быд настолько быстрым, что {entity.name} не смог заблокировать и получил {self.damage * 4} урона.")
            self.counter = 0
        else:
            print(f"Условия ультимейта не выполнены. Нанесите ещё {4 - self.counter} для возможности применения."
                  f"Так как условия для пронзающего удара не выполнены, удар был обычным.")
            self.attack(entity, self)