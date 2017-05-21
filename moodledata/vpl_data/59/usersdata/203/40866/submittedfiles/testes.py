for i in range (1000,10000,1):
    al1=i//100
    al2=i%100
    if i**(1/2)==al1+al2:
        print(i)