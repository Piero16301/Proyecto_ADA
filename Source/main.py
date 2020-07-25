from utils.vectorConverter import vectorConverter
from utils.matrixConverter import matrixConverter
from utils.matchConverter import matchConverter

from functionsVectors.matchGreedy import Min_Matching_Greedy
from functionsVectors.matchRecursive import Min_Matching_Recursive, sum
from functionsVectors.matchMemorized import Min_Matching_Memorized, CleanMemoria

from functionsMatrix.transformationGreedy import Min_Transformation_Greedy
from functionsImages.animation import *
from functionsImages.conversion import *

KRED = 0.2126
KGREEN = 0.7152
KBLUE = 0.0722
UMBRAL = 50 #NORMAL_RANGE 60<UMBRAL<120

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


def inputMenu():
    correcto = False
    num = 0
    while not correcto:
        try:
            num = int(input("Introduce una opcion: "))
            correcto = True
        except ValueError:
            print('Error, introduce un numero válido')
    return num


def readVector(path):
    file = open(path, "r")
    newVector = [int(num) for num in file.read().split(',')]
    return newVector


def readMatrix(path):
    with open(path, "r") as file:
        matrix = [[int(num) for num in line.split(',')] for line in file]
    return matrix


salir = False
opcion = 0
menu = 0

print("Ingrese los elementos de los vetores")

vectorA = readVector("vectors/vectorA.txt")
vectorB = readVector("vectors/vectorB.txt")

matrixA = readMatrix("matrix/matrixA.txt")
matrixB = readMatrix("matrix/matrixB.txt")

while not salir:

    print("1. Problema Min-Matching")
    print("2. Problema Min-Transformation")
    print("3. Salir")

    menu = inputMenu()

    if menu == 1:

        while not salir:

            print("1. Matching Greedy")
            print("2. Matching Recursivo")
            print("3. Matching Memoizado")
            print("4. Matching Programación Dinámica")
            print("5. Salir")

            opcion = inputOpcion()

            if opcion == 1:
                print("Algoritmo Greedy")
                A1 = vectorConverter(vectorA)
                B1 = vectorConverter(vectorB)
                resultado = Min_Matching_Greedy(A1, B1)
                print("Match:", resultado)
                print("Peso:", sum(resultado))
            elif opcion == 2:
                print("Algoritmo Recursivo")
                A1 = vectorConverter(vectorA)
                B1 = vectorConverter(vectorB)
                resultado = Min_Matching_Recursive(A1, B1)
                print("Match:", resultado)
                print("Peso:", sum(resultado))
            elif opcion == 3:
                print("Algoritmo Memoizado")
                A1 = vectorConverter(vectorA)
                B1 = vectorConverter(vectorB)
                resultado = Min_Matching_Memorized(A1, B1)
                CleanMemoria()
                print("Match:", resultado)
                print("Peso:", sum(resultado))
            elif opcion == 4:
                print("Algoritmo Programación Dinámica")
                A1 = vectorConverter(vectorA)
                B1 = vectorConverter(vectorB)
                resultado = Min_Matching_Memorized(A1, B1)
                CleanMemoria()
                print("Match:", resultado)
                print("Peso:", sum(resultado))
            elif opcion == 5:
                salir = True
            else:
                print("Introduce un numero entre 1 y 4")

    elif menu == 2:

        while not salir:

            print("1. Transformación Greedy")
            print("2. Transformación Peso Mínimo DP")
            print("3. Lectura de Imágenes")
            print("4. Animación")
            print("5. Transformación Peso Promedio Mínimo DP")
            print("6. Salir")

            opcion = inputOpcion()

            if opcion == 1:
                print("Transformación Greedy")
                image1 = "functionsImages/Images/PS5.png"
                image2 = "functionsImages/Images/XBOX.png"
                A1 = matrixConverter(convertion_blak_white(image1, KRED, KGREEN, KBLUE, UMBRAL))
                B1 = matrixConverter(convertion_blak_white(image2, KRED, KGREEN, KBLUE, UMBRAL))
                print(A1)
                print(B1)
                resultado = Min_Transformation_Greedy(A1, B1)
                print("Transformacion:")
                posiciones = list()
                for i in range(len(resultado[0])):
                    posiciones.append(matchConverter(resultado[0][i], A1[i], B1[i]))
                print(posiciones)
                print("Peso:", resultado[1])
            elif opcion == 2:
                print("2. Transformación Peso Mínimo DP")

            elif opcion == 3:
                print("3. Lectura de Imágenes")
                image1 = "functionsImages/Images/LA.png"
                convert_and_show(image1, KRED, KGREEN, KBLUE, UMBRAL)
            elif opcion == 4:
                print("4. Animación")
                image1 = "functionsImages/Images/LA.png"
                image2 = "functionsImages/Images/NY.png"
                A1 = convertion_blak_white(image1,KRED,KGREEN,KBLUE,UMBRAL)
                B1 = convertion_blak_white(image2,KRED,KGREEN,KBLUE,UMBRAL)
                matching = Min_Transformation_Greedy(A1, B1)
                posiciones = list()
                for i in range(len(matching[0])):
                    posiciones.append(matchConverter(matching[0][i], A1[i], B1[i]))
               #matching = Min_Transformation_PMin_DP(A1, B1)
               #matching = Min_Transformation_PProm_DP(A1, B1)
                animation_black_white(image1,image2,KRED,KGREEN,KBLUE,UMBRAL,posiciones)               
            elif opcion == 5:
                print("5. Transformación Peso Promedio Mínimo DP")

            elif opcion == 6:
                salir = True
            else:
                print("Introduce un numero entre 1 y 6")
    elif menu == 3:
        salir = True
    else:
        print("Introduce un numero entre 1 y 3")

print("Fin")
