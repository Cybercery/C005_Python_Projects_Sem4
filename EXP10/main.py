import re


# 1. Write a Python program to check that a string contains only a certain set of characters
# (in this case a-z, A-Z and 0-9).
def one():
    def is_allowed_specific_char(string):
        charRe = re.compile(r'[^a-zA-Z0-9.]')
        string = charRe.search(string)
        return not bool(string)

    print(is_allowed_specific_char("ABCDEFabcdef123450"))
    print(is_allowed_specific_char("*&%@#!}{"))
    return "\n"


# 2. Write a Python program that matches a string that has an a followed by zero or more b's.
def two():
    def text_match(text):
        patterns = 'ab*?'
        if re.search(patterns, text):
            return 'Found a match!'
        else:
            return 'Not matched!'

    print(text_match("ac"))
    print(text_match("abc"))
    print(text_match("abbc"))
    return "\n"


# 3. Write a Python program that matches a string that has an a followed by one or more b's.
def three():
    def text_match(text):
        patterns = 'ab+?'
        if re.search(patterns, text):
            return 'Found a match!'
        else:
            return 'Not matched!'

    print(text_match("ab"))
    print(text_match("abc"))
    return "\n"


# 4. Write a Python program that matches a string that has an a followed by zero or one 'b'.
def four():
    def text_match(text):
        patterns = 'ab?'
        if re.search(patterns, text):
            return 'Found a match!'
        else:
            return 'Not matched!'

    print(text_match("ab"))
    print(text_match("abc"))
    print(text_match("abbc"))
    print(text_match("aabbc"))
    return "\n"


# 5. Write a Python program that matches a string that has an a followed by three 'b'.
def five():
    def text_match(text):
        patterns = 'ab{3}?'
        if re.search(patterns, text):
            return 'Found a match!'
        else:
            return 'Not matched!'

    print(text_match("abbb"))
    print(text_match("aabbbbbc"))
    return "\n"


# 6. Write a Python program that matches a string that has an a followed by two to three 'b'.
def six():
    def text_match(text):
        patterns = 'ab{2,3}?'
        if re.search(patterns, text):
            return 'Found a match!'
        else:
            return 'Not matched!'

    print(text_match("ab"))
    print(text_match("aabbbbbc"))
    return "\n"


# 7. Write a Python program to find sequences of lowercase letters joined with a underscore
def seven():
    def text_match(text):
        patterns = '^[a-z]+_[a-z]+$'
        if re.search(patterns, text):
            return 'Found a match!'
        else:
            return 'Not matched!'

    print(text_match("aab_cbbbc"))
    print(text_match("aab_Abbbc"))
    print(text_match("Aaab_abbbc"))
    return "\n"


# 8. Write a Python program to find the sequences of one upper case letter followed by lower case letters
def eight():
    def text_match(text):
        patterns = '^[a-z]+_[a-z]+$'
        if not re.search(patterns, text):
            return 'Found a match!'
        else:
            return 'Not matched!'

    print(text_match("aab_cbbbc"))
    print(text_match("aab_Abbbc"))
    print(text_match("Aaab_abbbc"))
    return "\n"


# 9. Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
def nine():
    def text_match(text):
        patterns = 'a.*?b$'
        if re.search(patterns, text):
            return 'Found a match!'
        else:
            return 'Not matched!'

    print(text_match("aabbbbd"))
    print(text_match("aabAbbbc"))
    print(text_match("accddbbjjjb"))
    return ""


# 10. Write a Python program that matches a word at the beginning of a string.
def ten():
    def text_match(text):
        patterns = '^\w+'
        if re.search(patterns, text):
            return 'Found a match!'
        else:
            return 'Not matched!'

    print(text_match("The quick brown fox jumps over the lazy dog."))
    print(text_match(" The quick brown fox jumps over the lazy dog."))
    return "\n"


# 11. Write a Python program that matches a word at the end of string, with optional punctuation.
def eleven():
    def text_match(text):
        patterns = '\w+\S*$'
        if re.search(patterns, text):
            return 'Found a match!'
        else:
            return 'Not matched!'

    print(text_match("The quick brown fox jumps over the lazy dog."))
    print(text_match("The quick brown fox jumps over the lazy dog. "))
    print(text_match("The quick brown fox jumps over the lazy dog "))
    return "\n"


# 12. Write a Python program that matches a word containing 'z'
def twelve():
    def text_match(text):
        patterns = '\w*z.\w*'
        if re.search(patterns, text):
            return 'Found a match!'
        else:
            return 'Not matched!'

    print(text_match("The quick brown fox jumps over the lazy dog."))
    print(text_match("Python Exercises."))
    return "\n"


# 13. Write a Python program that matches a word containing 'z', not at the start or end of the word.
def thirteen():
    def text_match(text):
        patterns = '\Bz\B'
        if re.search(patterns, text):
            return 'Found a match!'
        else:
            return 'Not matched!'

    print(text_match("The quick brown fox jumps over the lazy dog."))
    print(text_match("Python Exercises."))
    return "\n"


# 14. Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.
def fourteen():
    def text_match(text):
        patterns = '^[a-zA-Z0-9_]*$'
        if re.search(patterns, text):
            return 'Found a match!'
        else:
            return 'Not matched!'

    print(text_match("The quick brown fox jumps over the lazy dog."))
    print(text_match("Python_Exercises_1"))
    return "\n"


# 15. Write a Python program where a string will start with a specific number
def fifteen():
    def match_num(string):
        text = re.compile(r"^5")
        if text.match(string):
            return True
        else:
            return False

    print(match_num('5-2345861'))
    print(match_num('6-2345861'))
    return "\n"


# 16. Write a Python program to remove leading zeros from an IP address
def sixteen():
    ip = "216.08.094.196"
    string = re.sub('\.[0]*', '.', ip)
    print(string)
    return "\n"


# 17. Write a Python program to check for a number at the end of a string
def seventeen():
    def end_num(string):
        text = re.compile(r".*[0-9]$")
        if text.match(string):
            return True
        else:
            return False

    print(end_num('abcdef'))
    print(end_num('abcdef6'))
    return "\n"


# 18. Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string. "Exercises number,
# 1, 12, 13, and 345 are important"
def eighteen():
    results = re.finditer(r"([0-9]{1,3})", "Exercises number 1, 12, 13, and 345 are important")
    print("Number of length 1 to 3")
    for n in results:
        print(n.group(0))
    return "\n"


# 19. Write a Python program to search some literals strings in a string.
# Sample text : 'The quick brown fox jumps over the lazy dog.'
# Searched words : 'fox', 'dog', 'horse'
def nineteen():
    patterns = ['fox', 'dog', 'horse']
    text = 'The quick brown fox jumps over the lazy dog.'
    for pattern in patterns:
        print('Searching for "%s" in "%s" ->' % (pattern, text), )
        if re.search(pattern, text):
            print('Matched!')
        else:
            print('Not Matched!')
    return "\n"


# 20. Write a Python program to search a literals string in a string and also find the location within the original
# string where the pattern occurs. Sample text : 'The quick brown fox jumps over the lazy dog.'
# Searched words : 'fox'
def twenty():
    pattern = 'fox'
    text = 'The quick brown fox jumps over the lazy dog.'
    match = re.search(pattern, text)
    s = match.start()
    e = match.end()
    print('Found "%s" in "%s" from %d to %d ' % (match.re.pattern, match.string, s, e))
    return "\n"


one()
two()
three()
four()
five()
six()
seven()
eight()
nine()
ten()
eleven()
twelve()
thirteen()
fourteen()
fifteen()
sixteen()
seventeen()
eighteen()
nineteen()
twenty()
