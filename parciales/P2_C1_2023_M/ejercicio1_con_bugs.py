# -*- coding: utf-8 -*-
"""
Segundo parcial - Miércoles 28/06/2023
Ejercicio 1:  Interpretá lo que quiso hacer le programadore y corregí los
dos bugs.
"""
def es_palindromo (palabra:list):
    es_palindromo = True

    for i in range(len(palabra)//2):
        if palabra[i] != palabra[-i]:
            es_palindromo = False
    if es_palindromo:
        print("{palabra} es un palíndromo")
    else:
        print(f"{palabra} no es un palíndromo")

    
palabra="casa"
es_palindromo(palabra)

palabra="radar"
es_palindromo(palabra)