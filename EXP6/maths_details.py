def printfactorial(number):
    factorial = 1
    for i in range(1, number + 1):
        factorial = factorial * i
    return factorial


def permutations(n, r):
    result = printfactorial(n) // printfactorial(n - r)
    return result


def combinations(n, r):
    result = permutations(n, r) // printfactorial(r)
    return result


def ifArmstrong(number):
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


def printReverse(number):
    temp = number
    reverse = 0
    remainder = 0
    while number != 0:
        remainder = number % 10
        reverse = reverse * 10 + remainder
        number = number // 10

    print(f"Original number: {temp}\nReversed number: {reverse}")
