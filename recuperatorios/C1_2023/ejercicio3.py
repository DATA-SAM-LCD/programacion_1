import sys
from ejercicio2 import leer_archivo, imprimir_registros_materia_promedio, \
    grafico_boxplot_materia

if __name__ == '__main__':
    if len(sys.argv) == 3:
        archivo = sys.argv[1]
        materia = sys.argv[2].upper()

        # Las siguientes 4 líneas de abajo podrían ir en una función
        df = leer_archivo(archivo)
        imprimir_registros_materia_promedio(df, materia)
        grafico_boxplot_materia(df, materia)
        grafico_boxplot_materia(df)
    else:
        raise SystemError(
            '''Debe ingresar el nombre del archivo y la materia a consultar
             Ejemplo: python ejercicio3.py notas_materias.csv MATEMATICA'''
        )
