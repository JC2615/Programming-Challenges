from random import *

part1 = [
  "You may not believe this but, ",
  "Believe it or not, ",
  "In all seriousness, ",
  "This might sound crazy, but ",
  "I swear I'm telling the truth: ",
  "I totally did it, buuut "
]

part2 = [
  "I was kidnapped by ",
  "my homework was eaten by ",
  "it was stolen then incinerated by ",
  "I was forcibly enrolled in a secret military training program run by ",
  "the government of Atlantis had me draft a new constitution, as I was constantly watched by ",
  "I was brain swapped with ",
  "I mistakenly opened up a wormhole and when I returned, it was sliced into pieces by ",
  "I singlehandedly overthrew the government of a small nation last night with the help of ",
  "the Italian Mafia called in a favor. Let's just say it did not please ",
  "I was invited to the birthday party of ",
  "Oprah wanted me to race ",
  "the Moon fell out of the sky and I had to put it back with ",
  "I died a horrible death, but was revived just this morning by "
]

part3 = [
  "ninjas",
  "a three-headed rabbit",
  "Ryan Reynolds",
  "the Big Man himself. Who you believe the Big Man to be, is entirely up to you",
  "sneezing trapeze artists",
  "a sentient violin",
  "a jelly-filled donut",
  "the principal",
  "Deadpool",
  "Eminem",
  "the very piece of homework you assigned",
  "John Cena",
  "Han Solo",
  "Kevin",
  "Francesca"
]

print("Where's your homework?")
print("")
for num in range(1, 11, 1):
  factor = randint(0, 1)
  if num == 1:
    print("I've got ten excus- I mean, reasons for you.")
    print("")

  if (factor == 0):
   print(str(num) + ". " + choice(part1) + choice(part2) + choice(part3) + " and " + choice(part3) + "!")
   print("")
  else:
    print(str(num) + ". " + choice(part1) + choice(part2) + choice(part3) + "!")
    print("")
