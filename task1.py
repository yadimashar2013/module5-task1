class House:  # Создали новый класс
    def __init__(self):
        self.numberOfFloors = 'Floor'


house = House()
house.numberOfFloors = 10  # Задали ему новый атрибут

for house.numberOfFloors in range(1, 11):  # В цикле проходим по атрибуту numberOfFloors
    print('Текущий этаж равен:', house.numberOfFloors)  # Распечатываем значение "Текущий этаж равен"
