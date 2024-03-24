import random
lista = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
numeros = ()
for c in range(0, 5):
    comp = random.choice(lista)
    numeros = numeros + comp
print(comp)
