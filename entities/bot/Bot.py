import random

from entities.Entity import Entity


class Bot:
    def __init__(self, entity):
        self.entity = entity
        self.nominal_hp = self.entity.nominal_hp
        self.diff_nominal_hp = None
        self.counter_move = 0

        if self.entity.nominal_hp - self.nominal_hp == 0:
            self.diff_nominal_hp = 0
        else:
            self.diff_nominal_hp = (self.entity.nominal_hp - self.nominal_hp) / 100

#метод атаки врагов под управлением бота
    def action(self, enemy):
        choice = random.randint(1, 100)
        if self.entity.hp >= self.nominal_hp - (self.nominal_hp * 0.6):
            if choice > 20:
                self.entity.attack(enemy, self.entity)
            else:
                self.entity.defender_func(enemy)
        elif self.entity.hp <= self.nominal_hp - (self.nominal_hp * 0.6):
            if choice > 60:
                self.entity.attack(enemy, self.entity)
            else:
                self.entity.defender_func(enemy)

    def medium_level(self, enemy):
        choice = random.randint(1, 100)
        if self.nominal_hp == enemy.nominal_hp and self.entity.hp < enemy.hp - (enemy.hp * 0.3):
            if enemy.damage < self.entity.hp * 0.2:
                print("1.0")
                if self.entity.status_action["ult"] is not None:
                    if self.entity.status_action["ult"] == False:
                        print("1.1")
                        self.action(enemy)
                    elif self.entity.status_action["ult"] == True:
                        print("1.2")
                        self.entity.ult(enemy)
        elif self.diff_nominal_hp >= 0.2:
            if enemy.damage > self.nominal_hp * 0.15:
                print("2.0")
                if self.entity.status_action["ult"] is not None:
                    if self.entity.status_action["ult"] == False:
                        print("2.1")
                        self.entity.attack(enemy, self.entity)
                    elif self.entity.status_action["ult"] == True:
                        print("2.2")
                        self.entity.ult(enemy)
            elif enemy.damage < self.nominal_hp * 0.15:
                if self.counter_move % 2 == 0:
                    print("2.3")
                    self.entity.defender_func(enemy)
                else:
                    print("2.4")
                    self.entity.attack(enemy, self.entity)
                self.counter_move += 1
        elif self.diff_nominal_hp < -0.25:
            if enemy.damage > self.nominal_hp * 0.15:
                print("3.0")
                if choice > 25:
                    print("3.1")
                    self.entity.defender_func(enemy)
                elif choice <= 25:
                    if self.entity.status_action["ult"] is not None:
                        print("3.2")
                        if self.entity.status_action["ult"] == False:
                            self.entity.attack(enemy, self.entity)
                        elif self.entity.status_action["ult"] == True:
                            self.entity.ult(enemy)
            elif enemy.damage < self.nominal_hp * 0.15:
                print("3.3")
                if choice > 45:
                    self.entity.defender_func(enemy)
                elif choice <= 45:
                    print("3.4")
                    if self.entity.status_action["ult"] is not None:
                        if self.entity.status_action["ult"] == False:
                            self.entity.attack(enemy, self.entity)
                        elif self.entity.status_action["ult"] == True:
                            self.entity.ult(enemy)
        else:
            print("3.5")
            self.action(enemy)