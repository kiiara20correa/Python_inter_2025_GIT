'''Dados un conjunto, A, escribe un programa en Python que imprima si el conjunto es
un subconjunto de otro conjunto, B'''

conjuntoa = {'sufrimiento', 'melancolía', 'apatía', 'dolor', 'desesperación', 'agotamiento'}
conjuntob = {'dolor', 'sufrimiento'}
print(conjuntob.issubset(conjuntoa))
