def store_personal_data(person: tuple):
    struna = str(person[0])+";"+str(person[1])+";"+str(person[2])
    with open("people.csv","a") as my_file:
        my_file.write(struna +"\n")