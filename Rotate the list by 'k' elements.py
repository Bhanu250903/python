def rotate_list(list, k):
    n = len(1st)
    k = k % n
    return 1st[-k:] + list[:-k]
    my_list = [1, 2, 3, 4, 5]
    k = 2
    rotated_list = rotate_list(my_list,k)
    print(rotated_list)
