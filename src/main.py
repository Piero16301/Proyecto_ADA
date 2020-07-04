from functions.converter import converter

from functions.greedy import Min_Matching_Greedy
from functions.recursive import Min_Matching_Recursive, sum
from functions.memorized import Min_Matching_Memorized, CleanMemoria


def inputOpcion():
    correcto = False
    num = 0
    while not correcto:
        try:
            num = int(input("Introduce una opcion: "))
            correcto = True
        except ValueError:
            print('Error, introduce un numero 1-4')
    return num


def readVector(path):
    file = open(path, "r")
    newVector = [int(num) for num in file.read().split(',')]
    return newVector


salir = False
opcion = 0

print("Ingrese los elementos de los vetores")

A = readVector("vectors/vectorA.txt")
B = readVector("vectors/vectorB.txt")

while not salir:

    print("1. Algoritmo Greedy")
    print("2. Algoritmo Recursivo")
    print("3. Algoritmo Memoizado")
    print("4. Salir")

    print(A)
    print(B)

    opcion = inputOpcion()

    if opcion == 1:
        print("Algoritmo Greedy")
        A1 = converter(A)
        B1 = converter(B)
        resultado = Min_Matching_Greedy(A1, B1)
        print("Match:", resultado[0])
        print("Peso:", resultado[1])
    elif opcion == 2:
        print("Algoritmo Recursivo")
        A1 = converter(A)
        B1 = converter(B)
        resultado = Min_Matching_Recursive(A1, B1)
        print("Match:", resultado)
        print("Peso:", sum(resultado))
    elif opcion == 3:
        print("Algoritmo Memoizado")
        A1 = converter(A)
        B1 = converter(B)
        resultado = Min_Matching_Memorized(A1, B1)
        CleanMemoria()
        print("Match:", resultado)
        print("Peso:", sum(resultado))
    elif opcion == 4:
        salir = True
    else:
        print("Introduce un numero entre 1 y 4")

print("Fin")
