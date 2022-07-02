import pdb
pdb.set_trace()

lista1=[2,4,1]
lista2=[i+1 for i in range(8)]
lista3=[100,250,43]
listas=[lista1, lista2, lista3]
maximo=[max(i) for i in listas]
for i in range(3):
    print (f"El número máximo de la lista {i+1} es {maximo[i]}.\n")


