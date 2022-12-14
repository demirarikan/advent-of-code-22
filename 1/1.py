with open("C:/Users/dmrar/Desktop/advent-of-code-22/1/1.txt", "r") as f:
    sum = 0
    max_sum_1 = 0
    max_sum_2 = 0
    max_sum_3 = 0
    sums_list = list()
    for line in f:
        if line == "\n":
            sums_list.append(sum)
            sum = 0
            # if sum >= max_sum_1:
            #     max_sum_3 = max_sum_2
            #     max_sum_2 = max_sum_1
            #     max_sum_1 = sum
            # elif sum >= max_sum_2:
            #     max_sum_3 = max_sum_2
            #     max_sum_2 = sum
            # elif sum >= max_sum_3:
            #     max_sum_3 = sum
            # sum = 0
        else:
            sum = int(line.strip()) + sum
    sums_list.append(sum)
    sums_list.sort(reverse=True)
    print(sums_list[0] + sums_list[1] + sums_list[2])
    print(sums_list[0], sums_list[1], sums_list[2])
    f.close()
