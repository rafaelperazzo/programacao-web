x=int(input(''))
cont=0
while x<0:
    x=int(input(''))
f=1
for i in range(1,x+1,1):
    f*=i
print('%d'%f)
    