# Write your solution here

def palindromes(s):
    return s == s[::-1]
    
while True:
    s=str(input("Please type in a palindrome: "))
    a = palindromes(s)
    if a:
        print(f"{s} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")
            

# Note, that at this time the main program should not be written inside
if __name__ == "__main__":
    string=""
    palindromes(string)