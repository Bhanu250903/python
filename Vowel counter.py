def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
string = "Hello, world!"
print(f"Number of vowels in'{string}':", count_vowels(string))
