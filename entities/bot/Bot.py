import random

from entities.Entity import Entity


class Bot:
    def __init__(self, entity):
        self.entity = entity
        self.nominal_hp = self.entity.nominal_hp
        self.diff_nominal_hp = None
        self.counter_move = 0

#метод активации ульты ИИ или просто атаки
    def using_ult(self, enemy):
        if self.entity.status_action["ult"] is not None:
            if self.entity.status_action["ult"] == False:
                self.action(enemy)
            elif self.entity.status_action["ult"] == True:
                self.entity.ult(enemy)

#метод атаки врагов под управлением бота
    def action(self, enemy):
        choice = random.randint(1, 100)
        if self.entity.hp >= self.nominal_hp - (self.nominal_hp * 0.6):
            if choice > 20:
                #self.entity.attack(enemy, self.entity)
                enemy.take_damage(self.entity.total_dmg(), enemy)
            else:
                self.entity.defender_func(enemy)
        elif self.entity.hp <= self.nominal_hp - (self.nominal_hp * 0.6):
            if choice > 60:
                #self.entity.attack(enemy, self.entity)
                enemy.take_damage(self.entity.total_dmg(), enemy)
            else:
                self.entity.defender_func(enemy)

#
    def medium_level(self, enemy):
        """
        Метод представляет собой средний уровень ИИ для не игровых сущностей.
        Он предназначен для сущностей, у которых есть возможность использовать ультимейт
        и он проводит средний анализ/сравнения некоторых данных игрока для более точного решения действия.
        """


        choice = random.randint(1, 100)
        #получение разницы номинального хп ИИ и Игрока
        self.diff_nominal_hp = self.entity.nominal_hp - enemy.nominal_hp
        if self.diff_nominal_hp != 0:
            self.diff_nominal_hp /= 100
        elif self.diff_nominal_hp == 0:
            self.diff_nominal_hp = 0

        #получение разницы хп ИИ и Игрока
        diff_hp = self.entity.hp - enemy.hp
        if diff_hp != 0:
            diff_hp /= 100
        elif diff_hp == 0:
            diff_hp = 0

        #Основной алгоритм проверки и принятия решения ИИ
        #1. Проверка номинального хп на равенство с ном. хп игрока и на разницу в 30% игрового хп
        if self.nominal_hp == enemy.nominal_hp and (diff_hp > 0.3 or diff_hp < 0.3):
            if enemy.damage < self.entity.hp * 0.2:
                print("1.0")
                self.using_ult(enemy)
            elif enemy.damage > self.entity.hp * 0.2:
                if choice > 35:
                    self.entity.defender_func(enemy)
                elif choice <= 35:
                    self.using_ult(enemy)
        #2. Проверка номинального хп на разницу +20% от ном. хп игрока
        elif self.diff_nominal_hp >= 0.2:
            if enemy.damage < self.nominal_hp * 0.15:
                print("2.0")
                self.using_ult(enemy)
            elif enemy.damage > self.nominal_hp * 0.15:
                if self.counter_move % 2 == 0:
                    print("2.3")
                    self.entity.defender_func(enemy)
                else:
                    print("2.4")
                    #self.entity.attack(enemy, self.entity)
                    enemy.take_damage(self.entity.total_dmg(), enemy)
                self.counter_move += 1
        #3. Проверка номинального хп на разницу -20% от ном. хп игрока (требуется доработка)
        elif self.diff_nominal_hp <= -0.2:
            if enemy.damage > self.nominal_hp * 0.15:
                print("3.0")
                if choice > 25:
                    print("3.1")
                    self.entity.defender_func(enemy)
                elif choice <= 25:
                    self.using_ult(enemy)
            elif enemy.damage <= self.nominal_hp * 0.15:
                print("3.3")
                if choice > 45:
                    self.entity.defender_func(enemy)
                elif choice <= 45:
                    print("3.4")
                    self.using_ult(enemy)
        #Если ничего не сработает, то происходит просто атака
        else:
            print("3.5")
            self.action(enemy)