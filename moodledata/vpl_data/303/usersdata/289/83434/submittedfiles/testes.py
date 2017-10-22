while(true):
    while(true):
        n = int(input("Digite um número: "))
        if (n>=0):
            break
    f = 1 
    for i in range (2,n+1,1):
        f*=i
        print("%d! = %d" % (n,f))
        
    
    