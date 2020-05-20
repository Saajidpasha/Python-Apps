import json
from difflib import get_close_matches
data = json.load(open("076 data.json"))#loading the json file into a dictionary variable
def translate(word):
    word = word.lower()
     #converts any case letters to lower case
    if word in data:#if the word is present in dictionary then will return its defintiion
        return data[word]
    #if the word is related like rainn then closest word is returned
    elif len(get_close_matches(word,data.keys())) > 0 :#use to get closest match for the string rainn

        yn = input( "Did you mean %s instead press Y or N " % get_close_matches(word,data.keys())[0])
        if yn == 'Y' or yn == 'y' :
            return data[get_close_matches(word,data.keys())[0]]
        elif yn == 'N' or yn == 'n':
            return "The word doesnt exist please cheeck it again."
        else:
            return "Please enter a valid option."

    else:
        return "The word Doesnt exist in the dictionary"

#word = input("\nenter a word ")
#output = translate(word)
"""if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)"""
