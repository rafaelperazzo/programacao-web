while True:
a=int(input('a:'))
if a>0:
    break
while a>=1:
    i=a//10
    r=a%10
    soma=soma+r
    a=a//10