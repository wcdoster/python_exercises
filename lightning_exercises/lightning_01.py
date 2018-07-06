def do_something(list, num, str="I have visited the city of "):
    new_list = list[:num]
    for item in new_list:
        print(str + item)
    
list = ["Nashville", "San Francisco", "New York", "Chicago", "Paris", "Dublin"]

do_something(list, 6)
do_something(list, 5, "I hate the city of ")