# -*- coding: utf-8 -*-
def calculo do IMC(P, A)
     if P/(A*A)<20:
        print "\nSeu IMC=%f você está abaixo do peso" % (P/(A*A))
    
    elifP/(A*A)>=20 and P/(A*A)/<=25:
        print "\nSeu IMC=%f você está no peso ideal" % (P/(A*A))
    
    elifP/(A*A)>=25 and P/(A*A)/<=30:
        print "\nSeu IMC=%f você está um pouco acima do peso" % (P/(A*A))