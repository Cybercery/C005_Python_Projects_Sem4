import simple as s
import compound as c


principle = int(input("Enter principle value: "))
rate = int(input("Enter rate p.a: "))
time = int(input("Enter time period: "))

inpt = input("Calculate compound interest or simple interest?(Enter C or S): ")
if inpt == 'C' or inpt == 'c':
    n = int(input("Number of times compounded yearly?\n"))
    print(c.compound_interest(principle, rate/n, time*n))

elif inpt == 'S' or inpt == 's':
    print(s.simple_interest(principle, rate, time))

else:
    print("Error (C(c) and S(s) are the only valid inputs. ")
