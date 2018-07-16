import unittest
import sys
sys.path.append('../')
from animals import Animal
from animals import Dog 

"""
In the test class' setUpClass() method, create an instance of Animal and Dog.
Animal object has the correct name property.
Set a species and verify that the object property of species has the correct value.
Invoking the walk() method set the correct speed on the both objects.
The animal object is an instance of Animal.
The dog object is an instance of Dog.
"""

class TestAnimal(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.bob = Dog("Bob")
        self.rob = Animal("Rob")

    def test_animal_creation(self):
        bob = Dog("Bob")
        self.assertIsInstance(bob, Animal)
        self.assertIsInstance(bob, Dog)

    def test_animal_can_set_legs(self):
        self.bob.set_legs(6)
        self.assertEqual(self.bob.legs, 6)

    def test_get_name(self):
        self.assertEqual(self.bob.get_name(), "Bob")

    def test_dog_walk(self):
        self.doggo = Dog("Doggo")
        self.doggo.walk()
        self.assertEqual(0, self.bob.speed)
        
        self.doggo.set_legs(4)
        self.doggo.walk()
        self.assertEqual(self.doggo.speed, .8)

    def test_animal_walk(self):
        self.animal = Animal()
        with self.assertRaises(ValueError):
            self.animal.walk()

        self.animal.set_legs(2)
        self.animal.walk()
        self.assertEqual(self.animal.speed, .2)


    def test_species(self):
        self.bob.set_species("dog")
        self.assertEqual(self.bob.get_species(), "dog")

    


if __name__ == '__main__':
    unittest.main()
