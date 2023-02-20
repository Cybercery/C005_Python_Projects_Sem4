class LessThanZero(Exception):
    pass


def printfactorial(number):
    factorial = 1
    for i in range(1, number + 1):
        factorial = factorial * i
    return factorial


def permutations(n, r):
    try:
        result = printfactorial(n) // printfactorial(n - r)
        if result > 0:
            return result
        else:
            raise LessThanZero
    except TypeError:
        print("pls put number")
    except LessThanZero:
        print("Enter a number greater than 0")
    except ValueError:
        print("I don't know how you achieved this, but use a valid number.")


def combinations(n, r):
    try:
        result = permutations(n, r) // printfactorial(r)
        if result > 0:
            return result
        else:
            raise LessThanZero
    except TypeError:
        print("pls put number")
    except LessThanZero:
        print("Enter a number greater than 0")
    except ValueError:
        print("I don't know how you achieved this, but use a valid number.")


def ifArmstrong(number):
    try:
        if number > 0:
            sumn = 0
            temp = number
            temp2 = temp
            count = 0

            while number != 0:
                number //= 10
                count += 1

            while temp > 0:
                digit = temp % 10
                sumn += digit ** count
                temp //= 10

            if temp2 == sumn:
                print(temp2, "is an Armstrong number")
            else:
                print(temp2, "is not an Armstrong number")
        else:
            raise LessThanZero

    except TypeError:
        print("pls put number")
    except LessThanZero:
        print("Enter a number greater than 0")
    except ValueError:
        print("I don't know how you achieved this, but use a valid number.")


def printReverse(number):
    try:
        temp = number
        reverse = 0
        remainder = 0
        while number != 0:
            remainder = number % 10
            reverse = reverse * 10 + remainder
            number = number // 10

        print(f"Original number: {temp}\nReversed number: {reverse}")
    except TypeError:
        print("pls put number")
    except ValueError:
        print("I don't know how you achieved this, but use a valid number.")


print(printReverse("d"))
