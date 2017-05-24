n=int(input('numero:'))
soma=0
den=1
num=1
for i in range(1,n+1,1):
    if i%2!=0:
        soma=soma+(num/den)
    else:
        soma=soma-(num/den)
    num=num+1
    den=num**2    
print('%.4f' %soma)    
   