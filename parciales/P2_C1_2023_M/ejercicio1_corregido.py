# -*- coding: utf-8 -*-
"""
Segundo parcial - Miércoles 28/06/2023
Ejercicio 1:  Interpretá lo que quiso hacer le programadore y corregí los
dos bugs.
"""
def es_palindromo (palabra: str): # Mal el tipo de dato
    es_palindromo = True

    for i in range(len(palabra)//2):
        if palabra[i] != palabra[-i-1]: # No tomaba correctamente la letra a comparar
            es_palindromo = False
            break # Opcionalmente, podemos cortar el ciclo una vez que detectemos que no es palindromo
    if es_palindromo:
        print(f"{palabra} es un palíndromo") # Faltaba indicar que el texto tenía formato
    else:
        print(f"{palabra} no es un palíndromo")

    
palabra="casa"
es_palindromo(palabra)

palabra="radar"
es_palindromo(palabra)

palabra="neuquen"
es_palindromo(palabra)