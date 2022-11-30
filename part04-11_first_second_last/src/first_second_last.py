# Write your solution here

def first_word(sentence):
    return sentence[0:(sentence.find(" "))]
def second_word(sentence):
    sentence=sentence[(sentence.find(" "))+1:]
    if " " in sentence:
        return sentence[0:(sentence.find(" "))]
    else:
        return sentence
def last_word(sentence):
    while " " in sentence:
        sentence=sentence[(sentence.find(" ")+1):]
    return sentence

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))