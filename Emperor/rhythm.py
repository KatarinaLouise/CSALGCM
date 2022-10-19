import math

def solve(n, r, times):
    p = math.ceil(n * r / 100)  # to get number of notes within r
    margins = []  # holds the absolute margins of the non-miss notes

    for i in range(n):
        if times[i][1] != -1:
            margins.append(abs(times[i][0] - times[i][1]))

    if len(margins) < p:
        return "It's impossible!"
    margins.sort()
    return margins[p - 1]


def main():
    n, r = list(map(int, input().strip().split(" ")))
    times = [list(map(int, input().strip().split(" "))) for i in range(n)]

    print(solve(n, r, times))


if __name__ == "__main__":
    main()