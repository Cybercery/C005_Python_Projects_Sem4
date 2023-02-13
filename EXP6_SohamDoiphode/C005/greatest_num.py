def greatest_num(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print(f"{num1} is the greatest")
    elif num2 > num1 and num2 > num3:
        print(f"{num2} is the greatest")
    else:
        print(f"{num3} is the greatest")


num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number(again): "))
num3 = int(input("Enter a number(again)(again): "))
print(greatest_num(num1, num2, num3))
