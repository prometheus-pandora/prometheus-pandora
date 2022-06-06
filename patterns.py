# Pattern Dictionary --> Contains different patterns that Pandora can use to understand Natural Language
# Created by Jefferson Enriquez-Garcia Jr.

# Dictionary that stores different patterns for re.search()
patterns = {}   

# Each item in the dictionary is a pattern
# Each item in the dictionary has a name which specifies its category
# The category format is as follows: [TAG.TYPE]
# [TAG] --> There are two possible tags, s (simple) or c (complex)
# [.] --> Seperator for TAGs and TYPEs
# [TYPE] --> Multiple TYPEs of patterns are possible, which helps Pandora understand the topic

# ------------------------------------------------------------------------------------------------------------------------------

# Greeting search patterns --> Could we find a way to expand this?
patterns["greeting"] = r"(\bhello\b)|(\bhi\b)|(\bgreetings\b)"

# Farewell search patterns --> expand?
patterns["farewell"] = r"(\bgoodbye\b)|(\bbye\b)|(\bfarewell\b)"

# Affirmation search patterns
patterns["affirmation"] = r"(\baffirmative\b)|(\byes\b)|(\byep\b)|(\byeah\b)"

# Rejection search patterns
patterns["rejection"] = r"(\bnegative\b)|(\bno\b)|(\bnope\b)|(\bnah\b)"

patterns["what is _"] = r"what is ([a-z]+)[?]?"

patterns["what are _"] = r"what are ([a-z]+)[?]?"

