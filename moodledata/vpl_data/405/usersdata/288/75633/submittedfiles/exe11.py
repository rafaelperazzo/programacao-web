n=int(input("Digite um numero inteiro: "))
if  0<(n//10000000)<=1:
    a=(n//10000000)
    b=(n%1000000)
    c=(b%100000)
    d=(c%10000)
    e=(d%1000)
    f=(e%100)
    g=(f%10)
    h=(g%1)
   
    print (n)
    print (a+b+c+d+e+f+g+h)
    
else: print ("Nao sei")    
    

