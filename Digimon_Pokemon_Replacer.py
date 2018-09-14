from random import *

input_file = open('input')
input_str = input_file.readlines()

def makeAwesome(listOfStrings):
    output = ""
    for string in listOfStrings:
      for word in string.split(" "):
        randNum = randint(0,3)
        if word.startswith("Pokemon"):
          word = "Digimon"
        elif word.startswith("POKEMON"):
          word = "DIGIMON"
        elif word.startswith("catch"):
          word = "digitize"
        
        if randNum == 1 and word != "\n":
          word = word.upper() + word[-1] * 5

        output += word + " "
        
    return output

print makeAwesome(input_str)
