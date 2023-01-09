def task1():
    sentences = ["I am a fool", "String, 1", "String, 2"]
    # reverse a sentence
    sentence = "I \nam a fool"
    print(sentences[0][::-1])

    # Find the characters at an odd position in string input by User
    split_sentence = sentence.split()
    for i in range(1, len(split_sentence), 2):
        print(split_sentence[i], end=" ")
    print("\n")

    # Check string starts with a specific character entered by the user.
    inpt = input("Enter a specific character: ")
    print(sentence.startswith(inpt))

    # Remove all newlines from the String.
    print(sentence.replace('\n', ''))

    # Replace all occurrence of substring in string
    replace_string = input("Enter a string: ")
    replacer_string = input("What do you want the substring to be replaced by? ")
    replaced_string = sentence.replace(replace_string, replacer_string)
    print(replaced_string)

    # Replace punctuation mark from from list of string
    print(sentences[1].replace(',', ''))

    # Find the number of matching characters in a string
    sentence1 = input("Enter String1: ")
    sentence2 = input("Enter String2: ")
    counter = 0

    if len(sentence1) > len(sentence2):
        for i in range(len(sentence2)):
            if sentence2[i] == sentence1[i]:
                counter += 1
    if len(sentence2) > len(sentence1):
        for i in range(len(sentence1)):
            if sentence1[i] == sentence2[i]:
                counter += 1
    print(f"Number of repeated characters: {counter}")

    # Convert a string into a list
    full_sentence = input("Enter a sentence = ")
    print(full_sentence.split(" "))

    # to convert all elements of the list to integer data type

    list_int = ['8', '6']
    print(list_int)
    for i in range(0, len(list_int)):
        list_int[i] = int(list_int[i])

    print(list_int)

    # Count Total numbers of upper case and lower case characters in input string
    uppercount = 0
    lowercount = 0
    for i in range(0, len(sentence1)):
        if sentence1[i].isupper():
            uppercount += 1
        if sentence1[i].islower():
            lowercount += 1
    print(f"Number of Uppercase letters: {uppercount}\nNumber of lowercase letters: {lowercount}")

    # To find vowels in a string
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in range(0, len(sentence1)):
        for j in range(0, 10):
            if sentence1[i] == vowels[j]:
                print(f"Vowel at position {i + 1}")

    # To reverse a user input string
    reverse_string = input("Enter yet another string: ")
    print(reverse_string[::-1])

    # To Sort a string in Python
    non_alphabetic_order = "zyx"
    print(sorted(non_alphabetic_order))

    # To print input string in upper case and lower case

    print(f"Upper case: {sentence1.upper()}")
    print(f"Lower case: {sentence1.lower()}")

    # convert integer to string in Python
    number1 = int(input("Enter a number: "))
    str_number1 = str(number1)


def task2():
    # List to be used for all operations
    shopping_list = ["Manilkara zapota", "Guava", "Strawberry", "Banana", "Apple"]

    # index     [printing index of "Strawberry"]
    index = shopping_list.index("Strawberry")
    print(f"Index of Strawberry is {index}\n")

    # Add an item to the end of the list    [added "Manga" at the end of the list]
    shopping_list.append("Mango")
    print(f"{shopping_list}\n")

    # Modify an element by using the index of the element   [renamed "Manilkara zapota" to "Sapodilla"]
    shopping_list[0] = "Sapodilla"
    print(f"{shopping_list}\n")

    # Remove an item from the list      [removed "Sapodilla"]
    shopping_list.remove(shopping_list[0])
    print(f"{shopping_list}\n")

    # Remove all items from the list    [removed all elements of the list]
    shopping_list.clear()
    print(f"{shopping_list}\n")

    # Slice Elements from a List    [printing 1->3 which prints 1 & 2, end index is exclusive]
    new_list = [0, 7, 1, 2, 3, 4, 5, 4]
    print(new_list[1:3])
    print("\n")

    # Remove the item at the given position in the list, and return it
    new_list.remove(5)
    print(f"{new_list}\n")

    # Return the index in the list of the first item whose value is x

    search = int(input("Enter a number: "))
    for i in range(7):
        if new_list[i] == search:
            print(f"Number found at {i}\n")
            break

    # Return the number of times 'x' appear in the list

    counter = 0
    search2 = int(input("Enter a number: "))
    for i in range(7):
        if search2 == new_list[i]:
            counter = counter + 1

    print(f"Element appears {counter} times. \n")

    # Sort the items of the list in place
    new_list.sort()
    print(f"{new_list}\n")

    # Reverse the elements of the list in place
    new_list.reverse()
    print(f"{new_list}\n")


def task3_4():
    # Write a python program to count unique values inside a list
    # Write a python program to print a list excluding the duplicates
    newer_list = ["Papaya", "Watermelon", "Muskmelon", "Muskmelon", "Muskmelon", "Muskmelon", "Pineapple"]
    unique = []
    count = 0
    for i in range(7):
        if newer_list[i] not in unique:
            count = count + 1
            unique.append(newer_list[i])
    print(f"Total no of unique characters: {count}\n")
    print(f"List without duplicates is : {unique}\n")


def task5():
    # Write a python program to count positive and negative numbers in a list
    minus = 0
    plus = 0
    newerer_list = [-3, -2, -1, 0, 1, 2, 3]
    for i in range(len(newerer_list)):
        if newerer_list[i] > 0:
            plus += 1
        elif newerer_list[i] < 0:
            minus += 1
        else:
            continue
    print(f"Number of negative numbers: {minus}\nNumber of positive numbers: {plus}")


def task6():
    # Write a python program to find the characters at an odd position in string input by user

    sentence = input("Enter a string: ")
    for i in range(1, len(sentence), 2):
        print(sentence[i], end=" ")
    print("\n")


def task7():
    # Write a python program to check if a string starts with a specific character entered by the user.
    sentence = "No"
    inpt = input("Enter a specific character: ")
    print(sentence.startswith(inpt))


def task8():
    # Write a python program to replace all occurrence of substring in string
    sentence = "Resident Evil"
    replace_string = input("Enter a string: ")
    replacer_string = input("What do you want the substring to be replaced by? ")
    replaced_string = sentence.replace(replace_string, replacer_string)
    print(replaced_string)


def task9():
    # Write a python program to find the number of matching characters in two string
    sentence1 = input("Enter String1: ")
    sentence2 = input("Enter String2: ")
    counter = 0

    if len(sentence1) > len(sentence2):
        for i in range(len(sentence2)):
            if sentence2[i] == sentence1[i]:
                counter += 1
    if len(sentence2) > len(sentence1):
        for i in range(len(sentence1)):
            if sentence1[i] == sentence2[i]:
                counter += 1
    print(f"Number of repeated characters: {counter}")


print(task9())