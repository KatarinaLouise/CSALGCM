n = int(input())
p = list(map(int, input().strip().split(' ')))
p.sort(reverse=True)  # sort descending order
discount = 0

while len(p) >= 3:
    discount += p[2]  # take cheapest from current triple
    del p[:3]  # delete current triple
print(discount)
