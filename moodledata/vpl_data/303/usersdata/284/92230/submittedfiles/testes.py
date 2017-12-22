n=int(input('digite o numero de elementos : '))
a=[]
for i in range(0,n,1):
    a.append(int(input('digite um valor: ')))
    soma=(a[i]**2)
    for i in range(1,n,1):
        soma=soma+(a[i]**2)
        print(soma)




            
        

    
        
