from project.food.food import Food


class Dessert(Food):
    GRAMS = 250
    CALORIES = 1000
    PRICE = 5
    def __init__(self, name, price, grams, calories):
        super().__init__(name, price, grams)
        self.__calories = calories

    @property
    def calories(self):
        return self.__calories