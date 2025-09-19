'''Determinar si un número es par o impar'''

numero = int(input('''¡Bienvenido a la calculadora de numeros pares e impares! 
"Por favor ingrese un número: '''))

resultado = "par" if numero % 2 == 0 else "impar"

print(f"{numero} es {resultado}")