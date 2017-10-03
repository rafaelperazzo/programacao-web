int(input("Digite sua idade:"))

n=idade
if 0<n<=12:
    print("criança")
if 12<n<=16:
    print("adolescente")
if 16<n<=60:
    print("adulto")
else:
    print("idoso")