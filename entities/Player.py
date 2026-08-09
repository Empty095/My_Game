from entities.Entity import Entity
from entities.seve_items.inventory import Inventory

class Player(Entity):
    def __init__(self, name = None, type_obj = "player", hp = 100, defender = 5, damage = 15, inventory = Inventory()):
        super(Player, self).__init__(name, type_obj, hp, defender, damage)
        self.inventory = inventory

#проверка на наличие никак игрока
        if name is None:
            self.name = input("Введите имя игрока:")
        elif name is not None:
            self.name = name

#ультимейт игрока (в будущем будет доработан)
    def ult(self, entity):
        if self.counter == 4:
            entity.status["defender"] = False
            entity.hp -= self.attack(entity) * 4
            self.counter = 0
