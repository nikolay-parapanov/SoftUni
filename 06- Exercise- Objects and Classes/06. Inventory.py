class Inventory:
    items = []

    def __init__(self, capacity: int):
        self.__capacity = capacity

    def add_item(self, item: str):
        if len(Inventory.items) < self.__capacity :
            Inventory.items.append(item)
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        return f"Items: {', '.join(Inventory.items)}.\nCapacity left: {(self.__capacity - len(Inventory.items))}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
