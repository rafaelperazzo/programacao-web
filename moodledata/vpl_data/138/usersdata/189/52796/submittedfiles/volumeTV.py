n=int(input('Volume inicial:'))
m=int(input('Mudança de volume:'))
for i in range(1,m+1,1):
    t=int(input('Alteração do volume:'))
    t=n-t+t
print(t)