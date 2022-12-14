import numpy as np


def index_of_larger_element(value, arr):
    return next((x[0] + 1 for x in enumerate(arr) if x[1] >= value), len(arr))


with open("C:/Users/dmrar/Desktop/advent-of-code-22/8/8.txt", "r") as f:
    res = []
    # visible = 0
    mul_res_max = 0
    for line in f:
        chars = [int(x) for x in line if x != "\n"]
        res.append(chars)
    npres = np.array(res)
    print(npres)
    n_row, n_column = npres.shape
    for (x, y), value in np.ndenumerate(npres):
        if x == 0 or x == n_row - 1 or y == 0 or y == n_column - 1:
            continue
        else:
            up = npres[:, y][:x]
            down = npres[:, y][x + 1 :]
            left = npres[x, :][:y]
            right = npres[x, :][y + 1 :]
            up = np.flip(up)
            left = np.flip(left)

            directions = [up, down, left, right]

            mul_res = 1

            for direction in directions:
                # print(index_of_larger_element(value, direction))
                mul_res *= index_of_larger_element(value, direction)
            if mul_res > mul_res_max:
                mul_res_max = mul_res
            # neighbours = np.concatenate((up, down, left, right))
            # print(neighbours)
    #         if all(i < value for i in up):
    #             visible += 1
    #             continue
    #         if all(i < value for i in down):
    #             visible += 1
    #             continue
    #         if all(i < value for i in left):
    #             visible += 1
    #             continue
    #         if all(i < value for i in right):
    #             visible += 1
    #             continue
    # visible += n_row * 2 + (n_column - 2) * 2
    # print(visible)
    print(mul_res_max)
    f.close()


# if __name__ == "__main__":
#     print(index_of_larger_element(5, [1, 2, 3, 4]))
