n1 = float (input("Digite a primeira nota "))
if n1<=5:
    print("Estude mais")
while n1>10:
    print("erro")
    n1 = float (input("Digite a primeira nota novamente "))
n2 = float (input("Digite a segunda nota "))
while n2>10:
    print("erro")
    n2 = float (input("Digite a primeira nota novamente "))
n3 = float (input("Digite a terceira nota "))

while n3>10:
    print("erro")
    n3 = float (input("Digite a primeira nota novamente "))
total = (n1+n2+n3)
print(total)

media = (total/3)
print ('sua média é = ', media)




