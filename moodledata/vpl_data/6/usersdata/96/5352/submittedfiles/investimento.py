# -*- coding: utf-8 -*-
from __future__ import division

# -*- coding: utf-8 -*-
from __future__ import division

ValorInvestimento = input('Digite o valor do investimento:')
Taxa = input('Digite o valor da taxa de crescimento:')

SaldoAno1 = ValorInvestimento + (ValorInvestimento*(Taxa/100))
SaldoAno2 = SaldoAno1 + (SaldoAno1*(Taxa/100))
SaldoAno3 = SaldoAno2 + (SaldoAno2*(Taxa/100))
SaldoAno4 = SaldoAno3 + (SaldoAno3*(Taxa/100))
SaldoAno5 = SaldoAno4 + (SaldoAno4*(Taxa/100))
SaldoAno6 = SaldoAno5 + (SaldoAno5*(Taxa/100))
SaldoAno7 = SaldoAno6 + (SaldoAno6*(Taxa/100))
SaldoAno8 = SaldoAno7 + (SaldoAno7*(Taxa/100))
SaldoAno9 = SaldoAno8 + (SaldoAno8*(Taxa/100))
SaldoAno10 = SaldoAno9 + (SaldoAno9*(Taxa/100))

print('O saldo do ano 1 é: %.2f' %SaldoAno1)
print('O saldo do ano 2 é: %.2f' %SaldoAno2)
print('O saldo do ano 3 é: %.2f' %SaldoAno3)
print('O saldo do ano 4 é: %.2f' %SaldoAno4)
print('O saldo do ano 5 é: %.2f' %SaldoAno5)
print('O saldo do ano 6 é: %.2f' %SaldoAno6)
print('O saldo do ano 7 é: %.2f' %SaldoAno7)
print('O saldo do ano 8 é: %.2f' %SaldoAno8)
print('O saldo do ano 9 é: %.2f' %SaldoAno9)
print('O saldo do ano 10 é: %.2f' %SaldoAno10)