# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов

# в коде должна быть решена задача цепочки вызовов одним из способов
#
# - Передача нужных параметров объекту Person при инициализации
# - подъем требуемых финальных методов в класс Planet
# - Создание цепочки вызовов внутри самих классов, т.е. Planet.get_population должен вызывать Country.get_population
# --> City.get_population() до тех пор пока не будет получено конкретное значение


class Room:
    def get_name(self):
        return 42


class Street:
    def get_room(self) -> Room:
        return Room()


class City:
    def get_street(self) -> Street:
        return Street()

    def population(self):
        return 100500


class Country:
    def get_city(self) -> City:
        return City()


class Planet:
    def get_contry(self) -> Country:
        return Country()


class Person:
    def __init__(self, room_number, city_population):
        self.planet = Planet()
        self.room_number = int(room_number)
        self.city_population = int(city_population)

    def get_person_room(self):
        return self.room_number

    def get_city_population(self):
        return self.city_population


if __name__ == '__main__':
    person = Person(100, 200000)
    print(person.get_person_room())
    print(person.get_city_population())

