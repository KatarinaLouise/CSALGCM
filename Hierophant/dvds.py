def solve(n, nums):
    count = 0
    prev = 0

    for i in nums:
        if i != prev + 1:
            count += 1
        else:
            prev = i
    return count


k = int(input())
for i in range(k):
    n = int(input())
    nums = list(map(int, input().strip().split(' ')))
    print(solve(n, nums))
