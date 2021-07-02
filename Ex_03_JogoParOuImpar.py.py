""" 
Você gosta de jogos? Silvio gosta! Ainda mais de jogos matemáticos e que precisam de raciocínio lógico. Como Silvio é muito criativo, criou um jogo para passar o tempo com seus amigos entre os intervalos das aulas. O jogo é simples, um de seus amigos diz em voz alta um número natural maior ou igual a dois e Silvio deve dizer rapidamente o número ímpar anterior e o par posterior ao número pronunciado.

Você é um programador que gosta de desafios, afinal todo programador encara desafios o tempo todo, e por isso se ofereceu para criar um programa para automatizar a resposta de Silvio, recebendo como entrada um número natural maior ou igual a dois e exibindo o ímpar anterior e o par posterior.

Entrada:
Um número natural maior ou igual a dois.

Saída:
Dois números naturais, separados por um espaço, em que o primeiro é o número ímpar que antecede o valor dado na entrada e o segundo é o par que sucede o valor dado na entrada.
"""
# Resolução


n = int(input()) # Entrada de um número natural maior ou igual a dois.

# Contadores de numeros pares e impares seguido dos espaços solicitado no exercício
countImpar = n 
countPar = n 
par = ''
impar = ''

# Loop realizando break caso o valor seja negativo
while n > 0: 
    countImpar -= 1
    countPar += 1
    if countImpar %2 == 1: # Caso o resto da divisção seja 1 o numero é impar
        impar = countImpar
    if countPar %2 == 0: # Caso o resto da divisção seja 0 o numero é par
        par = countPar
    if par != '' and impar != '':
        print(impar,par)
        break
