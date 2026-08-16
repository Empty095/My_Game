from random import choice


class Inventory:
    def __init__(self, weight):
        self.weight = weight
        self.bag = {1:None, 2:None, 3:None, 4:None, 5:None, 6:None, 7:None, 8:None, 9:None, 10:None}
        self.items_slots = {"weapon": None, "armor": None, "food": None}

    def add_item(self):
       pass

    def del_item(self):
        pass

    def using_item(self):
        pass

    def info_item(self):
        pass

    def filter_inventory(self):
        pass

    def action_inventory(self):
        print(f"""
        ДЕЙСТВИЕ
        1. Удалить предмет из инвентаря
        2. Использовать выбранный предмет
        3. Статистика предмета
        4. Проверить доступные предметы по категории
        """)
        try:
            choice = int(input("Введите номер действия которое собираетесь выполнить: "))
            match choice:
                case 1:
                    self.del_item()
                case 2:
                    self.using_item()
                case 3:
                    self.info_item()
                case 4:
                    self.filter_inventory()
                case _:
                    print("Неверный номер действия. Выберете только тот номер и действие, которые указаны в списке.")
        except ValueError:
            print("Ошибка ввода. Ввод принимает только числовое значение")


    def list_inventory(self):
        print(f"""ИНВЕНТАРЬ
        Оружие: {self.items_slots["weapon"]}
        Броня: {self.items_slots["armor"]}
        Вспомогательное средство: {self.items_slots["food"]}""")
        self.action_inventory()