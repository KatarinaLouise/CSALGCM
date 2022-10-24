import math

def solve(N, M, K, plots, circles, squares):
    plots.sort()
    count = 0

    # compute for the radius of the squares
    for i in range(K):
        squares[i] = math.sqrt(squares[i] ** 2 + squares[i] ** 2) / 2
    # combine the circle and squares radii in a list
    radii = circles + squares
    radii.sort()

    for house in radii:
        for i in range(N):
            if house < plots[i]:
                count += 1
                plots[i] = 0
                break
    return count


N, M, K = list(map(int, input().strip().split(' ')))
plots = list(map(int, input().strip().split(' ')))
circles = list(map(int, input().strip().split(' ')))
squares = list(map(int, input().strip().split(' ')))
print(solve(N, M, K, plots, circles, squares))
