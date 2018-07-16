class Bag_o_loot():
    
    loot_bag = {}
    
    def add_toy_for_child(self, child, toy):
        """
        function to assign toy to the value list dictionary with the key of child
        if child does not exist, then creates a new dictionary key of child
        """
        if child not in self.loot_bag.keys():
            self.loot_bag[child] = {"delivered":False, "toys":[toy]}
        else:
            self.loot_bag[child]["toys"].append(toy)

    def remove_toy_from_child(self, child, toy):
        """
        function to remove the toy included in the parameters from the child included in the parameters
        """
        i = self.loot_bag[child]["toys"].index(toy)
        del self.loot_bag[child]["toys"][i]

    def list_children(self):
        """
        function to provide a tuple of all of the children in loot_bag
        """
        return tuple(a for a in self.loot_bag.keys())

    def list_toys(self, child):
        """
        function to provide a tuple of all of the toys for a specific child
        """
        return tuple(a for a in self.loot_bag[child]["toys"])

    def deliver_toys(self, child):
        """
        function to set the delivered property to True
        """
        self.loot_bag[child]["delivered"] = True

        

# bag = Bag_o_loot()
# bag.add_toy_for_child("matthew", "toy")
# bag.add_toy_for_child("rob", "toy")
# bag.add_toy_for_child("cole", "toy")
# bag.add_toy_for_child("lisa", "toy")
# bag.add_toy_for_child("cole", "football")
# print(bag.loot_bag.keys())
# print(bag.list_children())
# print(bag.loot_bag)

# bag.remove_toy_from_child("cole", "football")
# print(bag.loot_bag)