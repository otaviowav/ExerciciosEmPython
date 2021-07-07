# Resolução

# Criamdo uma lista para receber todas as letras dop alfabeto.
alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Definindo um contador iniciando com 1.
cont = 1

# Solicitando um numero inteiro entre 1 e 26.
posicao = int(input())

# Definindo um laço que será interompido caso o valor seja negativo 
while 1 > posicao or posicao > 26:
    posicao = int(input())

# For que percorrerá a lista com as letras do alfabeto dependendo da entrada do numero inteiro inserido na variável posição.
for i in alfabeto:
    while cont <= posicao:
        print(alfabeto [cont-1]*cont)
        cont = cont + 1
    