def conversion():
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



conversion()
