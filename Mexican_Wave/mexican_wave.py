def wave(people: str)-> list:

    char_list = [x for x in people]
    wave_list = []

    for key, char in enumerate(char_list):
        if char == " ":
            char_list[key] = " "
            char_list[key - 1] = char_list[key - 1].lower()
        
        else:
            char_list[key] = char_list[key].upper()
            char_list[key - 1] = char_list[key - 1].lower()
            wave_list.append("".join(char_list))

    print(wave_list)
    return wave_list