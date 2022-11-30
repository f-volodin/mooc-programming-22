def add_student(dictionary, string):
    dictionary[string] = ""
    
def print_student(dictionary, string):
    if string in dictionary:
        print(f"{string}:")
        print(" no completed courses")
    else:
        print(f"{string}: no such person in the database")