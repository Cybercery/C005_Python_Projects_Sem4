import csv
# Create and Write
file1 = open('C:/Users/soham/PycharmProjects/C005_Python_Projects_Sem4/EXP9/exp7.txt', 'w', encoding="utf-8")
file1.write('Hello World\n')
file1.close()

# Read
file1 = open('exp7.txt', 'r')
print(file1.read())
file1.close()

# Append
file1 = open('exp7.txt', 'a', encoding="utf-8")
file1.write('Appending text\n\n\n\n')
file1.close()

# Read again
file1 = open('exp7.txt', 'r', encoding="utf-8")
print(file1.read())
file1.close()

# Read data from CSV file
with open('C:/Users/soham/PycharmProjects/C005_Python_Projects_Sem4/EXP9/SampleCSVFile_2kb.csv', 'r') as file2:
    file_csv = csv.reader(file2)
    for i in file_csv:
        print(i)
