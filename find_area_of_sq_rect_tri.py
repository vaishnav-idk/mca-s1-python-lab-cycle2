def area():
    n=int(input("enter the length of square side "))
    x=lambda a: a*a
    print(x(n))
    l=int(input("enter the length of rectangle  "))
    b=int(input("enter the breadth of rectangle  "))
    ar=lambda m,n: m*n
    print(ar(l,b))
    l=int(input("enter the heigth  of triangle  "))
    b=int(input("enter the base of triangle  "))
    ar=lambda r,h:0.5*r*h
    print(ar(l,b))
    
area()
