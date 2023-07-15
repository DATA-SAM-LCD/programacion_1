#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

def generar_numero():
    numero = randint(1, 10)
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
        n_usr = input("Adivina el número (entre 1 y 10): ")
        comparar_numeros(n_usr, objetivo)
        intentos += 1
        
        if n_usr == objetivo:
            adivinado = True

    print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")

main()