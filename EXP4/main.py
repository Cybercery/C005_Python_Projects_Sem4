import os


def task1():
    # 1.Create a tuple for storing student information and perform the following functions:
    info_tuple = ("Soham Doiphode", "C005", 70322100141, "B-1",)

    # a. Print an item of the tuple
    print(f"Name: {info_tuple[0]}")
    print(f"Roll Number: {info_tuple[1]}")
    print(f"SAP ID: {info_tuple[2]}")
    print(f"Division & Batch number: {info_tuple[3]}\n")

    # b. Check if an element exists within a tuple
    inpt = input("Enter element to be searched for: ")
    for i in range(len(info_tuple)):
        if inpt == info_tuple[i]:
            print(f"Element is found at Index: {i}\n")

    # c. Check number of times an item has repeated
    counter = 0
    for i in range(len(info_tuple)):
        for j in range(len(info_tuple)):
            if info_tuple[i] == info_tuple[j]:
                counter += 1
        print(f"{info_tuple[i]} has been repeated {counter} times.")
        counter = 0
    print("\n")

    # d. Remove an item from a tuple    [Removed 70322100141 from the tuple]
    print(f"Initial tuple: {info_tuple}")
    info_tuple = list(info_tuple)
    info_tuple.remove(info_tuple[2])
    info_tuple = tuple(info_tuple)
    print(f"After removal: {info_tuple}\n")

    # e. Slice a tuple  [printing first and second element]
    print(f"{info_tuple[0:2]}\n")

    # f. Get the index of an item of the tuple
    search = input("Enter an element: ")
    index = info_tuple.index(search)
    print(f"Position: {index}\n")

    # g. Print the size of a tuple
    print(f"Length of tuple: {len(info_tuple)}\n")

    # h. Modify items of a tuple
    print(f"Initial tuple: {info_tuple}")
    info_tuple = list(info_tuple)
    temp = info_tuple[0]
    info_tuple[0] = info_tuple[1]
    info_tuple[1] = temp
    info_tuple = tuple(info_tuple)
    print(f"After modification: {info_tuple}\n")


def task2():
    # 2.Develop a menu driven program for a food hub.
    # Example:
    # Please select option:
    # 1- Veg Menu
    # 2- Non-Veg Menu
    # 0- Exit
    # Enter your choice: 1
    # You have selected option 1 – Veg
    # Select from the following options for Veg
    # 1- Veg Burger
    # 2- Veg Pizza
    # 3- Dosa
    # Enter your choice: 2
    # Do you wish to continue [Y/N] ? Y
    # Select from the following options for Veg
    # 1- Veg Burger
    # 2- Veg Pizza
    # 3- Dosa
    # Enter your choice: 1
    # Do you wish to continue [Y/N] ? N
    # Your order is : [“Veg Pizza”, “Veg Burger”]
    # Perform operations accordingly.
    # b. For the same above example include price. The output will look like
    # {“Veg Pizza” : 120, “Veg Burger”: 110}. Also print the total price of user choice items.
    list = []
    bill = 0
    charinpt = "Y"
    print(f"Your cart: {list}\nCurrent Bill: {bill}")
    inpt = int(input("Please select option:\n1 - Veg Menu\n2 - Non-Veg Menu\n0 - Exist\nYour Choice: "))
    while charinpt == "Y" or charinpt == "y":
        inpt = int(input("Please select option:\n1 - Veg Menu\n2 - Non-Veg Menu\n0 - Exist\nYour Choice: "))
        if inpt == 1:
            os.system('cls')
            print("You have selected option 1 – Veg\n")
            veg_inpt = int(input(
                "\nSelect from the following options for Veg\n1- Veg Burger[50]\n2- Veg Pizza[90]\n3- Dosa[65]\nYour "
                "choice: "))
            if veg_inpt == 1:
                os.system('cls')
                list.append("Veg-Burger[50]")
                bill = bill + 50
                print(f"Your cart: {list}\nCurrent Bill: {bill}")
                charinpt = input("Do you wish to continue[Y/N]")
            elif veg_inpt == 2:
                os.system('cls')
                list.append("Veg-Pizza[90]")
                bill = bill + 90
                print(f"Your cart: {list}\nCurrent Bill: {bill}")
                charinpt = input("Do you wish to continue[Y/N]")
            elif veg_inpt == 3:
                os.system('cls')
                list.append("Dosa[65]")
                bill = bill + 65
                print(f"Your cart: {list}\nCurrent Bill: {bill}")
                charinpt = input("Do you wish to continue[Y/N]")
            else:
                os.system('cls')
                print("You entered the wrong choice, please select between 1,2,3")
                print(f"Your cart: {list}\nCurrent Bill: {bill}")
                charinpt = input("Do you wish to continue[Y/N]")
        elif inpt == 2:
            os.system('cls')
            print("You have selected option 2 - Non-Veg\n")
            nonveg_inpt = int(input(
                "\nSelect from the following options for Non-Veg:\n1. Non-Veg Burger[70]\n2. Non-Veg Pizza[110]\n3. Chicken "
                "Dosa[95]\nYour choice "
                "choice: "))
            if nonveg_inpt == 1:
                os.system('cls')
                list.append("Non Veg-Burger[70]")
                bill = bill + 70
                print(f"Your cart: {list}\nCurrent Bill: {bill}")
                charinpt = input("Do you wish to continue[Y/N]")
            elif nonveg_inpt == 2:
                os.system('cls')
                list.append("Non-Veg-Pizza[110]")
                bill = bill + 110
                print(f"Your cart: {list}\nCurrent Bill: {bill}")
                charinpt = input("Do you wish to continue[Y/N]")
            elif nonveg_inpt == 3:
                os.system('cls')
                list.append("Chicken Dosa[95]")
                bill = bill + 95
                print(f"Your cart: {list}\nCurrent Bill: {bill}")
                charinpt = input("Do you wish to continue[Y/N]")
            else:
                os.system('cls')
                print("You entered the wrong choice, please select between 1,2,3")
                print(f"Your cart: {list}\nCurrent Bill: {bill}")
                charinpt = input("Do you wish to continue[Y/N]")
    os.system('cls')
    print(f"Your cart: {list}\nTotal Bill: {bill}")


