import csv

def leer_archivo(path):
    numeros = []
    with open(path, 'rt', encoding="utf8") as file:
        rows = csv.reader(file)
        for row in rows:
            # Se puede hacer list comprehensions
            for elem in row:
                if elem.lstrip('-').isdigit():
                    numeros.append(int(elem))
    return numeros


def ordenar_numeros_creciente(numeros):
    numeros_ordenados = []
    while numeros:
        minimo = numeros[0]
        for x in numeros: 
            if x < minimo:
                minimo = x
        numeros_ordenados.append(minimo)
        numeros.remove(minimo)
    
    return numeros_ordenados


def ordenar_numeros_decreciente(numeros):
    # Posible solucion
    # numeros_ordenados = []
    # while numeros:
    #     maximo = numeros[0]
    #     for x in numeros: 
    #         if x > maximo:
    #             maximo = x
    #     numeros_ordenados.append(maximo)
    #     numeros.remove(maximo)

    # Otra solucion mas mejor
    creciente = ordenar_numeros_creciente(numeros)
    return creciente[::-1] # creciente[inicio:fin:paso]


if __name__ == '__main__':
    archivo = './numeros.csv'
    orden = 'creciente' # o 'decreciente'

    numeros = leer_archivo(path=archivo)
    if (orden == 'creciente'):
        numeros_ordenados = ordenar_numeros_creciente(numeros)
    else:
        numeros_ordenados = ordenar_numeros_decreciente(numeros)
    
    print(numeros_ordenados)