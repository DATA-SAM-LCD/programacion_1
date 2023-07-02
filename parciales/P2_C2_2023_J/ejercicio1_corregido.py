# -*- coding: utf-8 -*-
"""
Segundo parcial - Jueves 29/06/2023
Ejercicio 1:  Interpretá lo que quiso hacer le programadore y corregí los
dos bugs.
"""
def encontrar_duplicados(lista_de_elementos:list)-> list: #
    duplicados = [] # 3
    unicos = set() # 1,2,3
    for elemento in lista_de_elementos: # 3
        if elemento in unicos and elemento not in duplicados: # Es operador and
            duplicados.append(elemento)
        unicos.add(elemento)
    return duplicados # Devuelve una lista con los elementos duplicados

lista=[1, 2, 3, 4, 3, 2, 5]
print(lista) 
print(encontrar_duplicados(lista))

lista=['a', 'b', 'c', 'a', 'd', 'e', 'b']
print(lista) 
print(encontrar_duplicados(lista))