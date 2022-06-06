import time

# The human class; Contains various attributes associated with humans; can expand
class Human:
    def __init__(self):
        
        # Dictionary that hold information about a specific human
        self.info = {}


        # Personal identification Information   -------------------------------------------------------------------------------------

        # Personal Information Dictionary
        self.info["personal"] = {}

        # Dictionary that holds name information
        self.info["personal"]["name"] = {"full_name": "", 
                                         "first_name": "", 
                                         "last_name": ""}

        # Dictionary that holds age information
        self.info["personal"]["birthdate"] = {"month":0, 
                                              "day":0, 
                                              "year":0, 
                                              "age":0}

        # Dictionary that holds sex information
        self.info["personal"]["sex"] = {"sex":""}

        # Dictionary that holds pronoun information
        self.info["personal"]["pronoun"] = {"first_person_singular":"I",
                                            "second_person_singular": "you",
                                            "third_person_singular": "they",
                                            "third_person_singular_neuter": "it",
                                            "first_person_plural":"we",
                                            "second_person_plural": "you",
                                            "third_person_plural": "they"}


        # Family Information    -----------------------------------------------------------------------------------------------------

        # Family Information Dictionary
        self.info["family"] = {}

        # Dictionary that holds parent information
        self.info["family"]["parents"] = {"parent_1": None,
                                          "parent_2": None}
        
        # Dictionary that holds sibling information
        self.info["family"]["siblings"] = {"sibling": None}

        # Dictionary that holds children information
        self.info["family"]["children"] = {}


        # Hobby Information     -----------------------------------------------------------------------------------------------------

        self.info["hobbies"] = {}

    # set_name() --> ...
    def set_name(name):
        return 0

    # set_birthdate() --> ...
    def set_birthdate(birthdate):
        return 0

    # set_birthdate() --> ...
    def set_sex(sex):
        return 0

    # set_pronoun() --> ...
    def set_pronoun():
        return 0

    # set_family() --> ...
    def set_family():
        return 0

    


