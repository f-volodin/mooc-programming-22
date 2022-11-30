def print_persons(filename: str):
    import json
    with open(filename) as my_file:
        data = my_file.read()

    content = json.loads(data)

    for i in content:
        print(f"{content.name} {age} years ({hobbies})")