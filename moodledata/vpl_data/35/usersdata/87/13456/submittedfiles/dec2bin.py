p = int(input("Digite valor de p: "))
q = int(input("Digite valor de q: "))

i=0
a=p
while p>0:
    p=p//10
    i=i+1
p=a
j=0
while q>0:
    w=q%(10**i)
    if w==p:
        j=j+1
        break
    else:
        q=q//10
        
if j==0:
    print("N")
else:
    print("S")