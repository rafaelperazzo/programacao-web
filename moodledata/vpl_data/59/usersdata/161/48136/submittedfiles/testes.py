n=float(input('numero:'))
n=int(n)
a=float(input('a'))
a=int(a)
cont=0
i=a
cos=math.cos
for i in range (n,a+1,1):
    if math.cos(i)-math.exp(i)<0:
        cont=cont+1
        i=i+0.01
    if cont==0:
        print('sim')
 
   