def longest_series_of_neighbours(some_list: list):
    n = 1
    empty_list = [ ]
    for i in range(1, len(some_list)):
        if (some_list[i-1]-some_list[i] == 1) or (some_list[i-1]-some_list[i] == -1):
            n = n + 1
        else:
            n = 1
        empty_list.append(n)
    return max(empty_list)