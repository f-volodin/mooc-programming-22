while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    n = int(input("Function: "))
    if n == 0:
        print ("Bye now!")
        break
    elif n == 1:
        struna = str(input("Diary entry: "))
        with open("diary.txt", "a") as file:
            file.write(struna + "\n")
        print("Diary saved")
    elif n == 2:
        print("Entries:")
        with open("diary.txt") as file:
            for line in file:
                print(line)
