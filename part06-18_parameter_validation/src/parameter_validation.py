def new_person(name: str, age: int):
    if name == "":
        raise ValueError
    if " " not in name:
        raise ValueError
    if len(name) > 40:
        raise ValueError
    if age < 0:
        raise ValueError
    if age > 150:
        raise ValueError
    tupl = (name , age)
    return tupl