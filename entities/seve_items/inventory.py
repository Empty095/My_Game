class Inventory:
    def __init__(self, weight):
        self.weight = weight
        self.bag = {1:None, 2:None, 3:None, 4:None, 5:None, 6:None, 7:None, 8:None, 9:None, 10:None}
        self.items_slots = {"weapon": None, "armor": None, "food": None}

    #Функция добавления предметов в инвентарь (прошла тесты)
    def add_item(self, item):
        for key, value in self.bag.items():
            if value is None:
                self.bag[key] = item
                return

        print("Весь инвентарь занят. Освободите место для добавления новых предметов.")

    #Метод удаления из инвентаря предмета
    def del_item(self, index):
        if index in self.bag:
            self.bag[index] = None
        elif index not in self.bag:
            print(f"Данная ячейка отсутствует.")
        else:
            print("Ячейка пуста")

    #метод использования вещей из инвентаря (пройден тест)
    def using_item(self, index):
        if index in self.bag:
            x = self.bag[index]
            if self.items_slots[x.type_item] is not None:
                hand = self.items_slots[x.type_item]
                self.items_slots[x.type_item] = x
                self.bag[index] = hand
            else:
                self.items_slots[x.type_item] = x
                self.bag[index] = None

    #Метод просмотра информации о предмете в инвентаре (Прошел тест)
    def info_item(self, index):
        if index in self.bag and self.bag[index] is not None:
            print(f"""ИНФОРМАЦИЯ ПРЕДМЕТА {self.bag[index].name.upper()}
            Название: {self.bag[index].name}
            Тип снаряжения: {self.bag[index].type_item}
            Вес: {self.bag[index].weight}
            Урон: {self.bag[index].dmg}
            Защита: {self.bag[index].defender}
            Лечение: {self.bag[index].health}
            """)
        else:
            print("Ячейка пуста")

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

    #метод вывода информации о инвентаре (тест пройден)
    def list_inventory(self):
        show_dict = lambda d: print(*(f"{k}: {v.name if v else 'пусто'}" for k, v in d.items()), sep="\n")

        print(f"""ИНВЕНТАРЬ
        {show_dict(self.bag)}
        Оружие: {self.items_slots["weapon"]}
        Броня: {self.items_slots["armor"]}
        Вспомогательное средство: {self.items_slots["food"]}""")
        #self.action_inventory()