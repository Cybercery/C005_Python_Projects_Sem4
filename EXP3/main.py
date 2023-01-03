def task1():
    # reverse a sentence
    sentence = "I am a fool"
    print(sentence[::-1])
    print("")

    # Find the characters at an odd position in string input by User
    split_sentence = sentence.split()
    for i in range(1, len(split_sentence), 2):
        print(split_sentence[i], end=" ")
    print("\n")

    # Check string starts with a specific character entered by the user.
    print(sentence.startswith('I'))
    print(sentence.startswith('86'))
    print("\n")

    # Remove all newlines from the String.
    print(sentence.replace(' ', ''))

    # Replace all occurrence of substring in string
    replace_string = input("Enter a string")
    replaced_string = sentence.replace(sentence, replace_string)
    print(replaced_string)


print(task1())
