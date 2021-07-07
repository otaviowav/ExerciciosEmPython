# Resolução

notaTrabalho = float(input()) # Inserindo a nota do trabalho
notaProva = float(input()) # Inserindo a nota da prova

# Realizando o cálculo da média
media = (notaTrabalho + notaProva) / 2 


if media >= 6: # Caso a média seja maior ou igual a 6, aprovado
    print("aprovado")

# Caso contrário se a nota do trabalho maior ou igual a 2 e a 
# nota da prova menor que 6, talvez com a sub
elif notaTrabalho >=2 and notaProva < 6: 
    print("talvez com a sub")

# Caso contrário se a média for menor que 6, reprovado
elif media < 6:
    print("reprovado")
