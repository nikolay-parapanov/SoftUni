from project.animals.animal import Bird


class Hen(Bird):
    ALLOWED_FOODS = ['Vegetable', 'Fruit', 'Meat', 'Seed']
    WEIGHT_INCREMENTAL = 0.35

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return 'Cluck'


class Owl(Bird):
    ALLOWED_FOODS = ['Meat']
    WEIGHT_INCREMENTAL = 0.25

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return 'Hoot Hoot'

