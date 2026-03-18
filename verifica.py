# esercizio 1
lista = []
n = 9
for i in range(0, n):
    lista.append(i-1)
a = 3
for i in range(0, n):
    if(lista[i] % (a-1) == 0):
        lista[i] = 100
print(lista)

# esercizio 2
lista1 = [2, 3, 5]
lista2 = [-1, 0, 1, 2]
n1 = len(lista1)
n2 = len(lista2)
for i in range(0, n1):
    lista2.append(lista1[i] - 1)
i = 0
n3 = n1 + n2
while(i < n3):
    lista2[i] = lista2[i] - 1
    i = i + 1
print(lista2)

# esercizio 3
lista1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
n = len(lista1)
lista2 = []
for i in range(0, n, 2):
    lista2.append(lista1[i]-1)
for i in range(0, n, 2):
    lista2.append(lista1[lista2[i]])
for i in range(1, n, 3):
    lista2.append(lista1[lista2[i-1]])
print(lista2) 

