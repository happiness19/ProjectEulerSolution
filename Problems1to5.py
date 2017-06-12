def problem1 ():
    divThreeSum = 0
    divFiveSum = 0
    divFifteenSum = 0
    for i in range(1,1000):
        if (i % 3 == 0 & i % 5 == 0):
            divThreeSum += i
            divFiveSum += i
            divFifteenSum += i
        elif (i % 3 == 0):
            divThreeSum += i
        elif (i % 5 == 0):
            divFiveSum += i
    result = divThreeSum + divFiveSum - divFifteenSum
    return (result)
