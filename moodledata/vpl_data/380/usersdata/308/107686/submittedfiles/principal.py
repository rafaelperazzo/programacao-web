def converterDecimal(valor):
    resultado = 0
    expoente = len(valor)
    for i in valor[::-1]:
        resultado += int(i)**(len(valor)-expoente)
        print(int(i)**(expoente))
        expoente -= 1 
    return resultado

print(converterDecimal('1011'))

