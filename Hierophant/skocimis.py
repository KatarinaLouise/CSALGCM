a, b, c = list(map(int, input().strip().split(' ')))
right_gap = b - a - 1
left_gap = c - b - 1
print(max(right_gap, left_gap))
