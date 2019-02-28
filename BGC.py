#Decimal to binary function
def dToB():
    dec = int(input("Enter a decimal number to be converted into binary: "))

    #Instantiate a list to store the binary numbers
    binary = []

    #Sets up quotient and remainder to use
    quotient = 0
    base2 = 0

    #Divides by 2 until quotient equals 0 and adds the remainders to the binary list
    while (True):
        quotient = dec // 2
        base2 = dec % 2
        dec = quotient
        binary.append(base2)
        if quotient==0:
            break
    
    #Reverses list because the remainders have to be written in reverse order from when they were found to be correct
    binary.reverse()

    #Prints the binary representation
    for num in binary:
        print(num, end = '')

#Binary to decimal function
def bToD():
    binary = input("\nEnter a binary number to be converted into decimal: ")
    
    #Makes each bit an item in a list in order to multiply its position by its respective power of 2
    binary = [int(i) for i in binary]

    #Reverses list of bits because it makes it easier for the upcoming loop
    binary.reverse()

    #Sets up the decimal number that will be printed out
    decimal = 0

    #Loops over every bit and multiplies the bit by its respective power of two then adds the product to the decimal variable
    for i in range(len(binary)):
        decimal += (binary[i] * (2**i))

    #Prints the decimal representation of the entered binary number
    print(decimal)

#Calls functions
dToB()
bToD()