def famous_births(people):
    sorted_people = sorted(people.values(), key=lambda p: p['date_of_birth'])
    for person in sorted_people:
        print(f"{person['name']}is a great scientist born in {person['date_of_birth']}.")
women_sciemtists = {
    "ada":{"name": "Ada Lovelace", "date_of_birth": "1815"},
    "cecilia": {"name": "Cecilia Panye", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}
famous_births(women_sciemtists)

