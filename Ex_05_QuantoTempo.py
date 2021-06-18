"""
Programa criado para receber como entrada os tempos dos três percursos (de casa até o primeiro emprego, do primeiro emprego até o segundo e do segundo até a casa) e exibe o tempo total consumido.
Não se esqueça que os três tempos serão dados em minutos.

Entrada
Três números inteiros, um por linha, representando os tempos (em minutos) gastos em seus percursos.

Saída
O tempo total gasto seguido por um espaço em branco e pela palavra "minutos", sem aspas e em minúsculo.
"""

tempo1 = int(input())
tempo2 = int(input())
tempo3 = int(input())
tempoGasto = tempo1 + tempo2 + tempo3
print(f'{tempoGasto} minutos')