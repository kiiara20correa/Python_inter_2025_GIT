'''Imprimir un mensaje de error si no se pasan suficientes argumentos'''

def mi_funcion(*args):
    if len(args) < 2:
        print("Error: no se pasaron suficientes argumentos")
    else:
        print(f"Los argumentos recibidos son: {args}")

ingreso = input("Ingresa por lo menos 2 argumentos separados por espacio: ")

# convertimos el texto en una lista de números
numeros = [float(n) for n in ingreso.split()]  
#.split(): corta el texto por los espacios
#for n in entrada: esto dice: “por cada elemento n en esa lista…”.
#float(n): Convierte el texto "5" en el número 5.0 (decimal).

mi_funcion(*numeros)
