import sys
from ejercicio2 import read_file, missing_students, make_graph


def run(path: str, N: int) -> None:
    """
    Utilizo las funciones del módulo (ejercicio2) y las corro.
    """
    df = read_file(path=path)
    missing_students(df_students=df, N=N)
    make_graph(df=df)


if __name__ == '__main__':
    if len(sys.argv) == 3:
        path = sys.argv[1]
        try:        
            N = int(sys.argv[2])
        except ValueError:
            raise ValueError('Orden equivocado! Primero escribir ruta del csv y luego la cantidad de años')
        run(path=path, N=N)
    else:
        raise SystemError('Necesito la ruta del archivo y un número entero (diff años), en ese orden, para ejecutar las funciones')