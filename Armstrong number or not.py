def is_armstrong(number):
    digits = str(number)
    sum_of_powers = sum(int(digit) ** len(digits) for digit in digits)
    return sum_of_powers == number
input_number = 153
if is_armstrong(input_number):
   print(f"{input_number} is an armstrong number.")
else:
    print(f"{input_number} is not an armstrong number.")
