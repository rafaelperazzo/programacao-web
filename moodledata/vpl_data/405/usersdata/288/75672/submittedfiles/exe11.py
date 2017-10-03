n=int(input("Digite um numero inteiro: "))
if  0<(n//10000000)<=1:
    a=(n//10000000)
    b=(n%10000000)/1000000
    c=(b%1000000)/100000
    d=(c%100000)/10000
    e=(d%10000)/1000
    f=(e%1000)/100
    g=(f%100)/10
    h=(g%10)/1
   
    print (n)
    print (a+b+c+d+e+f+g+h)
    
else: print ("Nao sei")    
    

