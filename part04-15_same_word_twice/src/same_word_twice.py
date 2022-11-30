list=[]
word=""
while True:
    list.append(word)
    word = str(input("Word: "))
    if word in list:
        break
print(f"You typed in {len(list)-1} different words")