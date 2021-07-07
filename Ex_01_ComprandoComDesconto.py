# Resolução

valorProduto = float(input()) # Solicitando o valor da mercadoria
qtdMercadoria = int(input()) # Solicitando a quantidade 

# Bloco responsável por realizar a multiplicação da quantidade pelo valor e o desconto de 10%
valorTotal = qtdMercadoria * valorProduto  
valorDesconto = valorTotal * 0.10

# Aplicando mais 1% de desconto a cada unidade comprada
descontoVariavel = valorTotal * (0.01 * qtdMercadoria)
total = valorTotal - (valorDesconto + descontoVariavel)

# Saida
print(f'{valorTotal:.2f}') 
print(f'{total:.2f}') 
