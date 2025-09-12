'''Escribe un programa que intente sumar un número y una cadena. Si se produce un error
de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario.'''

# Primero solicitamos un número y una otro valor (letras, números, espacios o símbolos) al usuario:

numero = float(input("Ingrese un número: "))
valor = input("Ingrese otro valor: ")

try:
    # Intentar convertir valor a float antes de sumar
    resultado = numero + float(valor)
    print(f"El resultado de la suma es: {resultado}")
except ValueError:
    print("Error: El segundo valor no es un número.")
