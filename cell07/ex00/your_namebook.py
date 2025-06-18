def array_of_name(name_dict):
    result = []
    for first,last in name_dict.items():
        full_name = first.capitalize() + ' ' + last.capitalize()
        result.append(full_name)
    return result

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_name(persons))