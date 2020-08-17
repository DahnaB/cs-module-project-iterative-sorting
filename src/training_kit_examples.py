import math

def foo(n):
    sq_root = int(math.sqrt(n))
    for i in range(0, sq_root):
        print(i)

# 36 -> 6
# 100 -> 10
# 10000 -> 100
# O(log(n))

def bisect(n): # O(log(n))
    while n > 1:
        n = n/2
# 100
# 50
# 25
# 12.5
# 6.25
# 3
# 1.5
# 0.75~

# (2 ** 7)
# log is finding the seven in this example. So the number of steps?
# log of a number says please find for me this exponent 
## (2 ** ?) -> 16 exponenet of 4

def linear(n):
    while n > 1:
        n -= 1

def bar(x):
    sum = 0
    for i in range(0, 1463):
        i += 1
        for j in range(0, x):
            for k in range(x, x + 15):
                sum += 1

# 1463 * (1 + (n *(15 * 1)))
# 1463 * (1 + 15n)
# 1463 + (1463 * 15n)
# O(n)

def baz(array):
    print(array[1])
    midpoint = len(array) // 2
    for i in range(0, midpoint):
        print(array[i])
    for _ in range(1000):
        print("hi")

# 1 + 1 + n/2 + 1000
# 1002 + n/2
# O(n/2)
# O(n)

# n == 2n == n/2

def simple_recurse(n):
    if n <= 1:
        return n
    simple_recurse(n - 1)

simple_recurse(5)
simple_recurse(4)
simple_recurse(3)
simple_recurse(2)
simple_recurse(1)
simple_recurse(0)

# linear O(n)

def weird_recurse(num):
    if num <= 1:
        return num
    simple_recurse(num - 1)
    simple_recurse(num - 1)

# double last time: O(2n)?
# quadratic? O(n^2)
# exponential: 2^n

arr = [99, 98, 4, 0, 5, 2, 3, 1]

# Psuedocode for insertion sort
def insertion_sort(arr):
    ## start looping at the second element
    for index in range( 1, len(arr)):
    ## while current element is less than its left sibling
        current_element = arr[index]
        current_index = index
        while current_index > 0 and current_element < arr[current_index - 1]:
            arr[current_index] = arr[current_index - 1]
            current_index -= 1
        arr[current_index] = current_element

### copy left sibling to the right
### decrement index
## finally, put our current element down

# arr[i], arr[i - 1] = arr[i - 1], arr[i] ._. the python way? 

print(arr)
insertion_sort(arr)
print(arr)

# time complexity of insertion sort? 
# n * (1 + 1 + (n * 2) + 1)
# n * (3 + 2n)
# 3n + 2n^2
# O(n + n^2)
# O(n^2)
