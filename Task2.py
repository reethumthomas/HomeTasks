"""1. Write lambdas to:
a. Square a number x2
b. Inverse a number 1/x
c. Negate a number"""
from functools import reduce


def test1():
    square = lambda x: x ** 2
    print(square(8))
    inverse = lambda a: 1 / a
    print(inverse(4))
    negate = lambda b: -b
    print(negate(6))


"""2. Use reduce function and an appropriate lambda to find the maximum number in a list. """


def test2():
    list1 = [-1, 3, 7, 99, 0]
    print(reduce(max, list1))
    print(reduce(lambda x, y: x if x > y else y, list1))


"""4. Predict the output of following code: """

"""f = lambda x, y: x if x > y else y
l = [10, 30, 50, 30, 10]
num = reduce(f, l)
print(num)"""

# output = 50

"""5. Find output of following: 
functs = [lambda x: x ** 0.5, lambda x: 1 / x]
l = [1, 4, 16, 64]
ans = []
for num in l:
    res = num
    for funct in functs:
        res = funct(res)
    ans.append(res)
print(ans)
"""

# output = [1, 0.5, 0.25, 0.125]

"""6. Use filter function to filter a list of numbers and strings such that the result contains only 
numbers. (Hint : Use isinstance method) """


def test6():
    old_list = [1, 8, 13, 10, 4, 5, 'reethu', 6, 7, 'abcd', 'thomas']
    new_list = []
    for x in old_list:
        if not isinstance(x, str):
            new_list.append(x)
    print(new_list)

    num_list = [x for x in old_list if isinstance(x, int)]
    print(num_list)


"""7. Assume a list containing heights ft and inches in the form of a list of string 
Example : l = [‘5ft10in’, ‘5ft’, ….] 
Write a function to convert the heights to meter. Use map function along with your function to 
convert everything to m"""

"""Map in Python is a function that works as an iterator to return a result after applying a function to every item 
of an iterable (tuple, lists, etc.)."""


def test7(height_str):
    feet, inches = 0, 0
    if 'ft' in height_str:
        feet = int(height_str.split('ft')[0])
    if 'in' in height_str:
        inches = int(height_str.split('in')[0].split('ft')[-1])
    total_inches = feet * 12 + inches
    return round(total_inches * 0.0254, 2)


heights = ['5ft10in', '5ft', '6ft2in', '4in']
heights_in_meters = list(map(test7, heights))

print(heights_in_meters)

if __name__ == '__main__':
    test7('5ft10in')
