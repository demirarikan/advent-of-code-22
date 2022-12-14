from itertools import zip_longest


def grouper(iterable, n, *, incomplete="fill", fillvalue=None):
    "Collect data into non-overlapping fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, fillvalue='x') --> ABC DEF Gxx
    # grouper('ABCDEFG', 3, incomplete='strict') --> ABC DEF ValueError
    # grouper('ABCDEFG', 3, incomplete='ignore') --> ABC DEF
    args = [iter(iterable)] * n
    if incomplete == "fill":
        return zip_longest(*args, fillvalue=fillvalue)
    if incomplete == "strict":
        return zip(*args, strict=True)
    if incomplete == "ignore":
        return zip(*args)
    else:
        raise ValueError("Expected fill, strict, or ignore")


with open("C:/Users/dmrar/Desktop/advent-of-code-22/3/3.txt", "r") as f:
    result = 0
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for lines in grouper(f, 3):
        line1, line2, line3 = map(lambda x: set(x.strip()), lines)
        common_item = line1.intersection(line2.intersection(line3)).pop()
        result += alphabet.index(common_item) + 1
    print(result)
    f.close()
