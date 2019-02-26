def dToB():
    dec = int(input("Enter a decimal number to be converted into binary: "))
    binary = []
    quotient = 0
    base2 = 0
    while (True):
        quotient = dec // 2
        base2 = dec % 2
        dec = quotient
        binary.append(base2)
        if quotient==0:
            break
    binary.reverse()
    for num in binary:
        print(num, end = '')

def bToD():
    binary = input("\nEnter a binary number to be converted into decimal: ")
    binary = [int(i) for i in binary]
    binary.reverse()
    decimal = 0
    for i in range(len(binary)):
        decimal += (binary[i] * (2**i))
    print(decimal)

dToB()
bToD()