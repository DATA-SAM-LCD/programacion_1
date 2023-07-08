"""
Hola! Este ejercicio fue hecho por mi y no es el mismo que
dieron en el parcial. Es probable que haya diferencias!
Pero, sirve para practicar :)
"""

def geringoso(palabra):
    """
    Documentacion
    """
    capadepenapa = ''
    for c in palabra:
        # if c.lower() in 'aeiou': # Otra posible solucion
        if c in 'aeiouAEIOU':
            capadepenapa += c + 'p' + c.lower()
        else:
            capadepenapa += c # faltaba el +
    return capadepenapa

print(geringoso('banana')) # bapanapanapa
print(geringoso('manzana')) # mapanzapanapa
print(geringoso('mandarina'))
print(geringoso('Arbol')) # Aparbopol