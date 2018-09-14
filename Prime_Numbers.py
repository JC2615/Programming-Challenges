numbers = []
global count 
count = 0

def allPrime():
  for num in range(1, 101, 1):
    isPrime(num)


def isPrime(num):
  for number in range(2, num, 1):
    if number < num and num % number == 0:
      return False
  print num

allPrime()
