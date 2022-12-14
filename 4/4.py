with open("C:/Users/dmrar/Desktop/advent-of-code-22/4/4.txt", "r") as f:
    result = 0
    for line in f:
        range1, range2 = line.split(",")
        range1_start, range1_end = map(int, range1.split("-"))
        range2_start, range2_end = map(int, range2.split("-"))
        if (range1_start <= range2_end and range1_end >= range2_end) or (
            range2_start <= range1_start and range2_end >= range1_end
        ):
            result += 1
        elif (range1_start <= range2_end and range1_end >= range2_end) or (
            range1_start >= range2_start and range1_end <= range2_end
        ):
            result += 1
        elif (range2_start <= range1_end and range2_end >= range1_end) or (
            range2_start >= range1_start and range2_end <= range1_end
        ):
            result += 1
        else:
            continue
    f.close()
    print(result)
