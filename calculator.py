calculate();
def calculate():
  d=int(0);
  x = input("num 1? ");
  y = input("num 2? ");
  z =int(x);
  za=int(y);
  command=input("which function \n m=multiply\n d=divide \n s=subtract \n a=addition: ");
  if command=="m":
    d=int(z*za);
    print(d);

  elif command=="s":
    d = z-za;
    print(d);

  elif command=="a":
    d=z+za;
    print(d);

  elif command =="d":
    d=z/za;
    print(d);
