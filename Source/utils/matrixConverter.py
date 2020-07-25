from utils.vectorConverter import vectorConverter


def matrixConverter(matrix):
    result = list()
    for vector in matrix:
        result.append(vectorConverter(vector))
    return result
