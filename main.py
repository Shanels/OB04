from abc import ABC, abstractmethod


class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


class Sword(Weapon):
    def attack(self):
        return "attacks with a sword"


class Bow(Weapon):
    def attack(self):
        return "shoots an arrow"


class Monster:
    def __init__(self, health):
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print("The monster is defeated!")
        else:
            print(f"The monster has {self.health} health remaining.")


class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} chooses a {type(weapon).__name__.lower()}.")

    def attack(self):
        if self.weapon:
            print(f"{self.name} {self.weapon.attack()}.")
        else:
            print(f"{self.name} has not chosen a weapon.")


fighter = Fighter("Fighter")
monster1 = Monster(10)
monster2 = Monster(5)

sword = Sword()
fighter.change_weapon(sword)
fighter.attack()
monster1.take_damage(10)

bow = Bow()
fighter.change_weapon(bow)
fighter.attack()
monster2.take_damage(5)
