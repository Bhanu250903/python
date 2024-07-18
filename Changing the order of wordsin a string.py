def reverse_words(s):
    words = s.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)
string = "Hello, World! How are you?"
reverse_words(string)
