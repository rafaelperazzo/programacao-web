def conta_digitos (n):
    cont=1
    while(n//10>0):
        n=n//10
        cont+=1
    return cont
print(conta_digitos(8))
        
print(conta_digitos(999999999999999999999))

        

    
        
        
    