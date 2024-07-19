test_str = "welcome"
all_freq = {}
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
print("count of all characters in welcome is :\n" + str(all_freq))        