def task3():
    """
    3. Write a Python script to concatenate following dictionaries to create a new one
    Sample Dictionary :
    dic1={1:10, 2:20}
    dic2={3:30, 4:40}
    dic3={5:50,6:60}
    Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
    """
    dic1 = {1: 10, 2: 20}
    dic2 = {3: 30, 4: 40}
    dic3 = {5: 50, 6: 60}
    dic4 = {}
    for d in (dic1, dic2, dic3):
        dic4.update(d)
    print(dic4)


def task4():
    """
    4. Write a Python script to print a dictionary where the keys are numbers between 1 and 15
    (both included) and the values are square of keys.
    Sample Dictionary
    {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14:
    196, 15: 225}
    """
    squared = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169,
               14: 196, 15: 225}
    print(squared)


def task5():
    """
    5.Write a Python program to print all unique values in a dictionary
    Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"},
    {"V":"S009"},{"VIII":"S007"}]
    Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'
    """

    sample_data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"},
                   {"V": "S009"}, {"VIII": "S007"}]

    u_value = []
    print(sample_data)
    u_value = list(set(val for dic in sample_data for val in dic.values()))
    print(u_value)


def task6():
    """
    Write a Python program to extract a list of values from a given list of dictionaries.
    Original Dictionary:
    [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
    Extract a list of values from said list of dictionaries where subject = Science
    [92, 94, 88]
    Original Dictionary:
    [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
    Extract a list of values from said list of dictionaries where subject = Math
    [90, 89, 92
    """

    def test(lst, marks):
        result = [d[marks] for d in lst if marks in d]

        return result

    marks = [{'Math': 90, 'Science': 92},
             {'Math': 89, 'Science': 94},
             {'Math': 92, 'Science': 88}]

    print("\nOriginal Dictionary:")
    print(marks)
    subj = "Science"
    print("\nExtract a list of values from said list of dictionaries where subject =", subj)
    print(test(marks, subj))

    print("\nOriginal Dictionary:")
    print(marks)
    subj = "Math"
    print("\nExtract a list of values from said list of dictionaries where subject =", subj)
    print(test(marks, subj))


