"""
Pattern 1
1
12
123
1234
12345
"""
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print("")

"""
Pattern 2
A
A B
A B C 
A B C D 
A B C D E
"""

for i in range(1, 6):
    n = 'A'
    for j in range(1, i + 1):
        print(n, end="")
        n = chr(ord(n) + 1)
    print("")

"""
Pattern 3
*
* *
* * *
* * * *
* * * * *
"""
for i in range(1, 6):
    for j in range(1, i + 1):
        print(end="*")
    print("")

"""
Pattern 4 
1
2 2
3 3 3 
4 4 4 4
5 5 5 5 5
"""
for i in range(1, 6):
    for j in range(1, i + 1):
        print(i, end="")
    print("")
"""
Pattern 5
A
B B
C C C
D D D D
E E E E E
"""
n = 'A'
for i in range(1, 6):
    for j in range(1, i + 1):
        print(n, end="")
    n = chr(ord(n) + 1)
    print("")

"""
Pattern 6
    *
   **
  ***
 ****
*****
"""