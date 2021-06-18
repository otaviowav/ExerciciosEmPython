""" 
O objetivo é criar um programa para automatizar uma resposta, recebendo como entrada um número natural maior ou igual a dois e exibindo o ímpar anterior e o par posterior.

Entrada
Um número natural maior ou igual a dois.

Saída
Dois números naturais, separados por um espaço, em que o primeiro é o número ímpar que antecede o valor dado na entrada e o segundo é o par que sucede o valor dado na entrada.
"""

n = int(input())  
countImpar = n 
countPar = n 
par = ''
impar = ''
while n > 0: 
    countImpar -= 1
    countPar += 1
    if countImpar %2 == 1:
        impar = countImpar
    if countPar %2 == 0:
        par = countPar
    if par != '' and impar != '':
        print(impar,par)
        break
