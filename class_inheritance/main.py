from dog import Dog
from pet import Pet

pupper = Dog("Border Collie")

doggo = Pet("Doggo", pupper)

doggo.assign_owner("Cole")

print(doggo)