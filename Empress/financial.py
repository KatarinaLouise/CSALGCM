import sys
import operator

def check_day(arrP, arrC, r):
    low = 1
    high = sys.maxsize

    while low <= high:
        total = 0
        mid = low + (high - low) // 2  # mid is the number of days
        # print("low: ", low, " mid: ", mid, " high: ", high)
        dayP = [e * mid for e in arrP]   # multiply each profit by current number of days
        netP = list(map(operator.sub, dayP, arrC))  # subtract each cost from each profit

        # add all the net profits > 0
        for j in netP:
            if j > 0:
                total += j

        if low == high:
            return mid
        elif total >= r:
            high = mid
        else:
            low = mid + 1


# main driver
I = input().split()
n = int(I[0])
M = int(I[1])

dayProfits = []
invCost = []

# get each n investment's daily profit and cost
for i in range(n):
    y = [int(x) for x in input().split()]
    dayProfits.append(y[0])
    invCost.append(y[1])
result = check_day(dayProfits, invCost, M)
print(result)
