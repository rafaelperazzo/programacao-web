a=input('digite a:')
b=input('digite b:')
q=input('digite q:')
c=0
i=2
while i<=q:
    if a%i==0 and b%i==0:
        c=c+1
    i=i+1
print (c)