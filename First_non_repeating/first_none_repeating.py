def first_none_repeating_letter(string):
    x = []
    y = string.casefold()

    for char in y:
        x.append(y.count(char))

    if 1 in x:
        print(string[x.index(1)])
        return (string[x.index(1)])
    else:
        return ""