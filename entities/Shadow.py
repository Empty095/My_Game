from entities.Entity import Entity
from entities.bot.Bot import Bot

#класс создания тени. Он наследует свойства сущностей, но имеет уникальные методы
class Shadow(Entity):
    def __init__(self, name = "Shadow", type_obj = "entity", hp = 50, defender = 0, damage = 5):
        super(Shadow, self).__init__(name, type_obj, hp, defender, damage)
        self.bot = Bot(self)

#метод алгоритма атаки
    def auto_action(self, enemy):
        self.bot.action(enemy)