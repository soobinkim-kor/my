def greedy(n, m, k, numberList):
    numberList.sort()
    first = numberList[n - 1]
    second = numberList[n - 2]
    count = m / k
    r = m % k
    if (first == second):
        return first * m
    result = 0
    result = result + count * (first * k + second)
    result = result + r * first
    return result
