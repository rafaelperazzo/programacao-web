# -*- coding: utf-8 -*-

#Criação da classe "Number", do qual serão criados os meus objetos número p e q
class Number(object):
    def __init__(self, num, num_dig):
        self.num = num
        self.num_dig = num_dig
        
    def verificaValidade(self, num_p, num_q):
        self.num_p = num_p
        self.num_q = num_q
        while True:
            if len(str(self.num_p)) < len(str(self.num_q)):
                break
            print("\nO número de dígitos de p não é menor do que o de q!\n")
            self.num_p = int(input("Digite novamente p: "))
            self.num_q = int(input("Digite novamente q: "))
            
    def subnum(self, num__p, num__q):
        self.num__p = str(num__p)
        self.num__q = str(num__q)
        if self.num__p in self.num__q:
            print("S")
        else:
            print("N")
            
#O programa principal inicia aqui
pnum = int(input("Digite o número p: "))
qnum = int(input("Digite o número q: "))

_p = Number(pnum, len(str(pnum)))
_q = Number(qnum, len(str(qnum)))

_p.verificaValidade(_p.num, _q.num)

p = Number(_p.num_p, len(str(_p.num_p)))
q = Number(_p.num_q, len(str(_p.num_q)))

p.subnum(p.num, q.num)