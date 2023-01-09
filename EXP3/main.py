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
    print(sentence.startswith('I'))
    print(sentence.startswith('86'))

    # Remove all newlines from the String.
    print(sentence.replace('\n', ''))

    # Replace all occurrence of substring in string
    replace_string = input("Enter a string")
    replaced_string = sentence.replace(sentence, replace_string)
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
                print(f"Vowel at position {i+1}")

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


print(task1())
