num = int(input("Enter a number"))
digits = len(str(num))
sqr = num ** 2
automorph = sqr%pow(10,digits)
if automorph == num:
    print(f"{num} is automorphic")
else:
    print(f"{num} is not automorphic")
