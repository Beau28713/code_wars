def expanded_form(num):
    num_list = [int(x) for x in str(num)]
    num_list.reverse()
    power_list = []

    for pow in range(0, len(num_list)):
        if num_list[pow] >0:
            power_list.append(str(num_list[pow] * (10 ** pow)))

    power_list.reverse()
    answer = " + ".join(power_list)

    print(answer)
    return answer