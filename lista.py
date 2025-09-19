'''Buscar una palabra en una lista ingresada por teclado usando args y un operador ternario'''

def buscar_palabra(palabra, *args):
    return f"'{palabra}' está en la lista" if palabra in args else f"'{palabra}' NO está en la lista"

# ingreso palabras
lista = input("Ingresa palabras separadas por espacio: ").split()

# buscar
buscar = input("Qué palabra querés buscar?: ")

print(buscar_palabra(buscar, *lista))
#El * le dice “desarma la lista en elementos individuales”.