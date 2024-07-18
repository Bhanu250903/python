def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count
input_str = "Hello,world!"
print("number of vowels:",count_vowels(input_str))
