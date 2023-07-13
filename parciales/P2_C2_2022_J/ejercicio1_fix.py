"""
Hola! Este ejercicio fue hecho por mi y no es el mismo que
dieron en el parcial. Es probable que haya diferencias!
Pero, sirve para practicar :)
"""

def es_palindromo(palabra):
    palabra = palabra.lower() # No se estaba guardando el resultado de la operacion
    palabra = palabra.replace(" ", "") # No se extraian los espacios (medio engañoso)
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    return False # Si no es palindromo, no se estaba retornando nada


print(es_palindromo("ana"))
print(es_palindromo("Anita lava la tina"))
print(es_palindromo("Enrique"))
print(es_palindromo("radar"))
print(es_palindromo("sarasa"))