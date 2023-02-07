def print_factorial2(number):
    factorial = 1
    for i in range(1, number + 1):
        factorial = factorial * i
    return factorial


def print_fibonacci(number):
    t1 = 0
    t2 = 1
    sun = 0
    for i in range(number):
        print(sun, end="")
        sun = t1 + t2
        t2 = t1
        t1 = sun

    return 0
