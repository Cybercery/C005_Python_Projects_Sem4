from math import factorial


def task_a():
    """
    a. Given a year, determine whether it is a leap year. If it is a leap year, return the
    Boolean True, otherwise return False.
    Input 1990
    Output False (Hackerrank)
    """
    year = int(input("Enter a year: "))
    task_a_ifLeapYear(year)


def task_a_ifLeapYear(year):
    if year % 400 == 0:
        print(f"{year} is a leap year")
    elif year % 4 == 0 and year % 100 != 0:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")


def task_b():
    """
    b. Develop a python function to multiply all the numbers in a list. Sample List : (8, 2, 3,
    -1, 7) Expected Output: -336
    """
    list_to_be_multiplied = []
    product = 1
    inpt = int(input("Enter number of elements in a list: "))
    for i in range(inpt):
        input_element = int(input("Enter element: "))
        list_to_be_multiplied.append(input_element)
        product = product * input_element
    print(list_to_be_multiplied)
    print(f"Product: {product}")


def task_c():
    """
    c. Develop a Python function that prints out the first n rows of Pascal's triangle.
    """
    inpt = int(input("Enter number of rows of Pascal's Triangle: "))
    task_c_print_pascal(inpt)


def task_c_print_pascal(inpt):
    for i in range(inpt):
        for j in range(inpt - i - 1):
            print(end=" ")
        for j in range(i + 1):
            print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")
        print()


"""
e. What is the output of the following function call
"""


def outer_fun(a, b):  # Step 2: 5 and 10 saved in a and b
    def inner_fun(c, d):  # Step 4: Inner function: 5 and 10 saved in c and d, returned c and d, 50+10
        return c + d

    return inner_fun(a, b)  # Step 3: calling inner function, saving 5, 10 in c and d respectively
    return a


# result = outer_fun(5, 10)  # Step 1: calling outer function, saving 5, 10 in a,b respectively
# print(result)  # Step 5: Printing 5 + 10
"""
Output: 15
"""

"""
f. What is the output of the following display_person() function call
"""


def display_person(*args):  # Step 2: "Emma" and "25" saved in args
    for i in args:  # Step 3: for loop starting from 0 and ending at the final element of args ("25" in this case)
        print(i)  # Step 4: Printing each element of args


display_person("Emma", "25")  # Step 1: Calling display_person, adding "Emma" and "25" to args
"""
Output:
Emma 
25
"""