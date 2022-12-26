import math


def Log2(x):
    return (math.log10(x) /
            math.log10(2))


def isPowerOfTwo(n):
    return math.ceil(Log2(n)) == math.floor(Log2(n))


if isPowerOfTwo(33):
    print("Yes")
else:
    print("No")

if isPowerOfTwo(64):
    print("Yes")
else:
    print("No")
