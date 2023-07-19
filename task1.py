from animal import Animal, Dog, Cat, Fish


class AnimalsCreator(Dog, Cat, Fish, Animal):

    @staticmethod
    def create_animal(alias: str, weight: int, age: int):
        return Animal(alias, weight, age)

    @staticmethod
    def create_cat(alias: str, weight: int, age: int, race: str):
        return Cat(alias, weight, age, race)

    @staticmethod
    def create_dog(alias: str, weight: int, age: int, race: str):
        return Dog(alias, weight, age, race)

    @staticmethod
    def create_fish(alias: str, weight: int, age: int, race: str):
        return Fish(alias, weight, age, race)


if __name__ == '__main__':
    dog = AnimalsCreator.create_dog('Jack', 12, 5, 'rassel')
    fish = AnimalsCreator.create_fish('Nemo', 1, 1, 'shark')
    anim = AnimalsCreator.create_animal('Homosapiens', 30, 4)
    print(dog)
    print(fish)
    print(anim)
