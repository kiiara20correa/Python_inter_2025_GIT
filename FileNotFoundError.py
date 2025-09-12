'''Escribe un programa que intente abrir un archivo que no existe.
Si se produce una excepción FileNotFoundError, captura la excepción y muestra un mensaje de error al usuario. 
Sin embargo, también intenta crear el archivo si no existe.'''

# Se pide al usuario el nombre del archivo
nombre_archivo = input("Bienvenido. Ingrese el nombre del archivo que desea abrir: ")
try:
# Intentamos abrir el archivo que nos indica
    with open(nombre_archivo, "r") as archivo:
        contenido = archivo.read()
        print('''Abriendo...
Contenido del archivo: ''')
        print(contenido)
# Capturamos la excepción, en este caso, se produce cuando  el archivo no existe
except FileNotFoundError:
    print(f"El archivo '{nombre_archivo}' no existe. Se creará uno nuevo.")
    with open(nombre_archivo, "w") as archivo:
        archivo.write("")  # Creamos un archivo vacío
    print(f"Archivo '{nombre_archivo}' creado exitosamente.")
