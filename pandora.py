# Artificial Intelligence ChatBot "Pandora"
# Created by Jefferson Enriquez-Garcia Jr.
import re
from random import choice
from spellchecker import spellchecker
from patterns import patterns
from replies import replies
from entities import Human



# Pandora -->
class Pandora:

    # __init__() --> 
    def __init__(self):

        # ...
        self.information = Human()
        self.run = True

        # Dictionary that stores different patterns for re.search()
        self.patterns = patterns

        
        # Dictionary that stores different replies
        self.replies = replies


    # Helper Function for conversation()
    # find_pattern() --> Looks for a pattern in text, and returns a list [pattern name, match object] if pattern was found
    def find_pattern(self, text):
        pat_mat = []                                        # List that holds two items: pattern name; match object
        
        for pat in self.patterns:                           # Loops through all possible patterns
            mat = re.search(self.patterns[pat], text)       # Search for the current pattern in the text (stores result in mat)
            if mat:                                         # If a match was found (match == True) then
                pat_mat = [pat, mat]                        # Append the pattern name and match object as a tuple

        return pat_mat

    
    # Helper Function for find_reply()
    # find_groups() --> Takes a match object, returns a copy of the match groups without "None" (e.g. ["one", None] --> ["one"])
    def find_groups(self, mat):
        mat_group = mat.groups()            # mat_group --> Extract the match groups within the match object, store as tuple
        new_group = []

        for item in mat_group:              # Loop through the match groups
            if item != None:                # If a match group is not "None",
                new_group.append(item)      # Append the match group into the the new list

        return new_group


    # Helper Function for conversation()
    # find_reply() --> Takes a list [pattern name, match object], prints a reply
    def find_reply(self, pat_mat):
        if pat_mat != []:                               # First, check if a pattern was found
            pat = pat_mat[0]                            # Pattern Type (used to find search an appropriate response)
            mat = pat_mat[1]                            # Match Object (This contains the match groups)
            groups = self.find_groups(mat)              # List containing the match groups found within the match object

            msg_recieved = self.patterns[pat]           # This is the messge recieved from the user
            msg_to_send = choice(self.replies[pat])     # "Mad Libs" message for Pandora
            substitution = mat.group(0)                 # This is the message that Pandora replies with


            reply = re.sub(msg_recieved, msg_to_send, substitution)     # This is where the "Mad Libs" substitution takes place

            print(reply)                                # Pandora replies


        return 0


    # conversation() --> Allows Pandora to converse with a user
    def conversation(self):
        text = input(">> ")                 # Asks user for input, which Pandora will read and reply to
        text = spellchecker(text)           # Spellcheck the input, and correct for any mistakes
        
        pat_mat = self.find_pattern(text)   # Searches for patterns in the given text, and returns a list of match objects

        self.find_reply(pat_mat)            # Prints out an appropriate response, given the [pattern name, match object] list
        
    

# python3 pandora.py
def main():
    daughter = Pandora()            # Creates the entity "Pandora"
    daughter.conversation()         # conversation() --> "Pandora" class method that allows user to converse with A.I. using NLP



if __name__ == "__main__":
    main()