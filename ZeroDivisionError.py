'''Escribe un programa que intente dividir dos números. Si el segundo número es cero,
captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario.'''

print("Bienvenido a la calculadora de solo divisiones :)")
# Primero que el usuario ingrese los números:
numero1 = float(input("Ingresa el primer número o dividendo: "))
numero2 = float(input("Ingresa el segundo número o divisor: "))

try:
    resultado = numero1 / numero2
    print(f"El resultado de la división es: {resultado}")
#El bloque except se ejecutará cuando el bloque try falle debido a un error, acá especificamos ante qué tipo de error se va a ejecutar
except ZeroDivisionError:
    print("Error: Ojo al piojo. No se puede dividir por cero.")


