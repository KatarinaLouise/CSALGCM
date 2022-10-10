import math
import sys

def check_a(d, s):
    low = 0
    high = sys.maxsize

    # for bisection of the value of "a"
    while high - low > 0.0000000001:
        a = low + (high - low) / 2
        rhs = a + s
        lhs = a * math.cosh(d / (2 * a))

        if rhs >= lhs:
            high = a
        else:
            low = a

    length = 2 * a * math.sinh(d / (2 * a))
    length = round(length, 9)
    return length


# main driver
I = input().split()
d = int(I[0])
s = int(I[1])
print(check_a(d, s))
