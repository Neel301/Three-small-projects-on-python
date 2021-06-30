import json
# To get close matches
from difflib import get_close_matches

data = json.load(open("data.json"))
# this is for when your search word is exist:
def translate(word):
# First convert all the letter in to the lower case, So if you forgot to do upper case in some words, get the output with this method.
    word = word.lower()
    if word in data:
        return data[word]
# This is for the word whom starting word is capitala.
    elif word.title() in data:
        return data[word.title()]
# when enter the upper case word, do not get error with this method.
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word , data.keys())) > 0:
        print("Did you mean %s instead" %get_close_matches(word, data.keys())[0])
        decide = input("press y for yes or n for no")
        if decide == "y":
            return data[get_close_matches(word , data.keys())[0]]
        elif decide == "n":
            return("pugger your paw steps on wrong keys")
        else:
            return("You have entered wronge input Please enter just y or n")
    else:
        print("You have entered the Wrong word")
# this is when you have entered the wrong word
word = input("Enter the word you want to search")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
