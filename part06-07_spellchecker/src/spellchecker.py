struna = str(input("Write text: "))
list_x = struna.split(" ")

empty = [ ]
other = [ ]

with open("wordlist.txt") as file_x:
    for item in file_x:
        empty.append(item)

for element in empty:
    other.append(element.strip())
    #print(other)

for i in list_x:
    if i.lower() in other:
        pass
    else:
            #list_x.replace(i, f"*{i}*")
        list_x = list(map(lambda x: x.replace(i.lower(), f"*{i}*"), list_x))

strunna = " ".join(str(e) for e in list_x)
print(strunna)