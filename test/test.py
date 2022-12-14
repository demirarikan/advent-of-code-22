import math
import re


def is_square(n):
    if n > -1:
        return isinstance(math.sqrt(n), int)
    return False  # fix me


def move_zeros(lst):
    count = len(lst) - len(list(filter(lambda x: x != 0, lst)))
    zeros = [0] * count
    lst = list(filter(lambda x: x != 0, lst))
    lst.extend(zeros)
    return lst


def productFib(prod):
    res = 0
    index = 0
    while True:
        res = fib(index) * fib(index + 1)
        if res > prod:
            return [fib(index), fib(index + 1), False]
        if res == prod:
            return [fib(index), fib(index + 1), True]
        index += 1


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)


def digital_root(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    if sum // 10 == 0:
        return sum
    else:
        digital_root(sum)


def spin_words(sentence):
    words = sentence.split()
    for word in words:
        if len(word) > 5:
            word = word[::-1]
    return " ".join(words)


def domain_name(url):
    # regex = r"(http:\/\/|https:\/\/)*(www\.)*(\w+(-\w+)*)([.\w+]+)"
    result = re.search(r"(http:\/\/|https:\/\/)*(www\.)*(\w+(-\w+)*)([.\w+]+)", url)
    if result:
        print(result.group(3))


def test():
    target_string = "The price of PINEAPPLE ice cream is 20"

    # two groups enclosed in separate ( and ) bracket
    result = re.search(r"(\b[A-Z]+\b).+(\b\d+)", target_string)

    # Extract matching values of all groups
    print(result.groups())
    # Output ('PINEAPPLE', '20')

    # Extract match value of group 1
    print(result.group(1))
    # Output 'PINEAPPLE'

    # Extract match value of group 2
    print(result.group(2))


def pick_peaks(arr):
    result = {"pos": [], "peaks": []}
    temp_max = arr[0]
    temp_pos = 0
    for index, value in enumerate(arr):
        if value > temp_max:
            temp_max = value
            temp_pos = index
        elif value < temp_max:
            result["peaks"].append(temp_max)
            result["pos"].append(temp_pos)
            temp_max = value
            temp_pos = index
    #     for index, value in enumerate(arr[1:len(arr)-1], start=1):
    #         if value>arr[index-1] and value>arr[index+1]:
    #             result["pos"].append(index)
    #             result["peaks"].append(value)
    return result


if __name__ == "__main__":
    list1 = "a b c d 1"
    test = [[] for _ in range(len(list1) // 2)]
    for i in range(1):
        print(i)
