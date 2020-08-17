
# if we increase input size, how many more steps does this function need to take?


my_list = [1, 2, 3, 4, 5]

def print_list(arr):
    for thing in arr:
        print(thing)

print_list(my_list) # 5 steps

longer_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print_list(longer_list) # 10 steps

# double input size
# doubled the steps

# one-to-one ratio! Linear b/c the time this function takes grows at the same rate
# as the input increases
# O(n)

def nested_loop(arr):
    for thing in arr:
        for other_thing in arr:
            print(thing, other_thing)

# takes 25 steps

nested_loop(my_list) # takes 25

nested_loop(longer_list) # takes 100 steps

# doubled input size
# quadrupled the steps
# one-to-four ratio
# quadratic time complexity

# nested_loop(list_100_long) # 10000
#10x input
# 100x steps

# Count all the steps
# Then calculate Big O

def my_func(arr):
    a = 1
    b = 2
    c = a * b

    for x in range(1000):
        print(x)

    for thing in arr:
        print(thing)
    
    for thing in arr:
        x = 10
        y = 20
        z = x * y
        print(thing)

my_func(my_list)
my_func(longer_list)

# n == len(arr) == len(string) == size of input
## does this change if I change my input?

# 3 + 1000 + len(arr)
# 3 + 1000 + 10
# 3 + 1000 + len(arr)

# 3 + 1000 + (4 * len(arr))

# When figuring out O notation we just want to think aobut the big differences so 
# we only care about the length of the array - N is the length of the array
# O(n)

# (3 + 1000 + (4 * n)) ->
# (4n) ->
# (n) ->
# O(n) - linear time

# "on the order of:
# # n, n^2, n^3

def two_loops(arr):
    for x in range(10000000000):
        z = x * x
        print(z)

    for thing in arr:
        print(thing)

    for thing_again in arr:
        print(thing_again)

# Big O? 

# Line by line walkthough
# (big_num * 2) + len(arr) + len(arr)
# (big_num * 2) + (2 * len(arr))
# ignore the big constant
# O(2 * n) -> O(n)

