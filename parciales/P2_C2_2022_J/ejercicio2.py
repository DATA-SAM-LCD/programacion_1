from collections import Counter

def read_text_file(file_name):
    """
    Lee un archivo de texto y devuelve su contenido formateado
    """
    with open(file_name, 'rt') as file:
        text = file.read()
        text = text.replace('\n', '') # Elimino los saltos de linea
        text = text.replace(' ', '') # Elimino los espacios
        text = text.replace(',', '') # Elimino las comas
    return text

def count_letters(text, N, pretty_print=True):
    """
    Devuelve las N letras mas frecuentes, indicando
    la cantidad de veces que aparecen en un formato como este:

    Las 5 letras mas frecuentes son:
    a: 10
    b: 9
    c: 8
    ...

    """
    counter = Counter(text)

    if pretty_print:
        texto = f'Las {N} letras mas frecuentes son:\n'
        for letra, cantidad in counter.most_common(N):
            texto += f'{letra}: {cantidad} veces\n'
        return texto
    
    return counter.most_common(N)

if __name__ == '__main__':
    archivo = 'letras.txt'
    N = 5

    text = read_text_file(archivo)
    print(count_letters(text, N))