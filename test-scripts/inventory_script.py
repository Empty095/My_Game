from entities.seve_items.inventory import Inventory
from Item.Items import Item

LIST_ITEMS = [Item("weapon", "weapon_0"), Item("armor", "armor_0"), Item("food", "food_0")]

x = Inventory(999)

x.add_item(LIST_ITEMS[0])
x.add_item(LIST_ITEMS[1])
x.add_item(LIST_ITEMS[2])
x.add_item(LIST_ITEMS[0])
x.add_item(LIST_ITEMS[1])
x.add_item(LIST_ITEMS[2])
x.add_item(LIST_ITEMS[0])
x.add_item(LIST_ITEMS[1])
x.add_item(LIST_ITEMS[2])
x.add_item(LIST_ITEMS[0])
x.add_item(LIST_ITEMS[1])
x.add_item(LIST_ITEMS[2])

x.info_inventory()