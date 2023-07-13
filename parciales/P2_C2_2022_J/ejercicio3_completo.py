import sys
from collections import Counter

class Texto:
    def __init__(self, file):
        self.file = file
        self.text = ''

    def read_text_file(self):
        with open(self.file, 'rt') as file:
            text = file.read()
            text = text.replace('\n', '')
            text = text.replace(' ', '')
            text = text.replace(',', '')
        self.text = text

    def count_letters(self, N, pretty_print=True):
        counter = Counter(self.text)

        if pretty_print:
            texto = f'Las {N} letras mas frecuentes son:\n'
            for letra, cantidad in counter.most_common(N):
                texto += f'{letra}: {cantidad} veces\n'
            return texto
        
        return counter.most_common(N)


if __name__ == '__main__':
    if len(sys.argv) == 3:
        file = sys.argv[1]
        N = int(sys.argv[2])

        texto_inst = Texto(file)
        texto_inst.read_text_file()
        print(texto_inst.count_letters(N))
    else:
        raise SystemError('Cantidad de argumentos invalida')