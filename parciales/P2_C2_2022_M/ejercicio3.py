import csv
import sys


class Ordenador:
    def __init__(self, path):
        self.path = path
        self.numeros = []
    
    def leer_de_archivo(self):
        with open(self.path, 'rt', encoding="utf8") as file:
            rows = csv.reader(file)
            for row in rows:
                for elem in row:
                    if elem.lstrip('-').isdigit():
                        self.numeros.append(int(elem))

    def ordenar(self, metodo='creciente'):
        numeros_ordenados = []
        numeros = self.numeros.copy() # Probalo sin copy y fijate que pasa :o
        while numeros:
            minimo = numeros[0]
            for x in numeros: 
                if x < minimo:
                    minimo = x
            numeros_ordenados.append(minimo)
            numeros.remove(minimo)
        
        if metodo == 'decreciente':
            return numeros_ordenados[::-1]
        return numeros_ordenados


if __name__ == '__main__':
    if len(sys.argv) == 3:
        archivo = sys.argv[1]
        orden = sys.argv[2]

        ordenador = Ordenador(path=archivo)
        ordenador.leer_de_archivo()
        print(ordenador.numeros)

        numeros_ordenados = ordenador.ordenar(metodo=orden)
        print(numeros_ordenados)
        print(ordenador.numeros)
    else:
        raise SystemError('Me parece que le pifiaste a la cantidad de argumentos')