class Transistor:
    def __init__(self, type_of_transistor: str, brand: str, max_current: float, max_voltage: float):
        self.type_of_transistor = type_of_transistor
        self.brand = brand
        self.max_current = max_current
        self.max_voltage = max_voltage

    def __str__(self):
        return f'{self.type_of_transistor}, {self.brand}, {self.max_current}, {self.max_voltage}'

