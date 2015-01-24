nr1 = int(input("Sláðu inn tölu 1: "))
nr2 = int(input("Sláðu inn tölu 2: "))
def summa(x, y):
    while y:
        x, y = y, x%y
    return x
swag = summa(nr1,nr2)
print ("Stærsti sameiginlegi þáttur ",nr1," og ",nr2," er ",swag)
 