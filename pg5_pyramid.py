def pyramid():
    n=int(input("Enter a value "))
    for i in range (0,n+1):
        
        a=0
        for j in range(i):
            a=a+i
            print(a,end=" ")
            
        print(" ")


pyramid()
