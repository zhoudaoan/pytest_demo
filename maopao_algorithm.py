"""冒泡排序"""


def dubble_sort(numberlist):
    n = len(numberlist)
    for j in range(n - 1):
        for i in range(0, n - 1 - j):
            if numberlist[i] > numberlist[i + 1]:
                numberlist[i], numberlist[i + 1] = numberlist[i + 1], numberlist[i]


if __name__ == "__main__":
    li = [-4, 30, 6, 12, 90, 0, -34, 23, 22, 30]
    dubble_sort(li)
    print(li)
