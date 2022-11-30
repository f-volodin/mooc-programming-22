def read_input(x, y, z):
    while True:
        try:
            x = int(input("Please type in a number: "))
            if x >= y and x <= z:
                #print(f"You typed in: {x}")
                return (x)
            else:
                print(f"You must type in an integer between {y} and {z}")
        except ValueError:
            print(f"You must type in an integer between {y} and {z}")
            pass