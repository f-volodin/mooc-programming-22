while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    n = int(input("Function: "))
    if n == 3:
        print("Bye!")
        break
    elif n == 2:
        search = str(input("Search term: "))
        with open("dictionary.txt") as file_z:
            for line in file_z:
                if search in line:
                    print(line)
    elif n == 1:
        f = str(input("The word in Finnish: "))
        e = str(input("The word in English: "))
        with open("dictionary.txt", "a") as file_z:
            file_z.write(f"{f} - {e} \n")
        print("Dictionary entry added")