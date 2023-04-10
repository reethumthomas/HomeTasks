"""1. Write a for loop to print numbers from 1 to 10. All numbers should be in separate lines."""
import random


def test1():
    for num in range(1, 11):
        print(num)


# test1()

"""2. Write a for loop to print numbers from 10 to 1. All numbers should be in separate lines."""


def test2():
    for n in range(10, 0, -1):
        print(n)


# test2()


"""3. Print Elements at Odd indexes from a list (Using for loop)
l = [10,11,20, 21,30, 31, 40, 41]"""


def test3():
    numbers = [10, 11, 20, 21, 30, 31, 40, 41]
    for index in range(len(numbers)):
        if index % 2 != 0:
            print(numbers[index])


# test3()

"""4. Create a list of 5 random numbers and then print the list, sum of all numbers and average. Use
a for loop."""


def test4():
    limit = 5
    numbers = []
    sum_all, average = 0, 0
    for i in range(limit):
        num = random.randint(1, 100)
        sum_all += num

        numbers.append(num)
    average += sum_all / limit

    print("The numbers of the list are ", numbers)
    print("The sum of all numbers in the list is ", sum_all)
    print("The average of all numbers in the list is ", average)


# test4()

"""5. WAP to input a string and print individual characters in the string using for loop."""


def test5():
    string = input("Enter the input string")
    for s in string:
        print(s)


# test5()

"""6. WAP to input a string and print the ASCII value of each character in the string."""


def test6():
    string = input("Enter the input string")
    for s in string:
        print(ord(s))


# test6()


"""7. WAP to input a string and store ASCII values of all characters in a tuple."""


def test7():
    string = input("Enter the input string")
    list_tup = []

    for s in string:
        print(ord(s))
        list_tup.append(ord(s))

    print(tuple(list_tup))


# test7()


"""8. Write a function that takes a list of numbers from user as argument and returns the sum of only
odd numbers (Use only for loop. No need to use if statement)."""


def test8():
    num = int(input("Enter the number of elements"))
    numbers = []
    # numbers = [5, 10, 11, 99, 50, 63]

    for n in range(num):
        numbers.append(int(input()))
    print(numbers)
    sum_odd = 0
    for i in numbers:
        if i % 2 != 0:
            sum_odd += i
    print(sum_odd)


# test8()

"""9. WAP to input a list of numbers and store in a tuple. Now input another number and print the
index of this number in the tuple."""


def test9():
    limit = int(input("Enter the range of numbers"))
    numbers_list = []
    for n in range(limit):
        numbers_list.append(int(input()))

    another_num = int(input("Enter another number"))
    numbers_list.append(another_num)

    numbers_tuple = tuple(numbers_list)
    print(numbers_tuple)
    # print(numbers_list.index(another_num))
    print(numbers_tuple.index(another_num))


# test9()


"""10. WAP to input 10 numbers repeatedly (using range based for loop) and store them in a list."""
"""11. Update the above program to also print the sum of numbers."""


def test10_11():
    numbers = []
    sum_all = 0
    for index in range(11):
        number = int(input())
        sum_all += number
        numbers.append(number)

    print("The list of 10 numbers are ", numbers)
    print("The sum of all numbers in the list is ", sum_all)


# test10_11()

"""12. WAP to input a number and print all numbers from 1 till that number"""


def test12():
    num = int(input("Enter a number"))

    for i in range(1, num + 1):
        print(i)


# test12()

""" 13. WAP to input a number and print its factorial. Factorial is denoted by n!, where n is the number
    whose factorial is to be found.
        Ex: if n = 4 output should be 24
        4! = 1x2x3x4 = 24
"""


def test13():
    number = int(input("Enter the number to find the factorial"))
    factorial = 1
    for num in range(1, number + 1):
        factorial = factorial * num

    print("The factorial of", number, "is", factorial)


test13()
