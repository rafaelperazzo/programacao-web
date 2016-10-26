n=int(input("digite numero na base binaria:"))

i=0
j=1
while n!=0:
    i=i+n%10*j
    n=n//10
    j=j*2
print("%d"%i)