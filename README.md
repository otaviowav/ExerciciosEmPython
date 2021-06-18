## ExerciciosEmPython
 Repositório para exercícios em Python

#### Exercicio 01 - Comprando com desconto

###### Criar um programa para receber como entrada um número real, indicando o preço da mercadoria comprada, e um número inteiro indicando a quantidade de mercadoria comprada, após isto, ele exibirá o valor da compra antes do desconto e o valor final, já com o desconto aplicado.

#### Entrada:
* Um número real positivo na primeira linha, indicando o preço da mercadoria, e um número inteiro positivo na segunda linha, indicando a quantidade comprada da mercadoria.

#### Saída:
* Na primeira linha deve ser impresso um valor real com duas casas decimais, indicando o preço da compra sem o desconto e, na segunda linha, o preço final com o desconto aplicado, também com duas casas decimais.

##

#### Exercicio 02 - Conversor der Polegadas

###### Construir um programa que receba como entrada um número real, simbolizando uma quantidade de polegadas, e exiba o equivalente em          centímetros. Lembrando que uma polegada equivale a 2,54 cm.

#### Entrada:
* Um número real representando as polegadas.

#### Saída
* Um número real, com três casas decimais, representando a conversão das polegadas da entrada em centímetros.

## 

#### Exercicio 03 - Jogo do par ou ímpar

###### Criar um programa para automatizar uma resposta, recebendo como entrada um número natural maior ou igual a dois e exibindo o ímpar anterior e o par posterior.

#### Entrada

* Um número natural maior ou igual a dois.

#### Saída

* Dois números naturais, separados por um espaço, em que o primeiro é o número ímpar que antecede o valor dado na entrada e o segundo é o par que sucede o valor dado na entrada.

##

#### Exercicio 04 - Dia da entrega

###### Criar um programa que receba como entrada dois valores: (I) uma string com um dia da semana ('domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta' ou 'sabado'), sem acentuação, que indica o dia que um cliente realizou a compra no site da empresa; (II) um número natural que pode variar de 0 a 6, que indica a quantidade de dias, a partir da realização da compra, que o cliente deverá aguardar para receber a mercadoria. O programa deve exibir o dia da semana que a compra será entregue.

###### Note que um prazo de zero dias significa que a entrega será concluída no mesmo dia, assim como um prazo de dois dias significa que a entrega será concluída exatamente dois dias após a realização da compra. Por exemplo, se a compra foi realizada no 'sabado' e o prazo é de três dias, o cliente receberá na 'terca'. Cuidado com a acentuação, repare que ela não está presente nas entradas e nem nas saídas, nem mesmo o 'ç' de terça.

#### Entrada
* A entrada é composta por duas linhas, a primeira conterá uma string que corresponde a um dia da semana, que poderá ser qualquer um destes: ('domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta' ou 'sabado'), sem acentuação e sem os apóstrofos, que representa o dia em que o cliente realizou a compra; a segunda linha contém um número natural entre 0 e 6 (inclusive os extremos), que indica o prazo que o cliente deve esperar até receber sua compra.

#### Saída
* Uma string que indica o dia que o usuário receberá sua compra. Caso o usuário receba no mesmo dia, deverá ser exibida a string 'chega hoje!', sem apóstrofos. Caso o usuário receba em algum dos seis dias posteriores à compra, deverá ser exibida a string 'sera entregue <dia>', em que <dia> será o dia correspondente, também sem apóstrofos e sem acentuação.
 
##
 
#### Exercicio 05 - Quanto tempo?
 
###### Criar um programa para receber como entrada os tempos dos três percursos (de casa até o primeiro emprego, do primeiro emprego até o segundo e do segundo até a casa) e exibe o tempo total consumido.

###### Não se esqueça que os três tempos serão dados em minutos.

#### Entrada
* Três números inteiros, um por linha, representando os tempos (em minutos) gastos em seus percursos.

#### Saída
* O tempo total gasto seguido por um espaço em branco e pela palavra "minutos", sem aspas e em minúsculo.
 
##
 
#### Exercicio 06 - Professor, mas é só 0,5
 
 
###### Criar um programa para receber como entrada dois números reais, o primeiro representando a nota de trabalhos e o segundo a nota da prova regular. Considerando que cada uma das duas notas representa 50% da média final, seu programa exibirá uma mensagem indicando a situação do aluno que poderá ser uma das três:

###### a) Aprovado: se a média final for maior ou igual a seis;

###### b) Talvez com a prova substitutiva: se existir alguma nota possível na prova substitutiva que permita que a média final fique maior ou igual a seis. Lembrando que, assim como a nota de trabalhos e da prova regular, a nota máxima na prova substitutiva é dez e que ela pode substituir apenas a nota da prova regular, não a de trabalhos;

###### c) Reprovado: se a média final for menor do que seis e não existir possibilidade de recuperação, mesmo com a nota máxima na prova substitutiva.

###### Obs.: O nome do problema é uma referência a clássica frase proferida no final do semestre pelos alunos que não estudam adequadamente.

#### Entrada
* Dois números reais que podem variar de 0.00 à 10.00, um por linha, que representam a nota de trabalhos e a nota da prova regular, respectivamente.

#### Saída
* Uma frase indicando a situação do aluno a quem pertencem as notas da entrada. A situação pode ser 'aprovado', 'reprovado' ou 'talvez com a sub', sem os apóstrofos e completamente em minúsculo. Veja nos exemplos como a saída deve ser exibida.

##
