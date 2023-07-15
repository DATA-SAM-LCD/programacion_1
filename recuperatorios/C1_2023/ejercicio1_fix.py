#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

def generar_numero():
    numero = random.randint(1, 10) # Usaba randint sin indicar el módulo
    # Tambien podria haber cambiado el import a from random import randint
    return numero

def comparar_numeros(intento, objetivo):
    if intento == objetivo:
        print("¡Adivinaste!")
    elif intento < objetivo:
        print("Demasiado bajo. Intenta nuevamente.")
    else:
        print("Demasiado alto. Intenta nuevamente.")

def main():
    objetivo = generar_numero()
    intentos = 0
    adivinado = False

    while not adivinado:
        n_usr = int(input("Adivina el número (entre 1 y 10): ")) # Faltaba castear a int
        comparar_numeros(n_usr, objetivo)
        intentos += 1
        
        if n_usr == objetivo:
            adivinado = True

    print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")

main()