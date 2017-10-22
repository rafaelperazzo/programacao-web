x=int(input(''))
cont=0
while x<0:
    x=int(input(''))
for i in range(x,0,-1):
    x=x-1
    i*=x
print(i)
    