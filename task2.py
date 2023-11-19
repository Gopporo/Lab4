class Worker:

    name = str()
    surname = str()
    position = str()
    _income = dict()

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}

class  Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        total = 0
        for key, value in self._income.items():
            total += value
        return total

director = Position("Ivan", "Petrov", "Director", 2000, 1000)
print(director.name)
print(director.surname)
print(director.position)
print(director.get_full_name())
print(director.get_total_income())
