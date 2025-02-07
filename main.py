import random


class Cat:
    def __init__(self, name="Абобус", age=100):
        self.name = name
        self.age = age
        self.energy = 100
        self.hungry = 0

    def meow(self):
        print(f"{self.name} говорит: Мяу!")
        self.energy -= 5

    def eat(self):
        print(f"{self.name} ест корм.")
        self.hungry = 0
        self.energy += 10

    def sleep(self):
        print(f"{self.name} спит... Zzz...")
        self.energy = 100

    def play(self):
        """Котик играет, но устаёт"""
        if self.energy > 20:
            print(f"{self.name} играет с мячиком!")
            self.energy -= 20
            self.hungry += 10
        else:
            print(f"{self.name} устал и не хочет играть.")

    def status(self):
        print(f"Имя: {self.name}, Возраст: {self.age}, Энергия: {self.energy}, Голод: {self.hungry}")


abobus = Cat()

abobus.status()
abobus.meow()
abobus.play()
abobus.eat()
abobus.sleep()
abobus.status()
