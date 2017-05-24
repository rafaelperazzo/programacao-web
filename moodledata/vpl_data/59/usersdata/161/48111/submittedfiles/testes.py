a=int(input('numero:'))
a1=1
a2=1
for i in range(3,a+1,1):
   proximo=a1+a2
   a1=a2
   a2=proximo
print(proximo)   
   