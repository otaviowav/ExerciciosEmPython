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
