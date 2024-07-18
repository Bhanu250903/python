def print_even_odd_indices(string):
    even_index_chars = string[::2]
    odd_index_chars  = string[1::2]
    print("characters at even odd_index_charsices:", even_index_chars)
    print("characters at odd indices:", odd_index_chars)
input_string = "examples"
print_even_odd_indices(input_string)
