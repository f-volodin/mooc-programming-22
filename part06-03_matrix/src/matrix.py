def matrix_sum():
    e_list = []
    with open("matrix.txt") as file:
        for i in file:
            with open("other.txt", "a") as a_file:
                i = i.replace(",", "\n")
                a_file.write(i)

    with open("other.txt") as a_file:
        for i in a_file:
            i = i.replace("\n", "")
            e_list.append(int(i))
    #print(e_list)
    #e_list is list with all matrix numbers
    return sum(e_list)

def matrix_max():
    e_list = []
    with open("matrix.txt") as file:
        for i in file:
            with open("other.txt", "a") as a_file:
                i = i.replace(",", "\n")
                a_file.write(i)

    with open("other.txt") as a_file:
        for i in a_file:
            i = i.replace("\n", "")
            e_list.append(int(i))
    #print(e_list)
    #e_list is list with all matrix numbers
    return max(e_list)

print(matrix_sum())
print(matrix_max())