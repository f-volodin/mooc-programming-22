alef = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n = int(input("number to say: "))

for i in range(n):
    
    # Loop to print pattern
    for j in range(n):
        ch = chr(65+i)
        print(ch, end=' ')
    print()