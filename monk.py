# function that computes for the ascent height given a time
def compute_ascent_height(asc, time):
    curr_height = 0
    total_height = 0

    for monk in asc:
        # sum the height and time climbed before hitting given time
        if monk[1] < time:
            total_height += monk[0]
            time -= monk[1]  # remove the time already used to climb
        # otherwise, compute for the current height given time and current speed
        else:
            curr_height = monk[0] / monk[1] * time
            break
    return total_height + curr_height


# function that computes for the descent height given a time
def compute_descent_height(desc, time):
    curr_height = 0
    total_height = 0
    total_desc = 0

    for monk in desc:
        # sum the height and time climbed before hitting given time
        if monk[1] < time:
            total_height += monk[0]
            time -= monk[1]  # remove the time already used to climb
        # otherwise, compute for the current height given time and current speed
        else:
            curr_height = monk[0] / monk[1] * time
            break

    for h in desc:
        total_desc += h[0]
    return total_desc - (total_height + curr_height)


# function that looks for the time where asc height is equals to desc height
def check(ascend, descend):
    low = 0
    high = [sum(i) for i in zip(*ascend)]
    high = high[1]  # highest time is the ascent total time
    mid = 0

    while high - low > 0.0000000001:
        mid = low + (high - low) / 2
        asc = compute_ascent_height(ascend, mid)
        desc = compute_descent_height(descend, mid)

        if asc >= desc:
            high = mid
        else:
            low = mid
    return round(mid, 6)


# main driver
a, d = list(map(int, input().split()))
ascent = []
descent = []

for i in range(a):
    asc_h, asc_t = list(map(int, input().split()))
    ascent.append([asc_h, asc_t])

for i in range(d):
    desc_h, desc_t = list(map(int, input().split()))
    descent.append([desc_h, desc_t])

print(check(ascent, descent))
