import math
from math import sqrt

"""1. Predict Output,
	S1 = "Hello"
	S2 = "This is Python"
	print(len(S1), len(S2))
"""

# output is 5, 14


"""2. WAP to input a string and print its length."""


def test2():
    str1 = input("Enter a string")
    print(len(str1))


test2()

"""3. WAP to input 2 numbers and print their sum and difference."""


def test3():
    a = int(input("Enter first number"))
    b = int(input("Enter second number"))

    sum = a + b
    diff = a - b

    print("The sum of given 2 numbers is ", sum)
    print("The difference between given 2 numbers is ", diff)


test3()

"""4. Predict Output,
	s1 = 'ab'
	s2 = 'de'
	s3 = s1 + s2
	print(s3)
"""

# output = abde


"""5. Predict Output,
	s1 = 'ab' *4
	print(s1)
"""

# output = abababab


"""6. WAP to input a string s and a number n. Print the string n times on the screen, 
   each should appear in a separate line (do not use any kind of loops, use the multiplication operator).
"""


def test6():
    s = input("Enter the string")
    n = int(input("Enter the number"))
    print((s * n), sep="\n")
    print(*n * (s,), sep='\n')


test6()

"""7. Predict Output,
	s1 = 'Hello'
	s2 = 'This is India'
	s3 = s1 + '\n' + s2
	print(type(s3)
	print(len(s3)
"""

# output - (type(s3)) = str
# len(s3) = 19


"""8. Find the name of function to find the square root. (see all the options available in dir() of builtins"""


def test8():
    print(sqrt(4))
    print(math.sqrt(4))


test8()

"""9. WAP to input a number and print its square root ()."""


def test9():
    num = int(input("Enter the number to find square root"))

    print(math.sqrt(num))


test9()

"""10. WAP to input 4 numbers from user and print their average"""


def test10():
    numbers = []
    for n in range(4):
        num = int(input("Enter the numbers"))
        numbers.append(num)

    average = sum(numbers) / len(numbers)

    print("The average of give 4 numbers is ", average)


test10()

"""11. Use the help function to check what the abs function in python does."""

help(abs)


def test11():
    abs(-53.55)


test11()

# abs(x, /)
#     Return the absolute value of the argument.


"""12. What is the output of this code when run from python interpreter.
	print(__name__)
"""


def test12():
    print(__name__)


test12()

if __name__ == '__main__':
    test12()
