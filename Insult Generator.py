import random

input("Welcome to Insult Generator v1.0. Press enter to generate an insult. ")

part1 = ["Shut up, you ", "Sit down, you ", "You're a ", "This is the best way I could describe you: a "]

part2 = ["stupid ", "not so pretty ", "rotten ", "sickening ", "wonderful ", "dimwitted ", "maniacal ",
         "withering ", "hollow shell of a ", "dog hating ", "global warming loving "]

part3 = ["pig.", "rat.", "washboard.", "individual.",
         "capitalist.", "Nazi.", "socialist.", "monster.", "dictator.", "waste of space."]

while True:
    print("\n" + random.choice(part1) + random.choice(part2) + random.choice(part3))

    play_again = input("\nWanna play again? (Y/N): ").lower()
    if play_again == "y":
        continue
    elif play_again == "n":
        break
    else:
        print("'%s' is an invalid answer. Since you lack the ability to follow instructions, Insult Generator will shut "
              "down." % play_again)
        break
