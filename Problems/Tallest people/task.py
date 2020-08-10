def tallest_people(**people):
    for name, height in sorted(people.items()):
        if max(people.values()) == height:
            print(f'{name} : {height}')
