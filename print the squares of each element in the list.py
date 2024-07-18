numbers = input("Enter numbers separated by spaces: ").split()
numbers = list(map(int,numbers))
squares = [num ** 2 for num in numbers]
print("squares of the numbers:",squares)
