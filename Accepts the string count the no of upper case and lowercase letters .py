def count_upper_lower(s):
    upper_count = sum (1 for char in s 
if char .isupper())
    lower_count = sum(1 for char in s 
if char .islower())
    return upper_count, lower_count
    input_string = "Hello world"
    upper, lower 
    count_upper_lower(input_string )
    print(f"Number of uppercase letters:{upper}")
    print(f"Number of lowercase letters:{lower}")
