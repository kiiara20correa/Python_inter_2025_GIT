'''Escribe un programa que intente acceder a una clave que no existe en un
diccionario. Si se produce una excepción KeyError, captura la excepción y muestra'''

# Creamos nuestro diccionario
mi_diccionario = {
    
    "nombre": "Amapola",
    "edad": 25,
    "ciudad": "Córdoba",
    "profesion": "Psicóloga",
    "hobbies": ["leer", "comer", "viajar"]
    }

# Solicitamos al usuario una de las claves:
clave = input('''Las categorías disponibles son:
    nombre
    edad
    ciudad
    profesion
    hobbies
Ingrese la categoría a la que desea acceder:  ''')

try:
    # Intentamos acceder a la clave
    valor = mi_diccionario[clave]
    print(f"El valor asociado a '{clave}' es: {valor}")
except KeyError:
    print(f"Error: La clave '{clave}' no existe en el diccionario.")


