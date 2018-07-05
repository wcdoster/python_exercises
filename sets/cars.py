showroom = set()
showroom.update(["camry", "passat", "sentra", "accord"])
print(len(showroom))
showroom.add("sentra")
print(showroom)
showroom.update(["grand cherokee", "durango"])
print(showroom)
showroom.discard("camry")
print(showroom)

junkyard = {"corola", "jetta", "civic", "accord", "sentra", "maxima"}
print(junkyard.intersection(showroom))

showroom = showroom.union(junkyard)
print(showroom)

showroom.discard("jetta")
print(showroom)