"""
Hola! Este ejercicio fue hecho por mi y no es el mismo que
dieron en el parcial. Es probable que haya diferencias!
Pero, sirve para practicar :)
"""

def geringoso(palabra):
    capadepenapa = ''
    for c in palabra:
        if c in 'aeiou':
            capadepenapa += c + 'p' + c.lower()
        else:
            capadepenapa = c
    return capadepenapa

print(geringoso('banana'))
print(geringoso('manzana'))
print(geringoso('mandarina'))
print(geringoso('Arbol'))