def theory1():
    # input number

    a = int(input("Enter a number: "))
    b = int(input("Enter a number(again): "))

    # Addition
    c = a + b

    print("sum = {0} ".format(c))

    # Ordered List
    lang1 = ["eng", "hindi", "french"]

    # Tuple (also ordered, but cannot be changed)

    lang2 = ("eng", "hindi", "french")

    # Unordered list - Dictionary

    capital_city = {'Nepal': 'Kathmandu', 'India': 'Delhi', 'Italy': 'Rome'}
    # Can be called using key
    print(capital_city['Nepal'])
    return 0


def task2():
    # Task 2

    # 1. Print String
    print("Hello World")

    # 2. Initialisation and printing integer
    var1 = 5
    var2 = "Hello"
    var3 = 5.0
    print(var1, var2, var3)

    # 3. Basic Arithmetic
    var2 = var1 * 10 + 5 - 75 / 10
    print(var2)

    return 0


def task3():
    # Task 3

    # a. Create a variable savings with the value 100. Check out this variable by typing print(savings) in the script

    variable_savings = 100
    print(variable_savings)

    # b. Python as a calculator. (Perform all arithmetic operations on console/shell)

    a = int(input("Enter a number: "))
    b = int(input("Enter a number(again): "))

    print("Sum = {0} ".format(a + b))
    print("Difference = {0} ".format(a - b))
    print("Multiplication = {0} ".format(a * b))
    print("Division = {0} ".format(a / b))

    # c. Suppose you have Rs.100, which you can invest with a 10% return each year. After one year, it's 100×1.1=110
    # rupees, and after two years it's 100×1.1×1.1=121. Add code to calculate how much money you end up with after 7
    # years, and print the result.

    principle = 100
    rate = 10
    time = 7
    ci = principle*(1+rate/100)**time
    print(ci)

    # d. Write a Python script that prints the result for 8958937768937 divided by 2851718461558
    print(8958937768937/2851718461558)

    # e. Take two variables a and b and print three lines where:
    # ○ The first line contains the sum of the two numbers.
    # ○ The second line contains the difference of the two numbers (first - second).
    # ○ The third line contains the product of the two numbers.

    a = int(input("Enter a number: "))
    b = int(input("Enter a number(again): "))

    print("Sum = {0} ".format(a + b))
    print("Difference = {0} ".format(a - b))
    print("Multiplication = {0} ".format(a * b))

    # f.Take input from user in two variables and print the following:
    # ○ Add logic to print two lines. The first line should contain the result of integer division
    # ○ The second line should contain the result of float division
    # ○ No rounding or formatting is necessary.

    a = int(input("Enter a number: "))
    b = int(input("Enter a number(again): "))
    print(f"Integer Division: {a//b}\nFloat Division: {a/b} ")

    # g. Take input from the user in variables first_name ,last_name and age. Print the full
    # name of the user with age. Output should look like, e.g “Age of John William is 16”
    age = int(input("Enter your age: "))
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    print(f"Age of {first_name} {last_name} is {age}")

    # h. Accept the radius of a circle and find its area and circumference.
    radius = int(input("Enter the radius of the circle: "))
    print(f"Area: {3.14*radius**2}\nCircumference: {2*3.14*radius}")

    # i. Consider the following scenario:
    # Input :
    # Principle (amount): 1200
    # Time: 2
    # Rate: 5.4
    # Output : Compound Interest = 133.099243
    # Calculate Compound Interest, use your own variables
    principle = 1000
    rate = 15
    time = 2
    ci = principle * (1 + rate / 100) ** time
    print(f"Compound interest: {ci-principle}")

    # j. Write a program to accept 5 numbers from the user using individual statements. Print
    # the sum, average of the numbers. Check if the sum is less than 100 and print the true
    # false value
    n1 = int(input("Enter a number: "))
    n2 = int(input("Enter a number(again): "))
    n3 = int(input("Enter a number(again x2): "))
    n4 = int(input("Enter a number(again x3): "))
    n5 = int(input("Enter a number(again x4): "))
    sum_of_n = n1+n2+n3+n4+n5
    print(f"Sum ={sum_of_n}\nAverage: {sum_of_n/5}")
    if sum_of_n<=100:
        print("true")
    else:
        print("False")

    # k. Take input from the user in two variables. Perform below operations
    # ○ Find remainder
    # ○ Perform floor division
    # ○ Calculate a raise to b
    a = int(input("Enter a number: "))
    b = int(input("Enter a number(again): "))
    print(f"Remainder: {a%b}\nFloor Division: {a//b}\nNumber a raise to b: {a**b}")

    # l. Calculate area of a circle
    radius = int(input("Enter radius of a circle: "))
    print(f"Area of the circle of radius {radius} is {3.14*radius**2}")

    # m. Write a program to store integer value in a variable ‘a’. Perform below operations on the variable.
    # ○ Bitwise shift left
    # ○ Bitwise shift right

    a = int(input("Enter a number: "))
    print(f"Bitwise Shift Left = {a<<1}\nBitwise Shift Right: {a>>1}")

    return 0


print(task3())