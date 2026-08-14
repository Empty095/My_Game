from random import choice


class Inventory:
    def __init__(self):
        self.items = {"weapon": None, "armor": None, "food": None}

    def add_item(self, item):
        if item.type_item is not None in self.items:
            print(f"Вы не можете иметь больше 1 предмета типа {item.type_item}.")
            choice = input(f"Вы можете заменить предмет в инвентаре {self.items[item.type_item]} на {item.name}.\n Вы подтверждаете действие? Да/Нет: ")
            if choice == "Да":
                self.items[item.type_item] = item
                print(f"Предмет {item.name} успешно заменен.")
            elif choice == "Нет":
                print(f"Вы оставили {self.items[item.type_item]}")
            else:
                print("Неверный ввод, введите только тот выбор который был приведен.")
        else:
            self.items[item.type_item] = item
            print(f"Предмет {item.name} успешно добавлен.")

    def del_item(self, item):
        if item.type_item is not None in self.items:
            choice = input(f"Вы точно хотите удалить предмет {self.items[item.type_item]}? Да/Нет: ")
            if choice == "Да":
                self.items[item.type_item] = None
                print(f"Предмет {item.name} успешно удалён из инвентаря.")
            elif choice == "Нет":
                print(f"Вы оставили {self.items[item.type_item]}")
            else:
                print("Неверный ввод, введите только тот выбор который был приведен.")


    def list_inventory(self):
        print(f"""ИНВЕНТАРЬ
        Оружие: {self.items["weapon"]}
        Броня: {self.items["armor"]}
        Вспомогательное средство: {self.items["food"]}""")