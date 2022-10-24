def solve(n, m, prices):
    prices.sort()
    prev = prices[0]
    count = 0

    for i in range(1, n):
        if prev + prices[i] <= m:
            count += 1
            prev = prices[i]
        else:
            break
    return count + 1


n, m = list(map(int, input().strip().split(' ')))
prices = list(map(int, input().strip().split(' ')))
print(solve(n, m, prices))

