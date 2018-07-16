from animal import Animal
from dog import Dog

class Pet():
    def __init__(self, name, critter_instatnce):
        self.name = name
        self.animal_type = critter_instatnce

    def assign_owner(self, owners_name):
        self.owner = owners_name

    def __str__(self):
        return f"{self.name} has {self.animal_type.leg_num} legs, and it says {self.animal_type.say_something()}"
