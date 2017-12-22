def converterDecimal(valor):
    resultado = 0
    expoente = len(valor)
    for i in range (len(valor)-1, -1, -1):
        resultado += int(valor[i])**(expoente)
        expoente -= 1 
    return resultado

print(converterDecimal('1011'))

