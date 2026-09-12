class Effect:
    def __init__(self, effect_name, entity, effect_counter = None):
        self.effect_name = effect_name
        self.effect_counter = effect_counter
        self.entity = entity

        self.effect_on = False

    def healing(self, amount):
        self.entity.hp += amount

    def recovery_hp(self, amount):
        self.healing(amount)
        self.effect_counter -= 1

    def bonus_damage(self, amount):
        if self.effect_on == True:
            self.effect_counter -= 1
        else:
            self.effect_on = True
            self.entity.damage += amount

    def tick_damage(self, amount):
            self.entity.hp -= amount
            self.effect_counter -= 1