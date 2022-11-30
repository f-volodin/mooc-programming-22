dictionary = { }
while True:
    input_1 = int(input("command (1 search, 2 add, 3 quit): "))
    if input_1 == 3:
        print("quitting...")
        break
    elif input_1 == 2:
        name = str(input("name: "))
        phone = str(input("number: "))
        dictionary.setdefault(name, [])
        dictionary[name].append(phone)
        print("ok!")
    elif input_1 == 1:
        input_2 = str(input("name: "))
        if input_2 not in dictionary:
            print("no number")
        else:
            for i in dictionary[input_2]:
                print(i)