'''Calcular el promedio de una lista de números usando args y un operador ternario'''

def promedio(*args):
    return sum(args) / len(args) if len(args) > 0 else 0

numeros = input("Ingresa los números separados por espacio: ")

# convertir a lista de floats
convertir = list(map(float, numeros.split()))
#map: función que aplica otra función a cada elemento de una lista

# llamar a la función usando * para "desarmar" la lista
print(f"El promedio es: {promedio(*convertir)}")