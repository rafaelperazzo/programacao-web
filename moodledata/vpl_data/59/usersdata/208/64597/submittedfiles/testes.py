# -*- coding: utf-8 -*g
result=[]
for i in range(10,100,1):
    for j in range(10,100,1):
        list1=[]
        list2=[]
        k=i*j
        if n<1000 or n>100000:
            continue
        else:
            for item in str(i):
                list1.append(item)
            for item in str(j):
                list1.append(item)
            for item in str(k):
                list2.append(item)
            flag=1
            for each in list1:
                if each not in list2:
                    flag=0
                else:
                    list2.remove(each)
            for each in list2:
                if each not in list1:
                    flag=0
            if flag==1:
                if k not in result:
                    result.append(k)
for each in result:
    print(each)
                
                
  