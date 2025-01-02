def totalMoney(n):
    lastMonday = 1
    totalSum = 0

    for day in range(n):
        if day >= 7 and day % 7 == 0:
            lastMonday += 1
            totalSum += lastMonday
        else:
            totalSum += lastMonday + (day % 7)

    return totalSum


print(totalMoney(9))
