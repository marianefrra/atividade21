# Crie um programa que faça uma contagem regressiva de 10 até 0 e exiba "FIM!" ao final.

import time 

for numero in range(10, -1, -1):
    print(numero)
    time.sleep(1)

print("fim!")
