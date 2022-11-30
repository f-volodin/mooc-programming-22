def find_words(search_term: str):
    empty_list = []
    helper_list = []
    alef = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    with open("words.txt") as my_file:
        for unit in my_file:
            empty_list.append(unit)
            empty_list[-1] = empty_list[-1].strip()
            # emptyt list eto list so vsemi slovami iz fayla
    n = 0
    while n < 10:
#        for unit in empty_list:
        if "." in search_term:
            for item in alef:
                search_term = search_term.replace(search_term[search_term.find(".")], item, 1)
                if search_term not in helper_list:
                    helper_list.append(search_term)
        n = n + 1

    return helper_list

n = str(input("search term: "))
print(find_words(n))