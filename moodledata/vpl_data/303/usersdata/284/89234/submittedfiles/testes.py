x=int(input('digite o valor: '))
def divisor(x):
    for n in range(1,x+1,1):
        if (x%n==0):
            z=n
            n=n+1
    return(z)    

    
        
