n1 = float (input("Digite a primeira nota "))

while n1>10:
    print("erro")
    n1 = float (input("Digite a primeira nota novamente "))
if n1<=7:
    print("Estude mais")
elif n1<10:
    print("Muito bem")
else:
    print("Parabéns")
    
n2 = float (input("Digite a segunda nota "))
while n2>10:
    print("erro")
    n2 = float (input("Digite a primeira nota novamente "))
    if n2<=7:
    print("Estude mais")
elif n2<10:
    print("Muito bem")
else:
    print("Parabéns")
n3 = float (input("Digite a terceira nota "))

while n3>10:
    print("erro")
    n3 = float (input("Digite a primeira nota novamente "))
    if n3<=7:
    print("Estude mais")
elif n3<10:
    print("Muito bem")
else:
    print("Parabéns")
total = (n1+n2+n3)
print(total)

media = (total/3)
print ('sua média é = ', media)




