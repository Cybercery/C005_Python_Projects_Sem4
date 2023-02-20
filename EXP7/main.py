from math import factorial


def task_a(year):
    # Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return
    # False
    try:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        elif year % 4 == 0 and year % 100 != 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    except ValueError:
        print("Not a valid number, please try again")
    except TypeError:
        print("That's not a number, try again.")


def task_b():
    try:
        """
        b. Develop a python function to multiply all the numbers in a list. 
        Sample List : (8, 2, 3, -1, 7) 
        Expected Output: -336
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
    except TypeError:
        print("THAT'S NOT A NUMBER")
    except ValueError:
        print("I don't know how you achieved this, but use a valid number.")


class LessThanZero(Exception):
    pass


def task_c():
    """
    c. Develop a Python function that prints out the first n rows of Pascal's triangle.
    """
    try:
        inpt = int(input("Enter number of rows of Pascal's Triangle: "))
        if inpt > 0:
            task_c_print_pascal(inpt)
        else:
            raise LessThanZero
    except TypeError:
        print("That's not a number, try again.")
    except ValueError:
        print("Enter a valid number.")
    except LessThanZero:
        print("Enter a number greater than zero")


def task_c_print_pascal(inpt):
    for i in range(inpt):
        for j in range(inpt - i - 1):
            print(end=" ")
        for j in range(i + 1):
            print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")
        print()


print(task_c())
