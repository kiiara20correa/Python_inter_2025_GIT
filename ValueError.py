'''Escribe un programa que intente dividir dos números. 
Si el segundo número es cero, captura la excepción ZeroDivisionError. 
Si el primer número es un número no válido, captura la excepción ValueError. 
En cualquier caso, muestra un mensaje de error al usuario.'''

print("Bienvenido a la calculadora de solo divisiones ;)")

try:
# Se solicita el ingreso de de dos valores
    numero1 = float(input("Ingresa el primer número o dividendo: "))
    numero2 = float(input("Ingresa el segundo número o divisor: "))
#Se intenta hacer la división
    resultado = numero1 / numero2
    print(f"El resultado de la división es: {resultado}")
# Capturamos ingreso inválido de dividendo
except ValueError:
    print("Opaa, tenés ingresar un número válido. Intentá otra vez.")
# Capturamos ingreso invalido de divisor
except ZeroDivisionError:
    print("Error: Ojo al piojo. No se puede dividir por cero.")
