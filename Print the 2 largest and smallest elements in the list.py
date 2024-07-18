def find_len(list1):
    length = len(list1)
    list1.sort()
    print("largest element is:", list1[length-1])
    print("smallest element is:",list1[length-2])
    print("second largest element is:", list1[length-2])
    print("second smallest element is:", list1[1])
list1=[12, 45, 2, 41, 31, 10, 8,6,4]
largest = find_len(list1)
