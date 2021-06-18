""" 
O intúito desde programa é receber como entrada um número real, indicando o preço da mercadoria comprada, e um número inteiro indicando a quantidade de mercadoria comprada, após isto, ele exibirá o valor da compra antes do desconto e o valor final, já com o desconto aplicado.

Entrada: 
Um número real positivo na primeira linha, indicando o preço da mercadoria, e um número inteiro positivo na segunda linha, indicando a quantidade comprada da mercadoria.

Saída: 
Na primeira linha deve ser impresso um valor real com duas casas decimais, indicando o preço da compra sem o desconto e, na segunda linha, o preço final com o desconto aplicado, também com duas casas decimais. 
"""

# Bloco para entrada manual do valor do produto e quantidade da mercadoria
valorProduto = float(input()) 
qtdMercadoria = int(input()) 

# Bloco para realizar o cálculo do valor total e desconto
valorTotal = qtdMercadoria * valorProduto  
valorDesconto = valorTotal * 0.10
descontoVariavel = valorTotal * (0.01 * qtdMercadoria)
total = valorTotal - (valorDesconto + descontoVariavel)

# Saída
print(f'{valorTotal:.2f}') # Saída indicando o valor total sem o desconto
print(f'{total:.2f}') # Saída indicando o valor final com o desconto aplicado
