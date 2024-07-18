import math
def is_perfect_square(n):
    if n < 0:
        return False
    sqrt_n = int(math.sqrt(n))
    return sqrt_n * sqrt_n == n
number = 16
if is_perfect_square(number):
    print(f"{number} is a perfect square")
else:
    print(f"{number} is not a perfect square")
