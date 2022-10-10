def binary_search(arr, H):
    low = 0
    high = len(arr) - 1
    count = len(arr)

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] >= H:
            count = mid
            high = mid - 1
        else:
            low = mid + 1
    return len(arr) - count


# main driver
n = input().split()
N = int(n[0])
H = int(n[1])
stalagmites = []
stalactites = []

# get stalagmite and stalactite sizes
for i in range(N):
    x = int(input())
    if i % 2:
        stalactites.append(x)
    else:
        stalagmites.append(x)

# sort the stalagmites and stalactites
stalagmites.sort()
stalactites.sort()

# iterate through the "levels"
mini = 100000  # maximum number of stalagmites or stalactites
count = 0
for i in range(1, H+1):
    # binary search for stalagmites
    mites = binary_search(stalagmites, i)
    # binary search for stalactites
    tites = binary_search(stalactites, (H - i + 1))
    total = mites + tites

    # compare with the current min and add to count if equal
    if total < mini:
        mini = total
        count = 0
    if total == mini:
        count += 1

print(mini, ' ', count)
