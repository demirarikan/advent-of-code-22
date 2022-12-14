with open("C:/Users/dmrar/Desktop/advent-of-code-22/6/6.txt", "r") as f:
    signal = f.readline()
    for i in range(13, len(signal)):
        # print(signal[i - 3 : i + 1])
        chars_set = set(signal[i - 13 : i + 1])
        # print(chars_set)
        if len(chars_set) == 14:
            print(i + 1)
            break
    f.close()
