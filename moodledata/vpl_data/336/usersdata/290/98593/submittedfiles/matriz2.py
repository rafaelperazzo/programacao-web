# -*- coding: utf-8 -*-
c1=0
c2=0
c3=0
dim=int9input("Dimensão da matriz: "))
while dim<2:
    dim=int(input("Dimensão n da matriz: "))
matriz=np.empty([dim,dim])
matriztrans=np.empty([dim,dim])
matrizdiag=np.empty([2,dim])
matrizultprim=np.empy([dim,dim])
for i in range(