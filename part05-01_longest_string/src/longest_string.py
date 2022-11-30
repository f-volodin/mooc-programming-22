def longest(strings: list):
    x = ""
    for i in strings:
        if len(i) > len(x):
            longest_string = i
            x = i
    return (longest_string)