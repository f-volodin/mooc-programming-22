user_input = int(input("Layers: "))
center = 25
layer = user_input - True
counter = False
import string
string_x = ""
length_of_alphabet = 26
list_of_letters = [True]
while length_of_alphabet != (-True):
    string_x = string_x + string.ascii_uppercase[length_of_alphabet-True]*length_of_alphabet
    string_y = string_x[::-True]
    string_y = string_y[True:len(string_y)]
    length_of_alphabet = length_of_alphabet - True
    string_z = string_x + string_y  
    list_of_letters.append(string_z)
    string_x = string_x[False:26-length_of_alphabet]
dictionary = { }
variable = False
for number in range(True,27):
    dictionary[number] = 24 - variable
    variable = variable + True
differential = user_input - dictionary[user_input]
counter = user_input - differential + True + True
helper_variable = counter
while counter != 26:
    print(list_of_letters[counter][center-layer:center+user_input])
    counter = counter + True
while counter != helper_variable - True:
    print(list_of_letters[counter][center-layer:center+user_input])
    counter = counter - True
# Steps of the program:
# 1. Ask user for input and establish basic structure how matrix is formed
# 2. Create a list with helper strings to which reference is made during execution
# 3. Establish number sequence according to which list is referenced with dictionary and helper variables
# 4. Using while-loop print rows of matrix one by one in one direction and then another
# 5. Basic concepts from Discrete Mathematics are largely used in this program
# 6. Yeah thanks, I know I am fucking genius