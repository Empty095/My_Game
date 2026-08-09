class Inventory:
    def __init__(self):
        self.items = {"Weapon": None, "Armor": None, "Consumable": None}

    def add_item(self, item):
        if item.status in self.items:
            print(f"Вы не можете иметь больше 1 предмета типа {item.status}.")
        else:
            self.items[item.status] = item
            print(f"Предмет {item.name} успешно добавлен.")

    def list_inventory(self):
        print(f"""ИНВЕНТАРЬ
        Оружие: {self.items["Weapon"]}
        Броня: {self.items["Armor"]}
        Вспомогательное средство: {self.items["Consumable"]}""")