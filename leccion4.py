import random
import pdb


PURPLE = '\033[95m'
CYAN = '\033[96m'
DARKCYAN = '\033[36m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
END = '\033[0m'


colores = [PURPLE,CYAN,DARKCYAN,BLUE,GREEN,YELLOW,RED]

def es_primo(n):
    es = True
    for i in range(2,n):
        if n%i == 0:
            es = False
    return es

def es_maximo(lista,numero):
    es = False
    maximo = max(lista)
    if numero == maximo:
        es = True
    return es


def pintar(lista):
    lista_pintada = "["
    x=random.randint(0,6)
    for i in lista:
        if es_maximo(lista,i):
            lista_pintada = lista_pintada + colores[x] + str(i) + END + ', '
        else:
            lista_pintada = lista_pintada + str(i) + ', '
    lista_pintada = lista_pintada[:-1]
    lista_pintada = lista_pintada[:-1]
    lista_pintada = lista_pintada + "]"
    return lista_pintada


def pintar_total(lista):
    lista_total = "["
    for i in lista:
        lista_pintada = pintar(i)
        lista_total = lista_total + lista_pintada + ","
    lista_total = lista_total[:-1]
    lista_total = lista_total + "]"
    return lista_total




lista1 = [[random.randint(-15,15) for i in range(5)]for j in range(5)]
lista2 = [random.randint(1,100) for i in range(15)]


pintada = pintar(lista2)

primos = list(filter(es_primo,lista2))

maximos_señalados = pintar_total(lista1)

lista_maximos = [max(lista1[i]) for i in range(0,len(lista1))]

print("Lista de números aleatorios:")
print("Lista: ",lista2)
print("Lista con máximo pintado:")
print(pintada)
print("Lista de números primos:")
print(primos)
print("Lista de máximos señalados:")
print(maximos_señalados)
print("Lista de máximos:")
print(lista_maximos)