# Spellchecker
# Created by Jefferson Enriquez-Garcia Jr.


# Helper function for spellchecker()
# tokenize() --> Reads a string's contents, returns a list where each item is a word
def tokenize(sent):
    upper_to_lower = sent.lower()           # Converts all the characters in the string to lowercase (for formatting)
    str_to_list = upper_to_lower.split()    # Creates a list where each item is a word from the string

    return str_to_list


# Helper function for min_edit()
# sub_cost() --> Given two characters, returns the cost of substitution (0 if same letter, 2 if not)
def sub_cost(source, target):
    if source == target:
        return 0
    else:
        return 2


# Helper function for suggest()
# min_edit() --> Returns the minimum distance between two strings (source and target) using the Levenshtein distance algorithm
def min_edit(source, target):
    n = len(source)                                 # Finds length of "source" string (needed for loop)
    m = len(target)                                 # Finds length of "target" string (needed for loop)
    distance = [[0] * (m+1) for i in range(n+1)]    # Creates a list (distance[m+1][n+1]) using list comprehension
    
    # Initialization
    distance[0][0] = 0                                                                      # Distance from the empty string
    for i in range(1, n+1):
        distance[i][0] = distance[i-1][0] + 1                                               # Deletion cost
    for j in range(1, m+1):
        distance[0][j] = distance[0][j-1] + 1                                               # Insertion cost
    
    # Reccurence
    for i in range(1, n+1):
        for j in range(1, m+1):
            distance[i][j] = min(distance[i-1][j] + 1,                                      # Deletion cost
                                distance[i-1][j-1] + sub_cost(source[i-1], target[j-1]),    # Substitution cost
                                distance[i][j-1] + 1)                                       # Insertion cost

    # Termination (returns the min distance between the source and target)
    return distance[n][m]


# Helper function for spellchecker()
# suggest() --> Given an incorrectly spelled word, returns a list of 3 words with the least edit distance 
def suggest(misspelled_word):
    #words = open("words")                               # Open the "words" file, which contains a huge list of correctly spelled words
    words = open("words_modified")                      # Modified "words" file

    possible_corrections = {}                           # words that will store 
    misspelled_word_len = len(misspelled_word)          # Find the length of the misspelled word (needed for min_edit())

    for word in words:                                  # Check every correctly spelled word in "words"
        word = word[:-1]                                # Cutoff the "\n" from the current word because it isn't neccessary
        word_len = len(word)                            # Find the length of the current word

        # Check if a word in "words" is either +1,-1, or 0 characters longer than the misspelled word
        if (word_len == (misspelled_word_len + 1)) or (word_len == (misspelled_word_len - 1)) or (word_len == misspelled_word_len):
            pass
        else:
            continue

        # Check if the misspelled word has a size greater than or equal to 2
        if misspelled_word_len >= 2:
            pass
        else:
            continue

        # Compare the first and last characters of the misspelled word and correctly-spelled word
        if misspelled_word[0] == word[0] or misspelled_word[-1] == word[-1]:
            dist = min_edit(misspelled_word, word)      # Find the distance between the misspelled word and correctly-spelled word
            possible_corrections[word] = dist           # Add the correctly-spelled word to a list of possible corrections

    words.close()

    # Lambda function; Return a list, where each item is a tuple (correctly-spelled word, distance) arranged in ascending order
    sort_possible_corrections = sorted(possible_corrections.items(), key=lambda x: x[1])
    
    # First Possible Spelling for the Incorrectly-Spelled Word
    first_word = sort_possible_corrections[0][0]
    # second_word = sort_possible_corrections[1][0]
    # third_word = sort_possible_corrections[2][0]
    # fourth_word = sort_possible_corrections[3][0]

    return first_word


# Helper function for spellchecker()
# correctly_spelled() --> Checks to see if a word is in "words". Returns True if a word is in "words"
def is_correctly_spelled(word_to_check):
    #words = open("words")                   # Opens the "words" file, which containts a huge list of correctly spelled words
    words = open("words_modified")          # Modified "words" file

    for word in words:                      # Compare each word in the words to the input word
        if word_to_check == word[:-1]:      # If the input word is found in the words, then it is correctly spelled
            words.close()
            return True

    words.close()
    return False                            # If the input word is NOT in the words, then it is misspelled


# spellchecker() --> Check if the given string is correctly spelled. If it is not, return a corrected string.
def spellchecker(sent):
    sentence = tokenize(sent)                               # Turns string into list of words
    corrected_sentence_list = []                            # Copy of "sentence" list, where each item is a correctly-spelled word
    
    for word in sentence:                                   # ...
        if is_correctly_spelled(word):                      # ...
            corrected_sentence_list.append(word)            # ...
        else:
            corrected_sentence_list.append(suggest(word))   # ...

    corrected_sentence = " ".join(corrected_sentence_list)  # ...

    return corrected_sentence


# python3 spellchecker.py
# print(spellchecker("nope"))
