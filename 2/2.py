with open(
    "C:/Users/dmrar/Desktop/advent-of-code-22/2/2.txt", "r"
) as f:  # A:rock 1  B: paper 2  C: scissor 3      X: lose   Y: draw  Z: win
    sum = 0
    for line in f:
        plays = line.split()
        if plays[1] == "X":  # lose
            sum += 0
            if plays[0] == "A":
                sum += 3
            if plays[0] == "B":
                sum += 1
            if plays[0] == "C":
                sum += 2
        if plays[1] == "Y":  # draw
            sum += 3
            if plays[0] == "A":
                sum += 1
            if plays[0] == "B":
                sum += 2
            if plays[0] == "C":
                sum += 3
        if plays[1] == "Z":  # win
            sum += 6
            if plays[0] == "A":
                sum += 2
            if plays[0] == "B":
                sum += 3
            if plays[0] == "C":
                sum += 1
    print(sum)
    f.close()
