with open("C:/Users/dmrar/Desktop/advent-of-code-22/1/1.txt", "r") as f:
    sum = 0
    max_sum = 0
    elf = 1
    for line in f:
        if line == "\n":
            max_sum = max(sum, max_sum)
            sum = 0
        else:
            sum = int(line.strip()) + sum
    print(max_sum)
