def question1():
    # To find whether a number is strong or not
    for n in range(1, 100):
        original: int = n
        d = 1
        sun = 0

        while n > 0:
            factorial = 1
            d = n % 10

            while d > 0:
                factorial = factorial * d
                d = d - 1

            sun = sun + factorial
            n = n // 10

        if sun == original:
            print(f"{original} is Strong")

    return 0


def question2():
    # Find an element in a list
    names = ["Malenia", "Radahn", "Godrick", "Miquella", "Mogh", "Morgott", "Margit", "Melina", "Ranni", "Rykard"]
    tobesearchedfor = input("Enter the name to be found: ")

    for i in names:
        if i == tobesearchedfor:
            print(f"The name is present at position {names.index(i)}")

    return 0


def question3():
    # Print fibonacci series
    t1 = 0
    t2 = 1
    i = 0
    n = int(input("Enter a number: "))
    if n == 1:
        print(0)

    else:

        while i < n:
            sun = t1 + t2
            print(t1)
            t1 = t2
            t2 = sun
            i = i + 1

    return 0


def question4():
    n = int(input("Enter a number: "))
    d = 1
    sun = 0
    r = 0
    while n > 0:
        d = n % 10
        r = r * 10 + d
        n = n // 10

    print(f"Reverse = {r}")

    return 0


def question5():
    sun = 0
    for i in range(1, 200, 2):
        sun = sun + i
    print(sun)
    return 0


def question6():
    for i in range(5, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

    return 0


def question7():
    n1 = int(input("Enter marks for English: "))
    if n1 > 100 or n1 < 0:
        print("Error :( Marks have to have between 0 and 100")
        return
    n2 = int(input("Enter marks for Maths: "))
    if n2 > 100 or n2 < 0:
        print("Error :( Marks have to have between 0 and 100")
        return
    n3 = int(input("Enter marks for Physics: "))
    if n3 > 100 or n3 < 0:
        print("Error :( Marks have to have between 0 and 100")
        return
    n4 = int(input("Enter marks for Chemistry: "))
    if n4 > 100 or n4 < 0:
        print("Error :( Marks have to have between 0 and 100")
        return
    n5 = int(input("Enter marks for Computer Science: "))
    if n5 > 100 or n5 < 0:
        print("Error :( Marks have to have between 0 and 100")
        return

    average = (n1 + n2 + n3 + n4 + n5) / 5
    print(f"{average}")
    if average >= 92:
        print("Merit")

    elif 91 >= average >= 75:
        print("Distinction")

    elif 74 >= average >= 60:
        print("First Class")

    elif 59 >= average >= 45:
        print("Second Class")

    else:
        print("Fail")

    return 0


print(question7())
