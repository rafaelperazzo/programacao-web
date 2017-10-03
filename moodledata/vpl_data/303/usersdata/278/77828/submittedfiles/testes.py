h = float(input("Digite sua altura: "))
s = str(input("Você é do sexo? "))
if s=="feminino":
    pi = (72.7*h)-58
    print("%.2f" %(pi))
if s=="masculino":
    pi = (62.1*h)-44.7
    print("%.2f" %(pi))