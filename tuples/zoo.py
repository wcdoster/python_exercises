zoo = ("lion", "tiger", "bear", "elephant", "zebra")

print(zoo.index("bear"))

def find(animal):
    for value in zoo:
        if animal == value:
            print(f"{animal} is in the zoo")
            return
    print(f"{animal} is not at the zoo")

find("emu")
find("lion")

animals = []

for animal in zoo:
    animals.append(animal)

animals.extend(["leopard", "turtle", "snake"])

better_zoo = tuple(animals)

print(animals)
print(better_zoo)