def task7():
    """
    Write a Python program to print a tuple with string formatting.
    Sample tuple : (100, 200, 300)
    Output : This is a tuple (100, 200, 300
    """
    sample_tuple = (100, 200, 300)
    print("This is a tuple " + str(sample_tuple))


def task8():
    """
    Write a Python program to sort a tuple by its float element.
         Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
        Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')
    """
    price = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
    print(sorted(price, key=lambda x: float(x[1]), reverse=True))


def task9():
    """
    9.Write a Python program calculate the product, multiplying all the numbers of a given tuple.
    Original Tuple:
    (4, 3, 2, 2, -1, 18)
    Product - multiplying all the numbers of the said tuple: -864
    Original Tuple:
    (2, 4, 8, 8, 3, 2, 9)
    Product - multiplying all the numbers of the said tuple: 27648
    """

    def mutiple_tuple(nums):
        temp = list(nums)
        product = 1
        for x in temp:
            product *= x
        return product

    nums = (4, 3, 2, 2, -1, 18)
    print("Original Tuple: ")
    print(nums)
    print("Product - multiplying all the numbers of the said tuple:", mutiple_tuple(nums))

    nums = (2, 4, 8, 8, 3, 2, 9)
    print("\nOriginal Tuple: ")
    print(nums)
    print("Product - multiplying all the numbers of the said tuple:", mutiple_tuple(nums))


def task10():
    """
    10.Write a Python program to calculate the average value of the numbers in a given tuple of
    tuples.
    Original Tuple:
    ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
    Average value of the numbers of the said tuple of tuples:
    [30.5, 34.25, 27.0, 23.25]
    Original Tuple:
    ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
    Average value of the numbers of the said tuple of tuples:
    [25.5, -18.0, 3.75]
    """
    def average_tuple(nums):
        result = [sum(x) / len(x) for x in zip(*nums)]
        return result

    nums = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
    print("Original Tuple: ")
    print(nums)
    print("\nAverage value of the numbers of the said tuple of tuples:\n", average_tuple(nums))

    nums = ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
    print("\nOriginal Tuple: ")
    print(nums)
    print("\nAverage value of the numbers of the said tuple of tuples:\n", average_tuple(nums))


def task11():
    """
    1.Write a Python program to check if a specified element presents in a tuple of tuples.
    Original list:
    (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
    Check if White present in said tuple of tuples!
    True
    Check if White present in said tuple of tuples!
    True
    Check if Olive present in said tuple of tuples!
    False
    """

    def check_in_tuples(colors, c):
        result = any(c in tu for tu in colors)
        return result

    colors = (
        ('Red', 'White', 'Blue'),
        ('Green', 'Pink', 'Purple'),
        ('Orange', 'Yellow', 'Lime'),
    )
    print("Original list:")
    print(colors)
    c1 = 'White'
    print("\nCheck if", c1, "presenet in said tuple of tuples!")
    print(check_in_tuples(colors, c1))
    c1 = 'White'
    print("\nCheck if", c1, "presenet in said tuple of tuples!")
    print(check_in_tuples(colors, c1))
    c1 = 'Olive'
    print("\nCheck if", c1, "presenet in said tuple of tuples!")
    print(check_in_tuples(colors, c1))


def task12():
    """
    12.Write a Python program to convert a given list of tuples to a list of lists.
    Original list of tuples: [(1, 2), (2, 3), (3, 4)]
    Convert the said list of tuples to a list of lists: [[1, 2], [2, 3], [3, 4]]
    Original list of tuples: [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
    Convert the said list of tuples to a list of lists: [[1, 2], [2, 3, 5], [3, 4], [2, 3, 4, 2]]
    """

    def test(lst_tuples):
        result = [list(el) for el in lst_tuples]
        return result

    lst_tuples = [(1, 2), (2, 3), (3, 4)]
    print("Original list of tuples:")
    print(lst_tuples)
    print("Convert the said list of tuples to a list of lists:")
    print(test(lst_tuples))
    lst_tuples = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
    print("\nOriginal list of tuples:")
    print(lst_tuples)
    print("Convert the said list of tuples to a list of lists:")
    print(test(lst_tuples))

print(task9())
print(task10())
print(task11())
print(task12())

