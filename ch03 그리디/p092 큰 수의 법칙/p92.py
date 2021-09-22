def greedy(n, m, k, numberList):
    numberList.sort()
    first = numberList[n - 1]
    second = numberList[n - 2]
    count = int(m / (k + 1))
    r = m % (k + 1)
    if (first == second):
        return first * m
    result = 0
    result = result + count * (first * k + second)
    result = result + r * first
    return result


numberList = [2, 4, 5, 4, 6]
greedy(5, 8, 3, numberList)
