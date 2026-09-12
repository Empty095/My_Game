"""
Данный класс является шаблоном объекта управляющим эффектами.
Оно может:
-добавлять эффекты
-удалять
-обновлять статусы следя за ними и счетчиком жизни

При создании данный объект принимает в качестве аргумента, сущность к которому он будет добавлен.
"""

class EffectSystem:
    def __init__(self, entity):
        self.entity = entity
        self.effects = []

#метод добавления эффекта
    def add_effect(self, effect):
        if effect not in self.effects:
            self.effects.append(effect)
        else:
            index = self.effects.index(effect)
            self.effects[index].effect_counter += effect.effect_counter

#метод применения эффекта
    def using(self):
        pass

#метод удаление эффекта вручную
    def del_effect(self, effect):
        if effect in self.effects:
            self.effects.remove(effect)
        else:
            print("EFFECT NOT FOUND")

#метод проверка и обновление состояния эффекта
    def update(self):
        self.effects = [effect for effect in self.effects if effect.effect_counter > 0]

        for effect in self.effects:
            effect.effect_counter -= 1