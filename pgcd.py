def pgcd(a,b):
    if(a>b):
        x = a
        y = b
    else:
        x = b
        y = a
    while(x%y != 0):
        r = x % y
        x = y
        y = r
    print("le pgcd de",a,"et",b,"est = ",y)

pgcd(1938,836)
pgcd(378,182)