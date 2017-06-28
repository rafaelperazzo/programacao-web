a=int(input('digite a:'))
b=int(input('digite b:'))
q=int(input('digite q:'))
c=0
i=2
while i<=q:
    if a%i==0 and b%i==0:
        c=c+i
    i=i+1
print(c)