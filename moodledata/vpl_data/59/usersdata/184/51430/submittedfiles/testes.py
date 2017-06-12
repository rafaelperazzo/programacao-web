n=int(input('digite n:'))
denominador=1
termo=2
pi=1
for i in range(1,n+1,1):
    pi=pi*termo/denominador
    if termo>denominador:
        denominador=denominador+2
    else:
        numerador=numerador+2
    pi=pi*2
    print(pi)