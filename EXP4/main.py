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
        if inpt == 1:
            os.system('cls')
            print("You have selected option 1 – Veg\n")
            veg_inpt = int(input(
                "\nSelect from the following options for Veg\n1- Veg Burger[50]\n2- Veg Pizza[90]\n3- Dosa[65]\nYour "
                "choice: "))
            if veg_inpt == 1:
                os.system('cls')
                list.append("Veg-Burger")
                bill = bill + 50
                print(f"Your cart: {list}\nCurrent Bill: {bill}")
                charinpt = input("Do you wish to continue[Y/N]")
            elif veg_inpt == 2:
                os.system('cls')
                list.append("Veg-Pizza")
                bill = bill + 90
                print(f"Your cart: {list}\nCurrent Bill: {bill}")
                charinpt = input("Do you wish to continue[Y/N]")
            elif veg_inpt == 3:
                os.system('cls')
                list.append("Dosa")
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
                "\nSelect from the following options for Non-Veg:\n1-Non-Veg Burger[70]\nNon-Veg Pizza[110]\nChicken "
                "Dosa[95]\nYour choice "
                "choice: "))
            if nonveg_inpt == 1:
                os.system('cls')
                list.append("Non Veg-Burger")
                bill = bill + 50
                print(f"Your cart: {list}\nCurrent Bill: {bill}")
                charinpt = input("Do you wish to continue[Y/N]")
            elif nonveg_inpt == 2:
                os.system('cls')
                list.append("Non-Veg-Pizza")
                bill = bill + 90
                print(f"Your cart: {list}\nCurrent Bill: {bill}")
                charinpt = input("Do you wish to continue[Y/N]")
            elif nonveg_inpt == 3:
                os.system('cls')
                list.append("Chicken Dosa")
                bill = bill + 65
                print(f"Your cart: {list}\nCurrent Bill: {bill}")
                charinpt = input("Do you wish to continue[Y/N]")
            else:
                os.system('cls')
                print("You entered the wrong choice, please select between 1,2,3")
                print(f"Your cart: {list}\nCurrent Bill: {bill}")
                charinpt = input("Do you wish to continue[Y/N]")


print(task2())
