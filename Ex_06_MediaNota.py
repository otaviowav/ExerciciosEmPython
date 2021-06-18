"""
Programa criado para receber como entrada dois números reais, o primeiro representando a nota de trabalhos e o segundo a nota da prova regular. Considerando que cada uma das duas notas representa 50% da média final, seu programa exibirá uma mensagem indicando a situação do aluno que poderá ser uma das três:
    a) Aprovado: se a média final for maior ou igual a seis;
    b) Talvez com a prova substitutiva: se existir alguma nota possível na prova substitutiva que permita que a média final fique maior ou igual a seis. Lembrando que, assim como a nota de trabalhos e da prova regular, a nota máxima na prova substitutiva é dez e que ela pode substituir apenas a nota da prova regular, não a de trabalhos;
    c) Reprovado: se a média final for menor do que seis e não existir possibilidade de recuperação, mesmo com a nota máxima na prova substitutiva.
Obs.: O nome do problema é uma referência a clássica frase proferida no final do semestre pelos alunos que não estudam adequadamente.

Entrada
Dois números reais que podem variar de 0.00 à 10.00, um por linha, que representam a nota de trabalhos e a nota da prova regular, respectivamente.

Saída
Uma frase indicando a situação do aluno a quem pertencem as notas da entrada. A situação pode ser 'aprovado', 'reprovado' ou 'talvez com a sub', sem os apóstrofos e completamente em minúsculo. Veja nos exemplos como a saída deve ser exibida.
"""

notaTrabalho = float(input())
notaProva = float(input())
media = (notaTrabalho + notaProva) / 2
if media >= 6:
    print("aprovado")
elif notaTrabalho >=2 and notaProva < 6:
    print("talvez com a sub")
elif media < 6:
    print("reprovado")
