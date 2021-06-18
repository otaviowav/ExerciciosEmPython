""" 
Exercicio 02 - Conversor der Polegadas
O objetivo deste exercicio é construir um programa que receba como entrada um número real, simbolizando uma quantidade de polegadas, e exiba o equivalente em centímetros. Lembrando que uma polegada equivale a 2,54 cm.

Entrada:
Um número real representando as polegadas.

Saída
Um número real, com três casas decimais, representando a conversão das polegadas da entrada em centímetros.
"""

polegada = float(input()) # Entrada de um valor real
cm = polegada * 2.54 #Calculo de conversão para centimetros
print (f'{cm:.3f}') #Saída 
