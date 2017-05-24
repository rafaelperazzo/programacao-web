a=int(input('numero:'))
s=0
for i in range(1,a,1):
   if a%i==0:
       s=s+1
    if s==a:
        print('s')
    else:
        print('n')