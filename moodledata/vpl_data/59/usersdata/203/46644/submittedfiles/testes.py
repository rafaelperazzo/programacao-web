n1=int(input('digite primeiro: '))
n2=int(input('digite segundo: '))
for i in range (1,n1+1,1):
    if n1%i==0 and n2%i==0:
        mdc=i
print(mdc)