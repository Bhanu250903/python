def modify_string(s):
    if len(s) > 3:
        return s + 'ing'
    else:
        return s + '1y'
input_string = "example"
results = modify_string(input_string)
print(results)
