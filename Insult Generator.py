from random import *

part1 = {1: "Shut up, you ", 2:"Sit down, you ", 3: "You're a ", 4: "This is the best way I could describe you: a "}

part2 = {1: "stupid ", 2: "not so pretty ", 3: "rotten ", 4: "sickening ", 5: "wonderful ", 6: "dimwitted ", 7: "maniacal ",
         8: "withering ", 9: "hollow shell of a ", 10: "dog hating ", 11: "global warming loving "}

part3 = {1: "pig.", 2: "rat.", 3: "washboard.", 4: "individual.",
         5: "capitalist.", 6: "Nazi.", 7: "socialist.", 8: "monster.", 9: "dictator.", 10: "waste of space."}

while True:

    numGen = int(input("Welcome to Insult Generator v1.0. Enter the amount of insults you'd like to generate: "))

    for i in range(numGen):
        p1 = randint(1,4)
        p2 = randint(1,11)
        p3 = randint(1,10)

        print("\n" + part1[p1] + part2[p2] + part3[p3])
    
    play_again = input("\nWanna play again? (Y/N): ").lower()
    if play_again == "y":
        continue
    elif play_again == "n":
        break
    else:
        print("'%s' is an invalid answer. Since you lack the ability to follow instructions, Insult Generator v2.0 will shut "
              "down." % play_again)
        break