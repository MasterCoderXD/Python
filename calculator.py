def calculate():
    d = int(0)
    x = input("num 1? ")
    y = input("num 2? ")
    z = int(x)
    za = int(y)
    command = input(
        "which function \nm=multiply\n d=divide \n s=subtract \n a=addition \n e=exponent \n"
    )
    if command == "m":
        d = int(z * za)
        print(d)

    elif command == "s":
        d = z - za
        print(d)

    elif command == "a":
        d = z + za
        print(d)

    elif command == "d":
        d = z / za
        print(d)

    elif command == "e":
        d = z**za
        print(d)
