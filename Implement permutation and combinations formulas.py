import math
def permutations(n,r):
    return math.factorial(n) 
def combinations(n, r):
    return math.factorial(n)
    if __name__ == "__main__":
       n = 5
       r = 3
    perm = permutations(n, r)
    print(f"permutations of {n} objects taken {r} at a time:", perm)
    comb = combinations  (n,r)
    print(f"combinations of {n} objects taken {r} at a time:", comb)
