def solve(n, nums):
    max = -1000
    sum_total, count = 0, 0

    for i in nums:
        # for computing sum
        if i > 0:
            sum_total += i
            count += 1
        # for getting max
        if i > max:
            max = i
    if count == 0:
        sum_total = max
        count = 1
    return count, sum_total



n = int(input())
nums = [int(input()) for i in range(n)]
ans, total = solve(n, nums)

print("{} {}".format(ans, total))