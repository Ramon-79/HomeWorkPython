class Animal:
    def __init__(self, alias: str, weight: int, age: int):
        self.alias = alias
        self.weight = weight
        self.age = age

    def step(self):
        pass

    def voice(self):
        pass

    def __str__(self):
        return f"{self.alias} {self.weight} {self.age}"


class Cat(Animal):
    def __init__(self, alias: str, weight: int, age: int, race: str):
        super().__init__(alias, weight, age)
        self.race = race

    def step(self):
        return "Run"

    def voice(self):
        return "Mayu"

    def __str__(self):
        return f"{super().__str__()} {self.race}"


class Dog(Animal):
    def __init__(self, alias: str, weight: int, age: int, race: str):
        super().__init__(alias, weight, age)
        self.race = race

    def step(self):
        return "Run"

    def voice(self):
        return "Gov"

    def __str__(self):
        return f"{super().__str__()} {self.race}"


class Fish(Animal):
    def __init__(self, alias: str, weight: int, age: int, race: str):
        super().__init__(alias, weight, age)
        self.race = race

    def step(self):
        return "Swim"

    def voice(self):
        return ""

    def __str__(self):
        return f"{super().__str__()} {self.race}"


if __name__ == '__main__':
    dog = Dog("Rax", 40, 5, "lapdog")
    cat = Cat("Myrka", 1, 3, "trashbag")
    fish = Fish("Perch", 10, 5, "salty")

    print(dog)
    print(cat)
    print(fish)
