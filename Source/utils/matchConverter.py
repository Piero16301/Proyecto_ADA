def obtenerIndice(fila, iterador):
    inicio = -1
    final = -1
    for i in range(iterador, len(fila)):
        if inicio == -1:
            if fila[i] == 1:
                inicio = i
            else:
                continue
        else:
            if fila[i] == 1:
                continue
            else:
                final = i
                break
        if i == len(fila)-1 and inicio != -1:
            final = len(fila)
    if inicio == -1 or final == -1:
        inicio = 0
        final = 1
    return [inicio, final-1, final]


def matchConverter(match, filaA, filaB):
    iteradorA = 0
    iteradorB = 0
    resultado = []
    for i in match:
        resultadoA = []
        resultadoB = []
        if isinstance(i[0], int):
            indiceA = obtenerIndice(filaA, iteradorA)
            resultadoA.append((indiceA[0], indiceA[1]))
            iteradorA = indiceA[2]

            if isinstance(i[1], int):
                indiceB = obtenerIndice(filaB, iteradorB)
                resultadoB.append((indiceB[0], indiceB[1]))
                iteradorB = indiceB[2]
            else:
                for a in i[1]:
                    indiceB = obtenerIndice(filaB, iteradorB)
                    resultadoB.append((indiceB[0], indiceB[1]))
                    iteradorB = indiceB[2]
        else:
            for a in i[0]:
                indiceA = obtenerIndice(filaA, iteradorA)
                resultadoA.append((indiceA[0], indiceA[1]))
                iteradorA = indiceA[2]

            if isinstance(i[1], int):
                indiceB = obtenerIndice(filaB, iteradorB)
                resultadoB.append((indiceB[0], indiceB[1]))
                iteradorB = indiceB[2]
            else:
                for a in i[1]:
                    indiceB = obtenerIndice(filaB, iteradorB)
                    resultadoB.append((indiceB[0], indiceB[1]))
                    iteradorB = indiceB[2]

        resultado.append((resultadoA, resultadoB))
    return resultado
