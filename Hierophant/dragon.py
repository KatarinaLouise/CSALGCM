def solve(n, m, head_heights, knight_heights):
    head_heights.sort()
    knight_heights.sort()
    total_coins = 0
    total_heads = 0
    i = 0  # index of knight
    j = 0  # index of dragon head

    while i < m and j < n:
        if knight_heights[i] >= head_heights[j]:
            total_coins += knight_heights[i]
            total_heads += 1
            i += 1
        j += 1
        if j == n - 1 and i < m - 1:
            if knight_heights[i] < head_heights[j]:
                i += 1
            j = total_heads

    if total_heads < n:
        return "Loowater is doomed!"
    return total_coins


count = 0
while count < 5:
    n, m = list(map(int, input().strip().split(' ')))
    head_heights = []
    knight_heights = []

    if n + m == 0:
        break
    for i in range(n):
        head_heights.append(int(input()))
    for j in range(m):
        knight_heights.append(int(input()))
    print(solve(n, m, head_heights, knight_heights))
    count += 1
