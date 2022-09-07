# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
cwd = os.getcwd()
APP_FOLDER = cwd
totalFiles = 0
totalDir = 0
allfiles = 0
filesplus = 0
print("El Archivo se ejecutara en ",APP_FOLDER)
response = input("Desea ejecutarlo? (Y/N)\n")
if response.upper() == "Y":
    maxfiles = int(input("Cuantos archivos quieres que tenga como minimo la carpeta?(no usar con numeros menores a 1000)\n"))
    print("Comprobando archivos..")
    for base, dirs, files in os.walk(APP_FOLDER):
        for directories in dirs:
            totalDir += 1
            totalFiles = 0
        for Files in files:
            totalFiles += 1
            allfiles += 1
        if totalFiles > maxfiles:
            print('PATH : ', base)
            print('Archivos: ', totalFiles)
            filesplus += totalFiles
            print('Directorios: ', totalDir, "\n")

elif response == "N":
    quit()
else:
    print("\nDebes escribir Y o N")
    quit()

print("Terminado")
print('\nTotal Archivos contados es ', filesplus)
print('\nTotal Archivos en el PATH: ', allfiles)

input("Pulse un boton para cerrar..")
quit()

