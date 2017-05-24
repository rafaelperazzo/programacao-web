n=int(input('numero:'))
soma=0
den=1
for i in range(1,n+1,1):
    if i%2!=0:
        soma=soma+(4/den)
    else:
        soma=soma-(4/den)
    den=den+2    
print('%.4f' %soma)    
   