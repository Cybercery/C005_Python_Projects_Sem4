import maths_details as md
import calculator as c


def task1():
    # Permutations and Combinations
    inpt = input("Permutations or Combinations? (Type P or C): ")
    n = int(input("n = "))
    r = int(input("r = "))
    if inpt == "P":
        print(f"nPr\n{n}P{r} = {md.permutations(n, r)}")

    elif inpt == "C":
        print(f"nCr\n{n}C{r} = {md.combinations(n, r)}")
    else:
        print("Error, please try again")

    number = int(input("Enter a number: "))

    # Factorial of a number
    print(f"Factorial = {md.printfactorial(number)}")

    # If Armstrong
    print(md.ifArmstrong(number))

    # Print Reverse
    print(md.printReverse(number))


def task2():

    # Factorial of a number
    inpt = int(input("Enter a number: "))
    print(c.print_factorial2(inpt))

    # Print fibonacci series upto number entered by user
    print(c.print_fibonacci(inpt))

