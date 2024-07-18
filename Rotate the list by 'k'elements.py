def rotate_list(lst, k):
    n = len(1st)
    k = k % n 
    rotated_list = 1st[k:] + 1st[:k]
    return rotated_list
my_list = [1, 2, 3, 4, 5] 
k = 2
rotated_list = rotate_list(my_list, k)
print(rotated_list)
