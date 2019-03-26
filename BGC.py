#Decimal to binary function
def dToB(dec):
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
        binary.append(str(base2))
        if quotient==0:
            break
    
    #Reverses list because the remainders have to be written in reverse order from when they were found to be correct
    binary.reverse()

    if len(binary) < 4:
        for _ in range(4 - len(binary)):
            binary.insert(0, "0")

    #Prints the binary representation
    s = ""
    
    return s.join(binary)

#Binary to decimal function
def bToD(binary):
    #Makes each bit an item in a list in order to multiply its position by its respective power of 2
    binary = str(binary)
    binary = [int(i) for i in binary]

    #Reverses list of bits because it makes it easier for the upcoming loop
    binary.reverse()

    #Sets up the decimal number that will be printed out
    decimal = 0

    #Loops over every bit and multiplies the bit by its respective power of two then adds the product to the decimal variable
    for i in range(len(binary)):
        decimal += (binary[i] * (2**i))

    #Prints the decimal representation of the entered binary number
    return decimal

def hToB(hexadecimal):
    hexadecimal = [i for i in hexadecimal]

    binary = ""
    conversion = {"0":dToB(0), "1":dToB(1), "2":dToB(2), "3":dToB(3), "4":dToB(4), "5": dToB(5), "6":dToB(6), "7":dToB(7), "8":dToB(8), "9":dToB(9), "A":dToB(10), "B":dToB(11), "C":dToB(12), "D":dToB(13), "E":dToB(14), "F":dToB(15)}
    for num in hexadecimal:
        binary += str(conversion[num])

    return binary

#Calls functions
#print(dToB(7))
#print(0)
print(hToB("555ABC070"))