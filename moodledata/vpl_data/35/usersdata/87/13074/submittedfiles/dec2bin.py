p = int(input("Digite valor de p: "))
q = int(input("Digite valor de q: "))

i=1
while i<=p:
    i=i*10
while q>=p:
    s=q%i
    q=s/10
if s==p:
    print("S")
else:
    print("N")