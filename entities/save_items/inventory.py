class Inventory:
    def __init__(self, weight):
        self.weight = weight
        self.bag = {1:None, 2:None, 3:None, 4:None, 5:None, 6:None, 7:None, 8:None, 9:None, 10:None}
        self.items_slots = {"weapon": None, "armor": None, "food": None}

    #Функция добавления предметов в инвентарь
    def add_item(self, item):
        for key, value in self.bag.items():
            if value is None:
                self.bag[key] = item
                return

        print("Весь инвентарь занят. Освободите место для добавления новых предметов.")

    #Метод удаления из инвентаря предмета
    def del_item(self, index):
        if index in self.bag:
            if self.bag[index] is not None:
                self.bag[index] = None
            else:
                print(f"Слот {index} пустой")
        else:
            print(f"Неверный ввод. Слот с индексом {index} не существует. Введите номер слота который представлен в списке для применения данного действия.")

    #метод использования вещей из инвентаря
    def using_item(self, index):
        if index in self.bag:
            if self.bag[index] is not None:
                x = self.bag[index]
                if self.items_slots[x.type_item] is not None:
                    hand = self.items_slots[x.type_item]
                    self.items_slots[x.type_item] = x
                    self.bag[index] = hand
                else:
                    self.items_slots[x.type_item] = x
                    self.bag[index] = None
            else:
                print(f"Слот {index} пустой.")
        else:
            print(f"Неверный ввод. Слот с индексом {index} не существует. Введите номер слота который представлен в списке для применения данного действия.")

    #Метод просмотра информации о предмете в инвентаре
    def info_item(self, index):
        if index in self.bag:
            if self.bag[index] is not None:
                print(f"""ИНФОРМАЦИЯ ПРЕДМЕТА {self.bag[index].name.upper()}
                Название: {self.bag[index].name}
                Тип снаряжения: {self.bag[index].type_item}
                Вес: {self.bag[index].weight}
                Урон: {self.bag[index].dmg}
                Защита: {self.bag[index].defender}
                Лечение: {self.bag[index].health}
                """)
            else:
                print(f"Слот {index} пустой.")
        else:
            print(f"Неверный ввод. Слот с индексом {index} не существует. Введите номер слота который представлен в списке для применения данного действия.")

    #Метод поиска вещей по категории
    def filter_inventory(self, category):
        for k in self.bag:
            if self.bag[k] is not None:
                if self.bag[k].type_item == category:
                    print(self.bag[k].name)
        else:
            print(f"По категории {category} ничего не найдено. Повторите попытку")


    #Метод вывода информации о инвентаре и меню действия с ним. БУДЕТ РЕФАКТОРИНГ
    def info_inventory(self):
        show_dict = lambda d: print(*(f"{k}: {v.name if v else 'пусто'}" for k, v in d.items()), sep="\n")

        while True:
            print("ИНВЕНТАРЬ")
            show_dict(self.bag)
            print(f"""
Оружие: {self.items_slots["weapon"].name if self.items_slots["weapon"] else 'пусто'}
Броня: {self.items_slots["armor"].name if self.items_slots["armor"] else 'пусто'}
Вспомогательное средство: {self.items_slots["food"].name if self.items_slots["food"] else 'пусто'}
                    ДЕЙСТВИЕ
            1. Удалить предмет из инвентаря
            2. Использовать выбранный предмет
            3. Статистика предмета
            4. Проверить доступные предметы по категории
            5. Выйти из инвентаря""")
            try:
                choice = int(input("Введите номер действия которое собираетесь выполнить: "))
                match choice:
                    case 1:
                        choice_item = int(input("Введите индекс объекта в инвентаре который хотите удалить: "))
                        self.del_item(choice_item)
                    case 2:
                        choice_item = int(input("Введите индекс объекта в инвентаре который хотите использовать: "))
                        self.using_item(choice_item)
                    case 3:
                        choice_item = int(input("Введите индекс объекта в инвентаре о котором хотите узнать информацию: "))
                        self.info_item(choice_item)
                    case 4:
                        choice_item = input("Введите название категории предметов которые вы ищете в инвентаре: ")
                        self.filter_inventory(choice_item)
                    case 5:
                        break
                    case _:
                        print("Неверный номер действия. Выберете только тот номер и действие, которые указаны в списке.")
            except ValueError:
                print("Ошибка ввода. Ввод принимает только числовое значение")
                continue