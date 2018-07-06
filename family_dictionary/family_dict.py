my_family = {
    'father': {
        'name': "Rob",
        "age": 53
    },
    'mother': {
        'name': "Lisa",
        "age": 54
    },
    'brother': {
        'name': "Matthew",
        "age": 31
    }
}

family_list = {f'{description["name"]} is my {relation} and is {str(description["age"])} years old.' for relation,description in my_family.items()}

for person in family_list:
    print(person)