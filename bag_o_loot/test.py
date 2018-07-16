import unittest
from bag_o_loot import Bag_o_loot

"""
Requirements:
Items can be added to bag, and assigned to a child.
Items can be removed from bag, per child. Removing ball from the bag should not be allowed. A child's name must be specified.
Must be able to list all children who are getting a toy.
Must be able to list all toys for a given child's name.
Must be able to set the delivered property of a child, which defaults to false to true.
"""

class test_bag_o_loot(unittest.TestCase):

    # @classmethod
    # def set_up_class(self):
    #     """
    #     makes an instance of Bag_o_loot defined as bag
    #     """
    #     bag = Bag_o_loot()

    def test_add_item_assign_child(self):
        """
        Test to see if function add_toy_for_child adds a toy to the bag and assigns it to a specific child
        """
        bag = Bag_o_loot()
        bag.add_toy_for_child("boy", "toy")
        self.assertEqual(bag.loot_bag["boy"]["toys"][0], "toy")

    def test_remove_item_from_child(self):
        """
        Test to see if function remove_toy_from_child removes the specified toy from the specified child in loot_bag
        """
        bag = Bag_o_loot()
        bag.add_toy_for_child("boy", "toy")
        self.assertIn("toy", bag.loot_bag["boy"]["toys"])

        bag.remove_toy_from_child("boy", "toy")
        self.assertNotIn("toy", bag.loot_bag["boy"]["toys"])

    def test_list_children(self):
        """
        Test to see if function list_children will provide a list of all children getting toys
        """
        new_bag = Bag_o_loot()
        new_bag.add_toy_for_child("matthew", "toy")
        new_bag.add_toy_for_child("rob", "toy")
        new_bag.add_toy_for_child("cole", "toy")
        new_bag.add_toy_for_child("lisa", "toy")
        self.assertEqual(new_bag.list_children(), ("matthew", "rob", "cole", "lisa"))

    def test_list_toys_from_specific_child(self):
        """
        Test to see if function list_toys will provide a list of all the toys being give nto a specific child
        """
        this_bag = Bag_o_loot()
        this_bag.add_toy_for_child("me", "toy")
        this_bag.add_toy_for_child("me", "football")
        this_bag.add_toy_for_child("me", "drone")

        self.assertEqual(this_bag.list_toys("me"), ("toy", "football", "drone"))

    def test_deliver_toys(self):
        """
        Test to see if function deliver_toys will set the delivered property is changed to true
        """
        our_bag = Bag_o_loot()
        our_bag.add_toy_for_child("me", "baseball")
        our_bag.deliver_toys("me")

        self.assertEqual(our_bag.loot_bag["me"]["delivered"], True)

    

if __name__ == "__main__":
        unittest.main()

