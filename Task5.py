"""1. WAF: bmi() that takes the weight in kg and height in cm of a person, calculates and returns the BMI.
Write code that calls this function after taking height and weight as inputs and then prints
underweight, normal, overweight or obese depending on the value of BMI.
Refer this link for the ranges:
https://en.wikipedia.org/wiki/Body_mass_index
"""


def test1():
    weight_height = "55.05kg160.5cm"
    weight, height, height_in_m = 0, 0, 0
    if 'kg' in weight_height:
        weight = weight_height.split('kg')[0]
    if 'cm' in weight_height:
        height = weight_height.split('cm')[0].split('kg')[1]
        height_in_m = float(height) / 100
    BMI = round(float(weight) / (height_in_m ** 2), 1)
    print(BMI)

    if BMI < 18.5:
        print("Underweight")
    elif 18.5 <= BMI <= 22.9:
        print("Normal")
    elif BMI >= 23.0:
        print("Overweight")


# test1()

"""2. Take input of age of 3 people by user and determine oldest and youngest among them."""


def test2():
    age_person1 = int(input())
    age_person2 = int(input())
    age_person3 = int(input())

    if age_person1 > age_person2 and age_person1 > age_person3:
        print("Person 1 with age ", age_person1, " is the oldest")
    elif age_person2 > age_person1 and age_person2 > age_person3:
        print("Person 2 with age ", age_person2, " is the oldest")
    else:
        print("Person 3 with age ", age_person3, " is the oldest")

    youngest = age_person1
    oldest = age_person2
    if age_person2 <= youngest:
        youngest = age_person2
    elif age_person3 <= youngest:
        youngest = age_person3
    if age_person1 >= oldest:
        oldest = age_person1
    elif age_person3 >= oldest:
        oldest = age_person3
    print(youngest)
    print(oldest)


# test2()

""" 3. WAP to input a number and check if number is divisible by both 5 and 7. """


def test3():
    num = int(input("Enter a number"))

    if num % 5 == 0 and num % 7 == 0:
        print("Given number ", num, " is divisible by 5 and 7")
    else:
        print("Given number ", num, " is NOT divisible by 5 and 7")


# test3()

"""4. WAF: is_alphabet() that takes a string argument and returns True or False. True if all characters
in the string are alphabets otherwise False. (write code using for loop and if. Do not use built in
functions)
"""


def test4(string):
    flag = False
    for s in string:
        if s.isdigit():
            flag = False
    return flag


# print(test4(string='Returnee'))


"""5. WAF: is_leap_year() that takes a year as input and retuns True if year is leap year, otherwise
false.
"""


def test5():
    year = int(input("Enter the Year"))

    if year % 4 == 0 or year % 400 == 0:
        print("The given year ", year, " is a leap year")
    else:
        print("The given year ", year, " is NOT a leap year")


# test5()


"""8. WAF: uncommon_words() that takes two sentences (strings) as its arguments, and returns the
common words in both the sentences.
[Hint: store all the in a set. Read the documentation for set.] """


def test8(string1, string2):
    ls_string1 = string1.split(" ")
    ls_string2 = string2.split(" ")
    st = set()
    for each in ls_string1:
        if each.lower() in ls_string2:
            print(each)
            st.add(each)
    print(st)


# test8("Python is good", "Java is also good")

"""6. WAF: days_in_month() that take name of month in 3 character format(MMM), and year (YYYY)
as arguments and returns the number of days in the month.
Use the function is_leap_year() to check the special case of 29 days in leap year for month of
FEB. [Use dictionary to store the mapping of month and days.]
"""


def days_in_month(MMM):
    pass
    dic_month = {
        "JAN": 1,
        "FEB": 2,
        "MAR": 3,
        "APR": 4,
        "MAY": 5,
        "JUN": 6,
        "JUL": 7,
        "AUG": 8,
        "SEP": 9,
        "OCT": 10,
        "NOV": 11,
        "DEC": 12
    }
    month = dic_month[MMM]
    print(month)
    return month


def return_days(month, YYYY):
    # print(days_in_month)
    year = YYYY
    Month_a = month
    list_months = [1, 3, 5, 7, 8, 10, 12]
    if (year % 400 == 0) or (year % 4 == 0 and Month_a == 2):
        days = 29
    elif Month_a == 2:
        days = 28
    elif Month_a in list_months:
        days = 31
    else:
        days = 30
    print(days)
    is_leap_year()


def is_leap_year():
    year = 2020
    month = 7
    if (year % 400 == 0) or (year % 4 == 0 and month == 2):
        print("The given year ", year, " is a leap year")
    else:
        print("The given year ", year, " is NOT a leap year")


# days_in_month("FEB")
# is_leap_year()
return_days(days_in_month("JUL"), 2020)
