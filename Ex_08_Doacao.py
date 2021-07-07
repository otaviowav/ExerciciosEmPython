# Resolução

vicCoin = 0 # Iniciando o valor com 0
vicSoma = 0 # Iniciando o valor da variável de soma com 0

# Laço criado para solicitar valores enquanto for > -1.0
while vicCoin > -1.0:
    vicCoin = float(input())
    vicSoma = vicSoma + vicCoin # Somando os valores 
print(f'VC$ {vicSoma+1:.2f}')
print(f'R$ {(vicSoma + 1) * 2.50:.2f}') # Realizando a conversão da moeda