'''Dados dos conjuntos, A y B, escribe un programa en Python que imprima el
conjunto de los elementos que se encuentran en A o en B, pero no en ambos'''

conjuntoa = {1, 2, 3, 4, 5, 6, 7, 9}
conjuntob = {2, 6, 9, 1, 8}

print(conjuntoa - conjuntob)
print(conjuntob - conjuntoa)
print(conjuntob.symmetric_difference(conjuntoa))