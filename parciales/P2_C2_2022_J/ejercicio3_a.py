import sys
from ejercicio2 import read_text_file, count_letters

def main(file, N, pretty_print=True):
    text = read_text_file(file)
    print(count_letters(text, N, pretty_print))

if __name__ == '__main__':
    if len(sys.argv) == 3:
        file = sys.argv[1]
        N = int(sys.argv[2])

        main(file, N)
    else:
        raise SystemError('Cantidad de argumentos invalida')