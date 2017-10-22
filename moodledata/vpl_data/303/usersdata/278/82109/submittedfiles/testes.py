while (True):
    x = int(input("Digite um número no intervalo [1,13]: "))
    if x>=1 and x<=13:
        print("%.d" %(x))
        break
    else:
        print("O número não está entre [1,13].")
        print("Pfvr tente novamente!")
    