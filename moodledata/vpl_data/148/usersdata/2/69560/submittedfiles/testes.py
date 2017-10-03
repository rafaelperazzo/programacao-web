# -*- coding: utf-8 -*-

import timeit

times = []
ips = []
teste1 = 'i = 9.098 + 7.87'

teste2 = """if (1==1):
                pass
    """
teste3 = """if (1==2):
                pass
    """
teste4 = """
if (1==1):
    cont = cont + 1
"""    

t = timeit.timeit(stmt=teste1,setup='import timeit',number=30000000)
ips.append(30000000/t)
times.append(t)

t = timeit.timeit(stmt=teste2,setup='import timeit',number=30000000)
ips.append(30000000/t)
times.append(t)

t = timeit.timeit(stmt=teste3,setup='import timeit',number=30000000)
ips.append(30000000/t)
times.append(t)

config = """
import timeit
cont = 0
"""
t = timeit.timeit(stmt=teste4,setup=config,number=30000000)
ips.append(30000000/t)
times.append(t)

print (times)
print(ips)