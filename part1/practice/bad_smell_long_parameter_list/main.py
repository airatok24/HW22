# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)

# Должен быть устранен длинный список параметров (количество параметров не больше трех)
# Должен быть устранен длинный метод - отдельно метод получения скорости, отдельно метод смещения по полю

class Unit:
    def __init__(self, x_coord, y_coord, movement_type):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.field = self.set_field()
        self.movement_type = movement_type
        self.speed = self._determine_speed()

    def set_field(self):
        # некая инициализация поля подразумевается
        return self.field

    def set_unit(self, x, y, unit):
        # функция set_unit ниже используется, но ее поведение не было определено.
        pass

    def _determine_speed(self):
        if self.movement_type == "default":
            self.speed = 1
        if self.movement_type == "fly":
            self.speed = self.speed * 1.2
        if self.movement_type == "crawl":
            self.speed = self.speed * 0.5
        else:
            raise ValueError('Что-то пошло не так.')
        return self.speed

    def move_in_field(self, direction):
        if direction == 'UP':
            self.field.set_unit(x=self.x_coord, y=self.y_coord + self.speed, unit=self)
        elif direction == 'DOWN':
            self.field.set_unit(x=self.x_coord, y=self.y_coord - self.speed, unit=self)
        elif direction == 'LEFT':
            self.field.set_unit(x=self.x_coord - self.speed, y=self.y_coord, unit=self)
        elif direction == 'RIGTH':
            self.field.set_unit(x=self.x_coord + self.speed, y=self.y_coord, unit=self)


...
