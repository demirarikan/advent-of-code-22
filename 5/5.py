with open("C:/Users/dmrar/Desktop/advent-of-code-22/5/5.txt", "r") as f:
    first_line = f.readline()
    result = [[] for _ in range(len(first_line) // 4)]
    first_line = first_line.strip("\n")
    crates = [first_line[i : i + 4] for i in range(0, len(first_line), 4)]
    for index, crate in enumerate(crates):
        if crate[0] != "[":
            continue
        else:
            result[index].insert(0, crate[1])
    cargo = True
    for lines in f:
        if lines == "\n":
            cargo = False
            # skip the "\n" line
            lines = f.readline()
        if cargo == True:
            lines = lines.strip("\n")
            crates = [lines[i : i + 4] for i in range(0, len(lines), 4)]
            for index, crate in enumerate(crates):
                if crate[0] != "[":
                    continue
                else:
                    result[index].insert(0, crate[1])

        else:
            # Operations start
            lines = lines.strip("\n")
            amount, source, dest = [int(lines.split(" ")[i]) for i in (1, 3, 5)]
            source -= 1
            dest -= 1
            temp = []
            for i in range(amount):
                temp.insert(0, result[source].pop())
            result[dest].extend(temp)
    for el in result:
        print(el[len(el) - 1], end="")
    f.close()
