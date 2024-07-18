def are_anagrams(str1,str2):
    str1_sorted = sorted(str1.lower())
    str2_sorted = sorted(str2.lower())
    return str1_sorted == str2_sorted
string1 = "listen"
string2  = "silent"
if are_anagrams(string1 , string2):
    print(f"{string1} and{string2} are anagrams.")
else:
    print("f{string1} and {string2} are not anagrans.")
