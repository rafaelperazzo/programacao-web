h = float(input("Digite sua altura: "))
s = bool(input("Você é do sexo feminino? (sim: true; não: false) "))
if s=="sim":
    pi = (72.7*h)-58
    print("%.2f" %(pi))
if s=="não":
    pi = (62.1*h)-44.7
    print("%.2f" %(pi))