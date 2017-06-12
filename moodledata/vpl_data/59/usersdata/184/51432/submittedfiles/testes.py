n=int(input('digite n:'))
a1=1
a2=1
for i in range(3,n+1,1):
    próximo=a1+a2
    a1=a2
    a2=próximo
print(próximo)