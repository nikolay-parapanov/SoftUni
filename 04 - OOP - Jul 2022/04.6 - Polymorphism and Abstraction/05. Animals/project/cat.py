from project.animals.animal import Animal


class Cat(Animal):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def make_sound(self):
        return f"Meow meow!"