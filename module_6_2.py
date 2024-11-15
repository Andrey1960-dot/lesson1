class Vehicle:
    __COLOR_VARIANTS = ['black', 'white', 'red', 'blue','green']
    def __init__(self, owner, model, engine_power, color ):
        self.owner = owner
        self._model = model
        self._engine_power = engine_power
        self._color = color
    def get_model(self):
        return f'Модель:{self._model}'

    def get_horsepower(self):
        return f'Мощность двигателя:{self._engine_power}'

    def get_color(self):
        return f'Цвет:{self._color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец:{self.owner}')

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self._color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
    __PASSENGER_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['black', 'white', 'red', 'blue', 'green']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в том числе вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем, что поменялось
vehicle1.print_info()

