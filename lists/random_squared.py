import random

random_numbers = random.sample(range(0,49), 20)
print(random_numbers)

random_squared = [num*num for num in random_numbers]
print(random_squared)