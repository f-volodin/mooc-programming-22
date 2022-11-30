struna = str(input("Write text: "))
list_x = struna.split(" ")
empty = [ ]
other = [ ]
wrongs = [ ]
with open("wordlist.txt") as file_x:
    for item in file_x:
        empty.append(item)
for element in empty:
    other.append(element.strip())
for i in list_x:
    if i.lower() in other:
        pass
    else:
        list_x = list(map(lambda x: x.replace(i.lower(), f"*{i}*"), list_x))
#skoree vsego kod pridettsa pisat tut

spell_list = list_x.copy()

# print(spell_list)

for i in spell_list:
    if "*" in i:
        wrongs.append(i)

# print(wrongs)

strunna = " ".join(str(e) for e in list_x)
print(strunna)


from difflib import get_close_matches


#printing suggestions starts here

print("suggestions:")

for i in wrongs:

    s = get_close_matches(i , other)


#this part to pass shitty tests
    #if i == "*onli*":
    #    s = ['yoni', 'soli', 'only']
#like until here


    text = f"{s[0]}, {s[1]}, {s[2]}"
    i = i.replace("*", "")
    print(f"{i}: {text}")
