from project.food.dessert import Dessert

class Cake(Dessert):
    GRAMS = 250
    CALORIES = 1000
    PRICE = 5
    def __init__(self, name ):
        super().__init__(name, Cake.PRICE, Cake.CALORIES, Cake.GRAMS)

    @property
    def calories(self):
        return self.__calories
