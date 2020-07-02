
print("Enter The Type OF Data")

a = "b"
b = "d"
c = "o"
d = "h"
e = "a"

def binary():
    print("This Is Binary Coversion")
    inb = int(input("Enter The Binary Code: "))
    string_bin = str(inb)
    deco = int(string_bin,2)
    print("Decimal: "+str(deco))
    print("Hex: " + str(hex(deco)))
    print("Octal: " + str(oct(deco)))
    print("ASCII: " + str(chr(deco)))

def decimal():
    print("This Is Decimal Conversion")
    ind = int(input("Enter The Decimal Code: "))
    print("Binary: "+str(bin(ind)))
    print("Hex: " + str(hex(ind)))
    print("Octal: " + str(oct(ind)))
    print("ASCII: " + str(chr(ind)))

def octal():
    print("This Is Octal Conversion")
    ino = int(input("Enter The Octal Code: "))
    deco = int(str(ino), 8)
    print("Binary: " + str(bin(deco)))
    print("Decimal: " + str(deco))
    print("Hex: " + str(hex(deco)))
    print("ASCII: " + str(chr(deco)))

def hexa():
    print("This Is Hex Conversion")
    inx = input("Enter The Hex Code: ")
    deco = int(str(inx), 16)
    print("Binary: " + str(bin(deco)))
    print("Decimal: " + str(deco))
    print("Octal: "+ str(oct(deco)))
    print("ASCII: " + str(chr(deco)))

def Ascii():
    print("This Is ASCII Conversion")
    ina = input("Enter The ASCII Code: ")
    deco = ord(ina)
    print("Binary: " + str(bin(deco)))
    print("Decimal: " + str(deco))
    print("Ocatl: " + str(oct(deco)))
    print("Hex: " + str(hex(deco)))



while(True):

    f = input("Enter\n b for Binary\n d for Decimal\n h for Hex\n o for Octal\n a for ASCII\n x for Exit\n")

    
    if f == a:
        binary()

    elif f == b:
        decimal()

    elif f == c:
        octal()
    elif f == d:
        hexa()

    elif f == e:
        Ascii()
    elif (f == "X" or "x"):
        exit()