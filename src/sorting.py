arr = [4, 0, 5, 2, 3, 1]

#O(n) - worst case linear time
def find_num(arr, target_num):
    for x in arr:
        if x == target_num:
            return x
    return -1

find_num(arr, 1)

arr2 = [0, 1, 2, 3, 4, 5, 98, 99]

# binary search is log(n)