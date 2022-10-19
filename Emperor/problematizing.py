def solve(n, t, problems):
    count = 0

    # sort the problems by ascending order
    problems.sort()

    for i in range(n):
        # don't consider the unsolvable problems
        if problems[i][0] != -1 and problems[i][0] <= t:
            count += 1  # increment count of answered problems
            t -= problems[i][0]  # subtract used time from total time

    if count == 0:
        return "This exam is impossible!"
    return count


def main():
    n, t = list(map(int, input().strip().split(' ')))
    problems = [tuple(map(int, input().strip().split(" "))) for i in range(n)]
    print(solve(n, t, problems))


if __name__ == "__main__":
    main()
