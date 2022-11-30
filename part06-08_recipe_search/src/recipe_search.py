def search_by_name(filename: str, word: str):
    my_list = [ ]
    recipes = [ ]
    with open(filename) as the_file:
        for line in the_file:
            line = line.replace("\n" , "")
            my_list.append(line)
    for item in my_list:
        if (word.lower() in item.lower()) and (item[0] in "QWERTYUIOPASDFGHJKLZXCVBNM"):
            
            recipes.append(item)
    return (recipes)

def search_by_time(filename: str, prep_time: int):
    my_list = []
    other_list = []
    with open(filename) as the_file:
        for line in the_file:
            line = line.replace("\n" , "")
            my_list.append(line)
    for i in my_list:
        if i != "":
            if i[0] in "1234567890":
                if int(i) <= prep_time:
                    index = my_list.index(i)
                    n = my_list[index-1]
                    struna = (f"{n}, preparation time {i} min")
                    other_list.append(struna)
    return other_list

def search_by_ingredient(filename: str, ingredient: str):
    my_list = []
    other_list = []
    with open(filename) as the_file:
        for line in the_file:
            line = line.replace("\n" , "")
            my_list.append(line)
    for item in my_list:
        if 
            other_list.append(item)




if __name__ == "__main__":
    found_recipes = search_by_ingredient("recipes1.txt", "eggs")

    for recipe in found_recipes:
        print(recipe)