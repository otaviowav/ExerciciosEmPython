## <a id="anchortextTopo"/>ExerciciosEmPython<img align="center" alt="Python" height="40" width="50" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">
Repositório criado para realização de exercícios práticos na linguagem Python.

Neste documento encontra-se os enunciados para estudo, as resoluções encontram-se dentro do arquivo .py de cada exercicio proposto.

#### Lista de exercícios<br>
[Exercício 01](#anchortext01)<br>
[Exercício 02](#anchortext02)<br>
[Exercício 03](#anchortext03)<br>
[Exercício 04](#anchortext04)<br>
[Exercício 05](#anchortext05)<br>
[Exercício 06](#anchortext06)<br>
[Exercício 07](#anchortext07)<br>
[Exercício 08](#anchortext08)<br>

## <a id="anchortext01"/>Exercicio 01 - Comprando com desconto

Maria, além de comerciante, é também uma excelente negociante! Por isso, sempre consegue descontos em suas compras. Ao visitar uma loja, Maria recebeu a seguinte proposta de um vendedor: "Se comprar minha mercadoria concederei um desconto fixo de 10% e mais 1% a cada unidade comprada". Infelizmente, Maria está cansada de tanto trabalhar e não quer fazer os cálculos sozinha para descobrir qual será o valor da compra antes e depois do desconto, por isso pediu sua ajuda.

Você criará um programa que receberá como entradas um número real, indicando o preço da mercadoria comprada por Maria, e um número inteiro, indicando a quantidade de mercadoria comprada, e exibirá o valor da compra antes do desconto e o valor final, já com o desconto aplicado.

**Observação:** Para todos os efeitos, assuma que essa loja nunca vende mais do que 40 unidades de uma mesma mercadoria para a mesma pessoa. Repare que não é necessário verificar, basta assumir que isso é verdade.

### **Entrada:**<br>
Um número real positivo na primeira linha, indicando o preço da mercadoria, e um número inteiro positivo na segunda linha, indicando a quantidade comprada da mercadoria.

### **Saída:**<br>
Na primeira linha deve ser impresso um valor real com duas casas decimais, indicando o preço da compra sem o desconto e, na segunda linha, o preço final com o desconto aplicado, também com duas casas decimais.<br>

Exemplo Input     |Exemplo Output
:-----------------|:-----------------
1.00<br>40        |40.00<br>20.00
100.00<br>10      |1000.00<br>800.00
1000.00<br>5      |5000.00<br>4250.00
2608542.45<br>39  |101733155.55<br>51883909.33

[Voltar ao topo](#anchortextTopo)<br>

#

## <a id="anchortext02"/>Exercicio 02 - Conversor de Polegadas

Megan quer comprar um novíssimo smartphone e está muito empolgada com as possibilidades que uma tela de tantas polegadas pode oferecer para seu entretenimento. Mas há um problema, Megan percebeu que não sabe lidar com polegadas, afinal sempre realizou cálculos usando centímetros e gostaria de se basear nessa unidade de medida para imaginar o tamanho de tela que comprará. Você pode ajudar Megan?

Seu trabalho é construir um programa que receba como entrada um número real, simbolizando uma quantidade de polegadas, e exiba o equivalente em centímetros. Lembre-se que uma polegada equivale a 2,54 cm.

### **Entrada:**<br>
Um número real representando as polegadas.

### **Saída:**<br>
Um número real, com três casas decimais, representando a conversão das polegadas da entrada em centímetros.<br>

Exemplo Input     |Exemplo Output
:-----------------|:-----------------
10.0              |25.400
6809332.23761114  |17295703.884
2.0               |5.080
1.0               |2.540

[Voltar ao topo](#anchortextTopo)<br>

#

## <a id="anchortext03"/>Exercicio 03 - Jogo do par ou ímpar

Você gosta de jogos? Silvio gosta! Ainda mais de jogos matemáticos e que precisam de raciocínio lógico. Como Silvio é muito criativo, criou um jogo para passar o tempo com seus amigos entre os intervalos das aulas. O jogo é simples, um de seus amigos diz em voz alta um número natural maior ou igual a dois e Silvio deve dizer rapidamente o número ímpar anterior e o par posterior ao número pronunciado.

Você é um programador que gosta de desafios, afinal todo programador encara desafios o tempo todo, e por isso se ofereceu para criar um programa para automatizar a resposta de Silvio, recebendo como entrada um número natural maior ou igual a dois e exibindo o ímpar anterior e o par posterior.

### **Entrada:**<br>
Um número natural maior ou igual a dois.

### **Saída:**<br>
Dois números naturais, separados por um espaço, em que o primeiro é o número ímpar que antecede o valor dado na entrada e o segundo é o par que sucede o valor dado na entrada.<br>

Exemplo Input |Exemplo Output
:-------------|:-------------
2             |1 4
55            |53 56
100           |99 102
88            |87 90

[Voltar ao topo](#anchortextTopo)<br>

#

## <a id="anchortext04"/>Exercicio 04 - Dia da entrega

"Tempos modernos"… e não nos referimos ao clássico filme de Charles Chaplin, mas sim às facilidades que a tecnologia proporciona, inimagináveis há algumas décadas. Uma dessas tecnologias é a internet, que possibilitou as compras online.

Podemos comprar em sites de empresas e em poucos dias a mercadoria estará em nossas mãos. A Impacta Express, uma multinacional de comércio eletrônico e com sua própria logística de distribuição, quer revolucionar realizando qualquer entrega no prazo de até seis dias a partir da realização da compra.

Por participar de sites de programação como o URI Online Judge, o coordenador de TI da Impacta Express encontrou você entre os primeiros do rank, ficou fascinado com seu desempenho e te convidou para uma entrevista!

Como parte da entrevista, o coordenador solicitou um programa que receba como entrada dois valores: (I) uma string com um dia da semana ('domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta' ou 'sabado'), sem acentuação, que indica o dia que um cliente realizou a compra no site da empresa; (II) um número natural que pode variar de 0 a 6, que indica a quantidade de dias, a partir da realização da compra, que o cliente deverá aguardar para receber a mercadoria. O programa deve exibir o dia da semana que a compra será entregue.

Note que um prazo de zero dias significa que a entrega será concluída no mesmo dia, assim como um prazo de dois dias significa que a entrega será concluída exatamente dois dias após a realização da compra. Por exemplo, se a compra foi realizada no 'sabado' e o prazo é de três dias, o cliente receberá na 'terca'. Cuidado com a acentuação, repare que ela não está presente nas entradas e nem nas saídas, nem mesmo o 'ç' de terça.

### **Entrada:**<br>
A entrada é composta por duas linhas, a primeira conterá uma string que corresponde a um dia da semana, que poderá ser qualquer um destes: ('domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta' ou 'sabado'), sem acentuação e sem os apóstrofos, que representa o dia em que o cliente realizou a compra; a segunda linha contém um número natural entre 0 e 6 (inclusive os extremos), que indica o prazo que o cliente deve esperar até receber sua compra.

### **Saída:**<br>
Uma string que indica o dia que o usuário receberá sua compra. Caso o usuário receba no mesmo dia, deverá ser exibida a string 'chega hoje!', sem apóstrofos. Caso o usuário receba em algum dos seis dias posteriores à compra, deverá ser exibida a string 'sera entregue "dia"', em que "dia" será o dia correspondente, também sem apóstrofos e sem acentuação.<br>

Exemplo Input |Exemplo Output
:-------------|:-------------
terca<br>5    |sera entregue domingo
sabado<br>6   |sera entregue sexta
terca<br>0    |chega hoje!
quinta<br>5   |sera entregue terca

[Voltar ao topo](#anchortextTopo)<br>

#

## <a id="anchortext05"/>Exercicio 05 - Quanto tempo?

"Não tem jeito!", Julius repete para si mesmo que o trânsito da cidade grande é o maior vilão de seus dias, fazendo com que gaste muito tempo no percurso entre sua casa e o primeiro emprego, entre seu primeiro emprego e o segundo emprego, e entre seu segundo emprego até o regresso a casa. Pois é, Julius tem dois empregos!

Julius é ótimo na realização de contas, mas como está sempre com pressa, nunca teve tempo para calcular o tempo total gasto no trânsito, desde o momento que sai de casa até o momento que regressa. Seu relógio é antigo, não possibilitando cronometrar um percurso, pausar e continuar a cronometragem no próximo, por isso só sabe o tempo gasto entre os percursos isoladamente, mas não o tempo gasto nos percursos somados. Até ofereceram um novo relógio com desconto para Julius, para ele respondeu ao vendedor que "não comprar o relógio daria um desconto maior".

Você, como um bom amigo, se ofereceu para criar um programa que recebe como entrada os tempos dos três percursos de Julius (de casa até o primeiro emprego, do primeiro emprego até o segundo e do segundo até a casa) e exibe o tempo total consumido.

Não se esqueça que os três tempos serão dados em minutos.

### **Entrada:**<br>
Três números inteiros, um por linha, representando os tempos (em minutos) gastos por Julius em seus percursos.

### **Saída:**<br>
O tempo total gasto por Julius seguido por um espaço em branco e pela palavra "minutos", sem aspas e em minúsculo, conforme exemplos.<br>

Exemplo Input     |Exemplo Output
:-----------------|:-----------------
275<br>245<br>212 |732 minutos
116<br>110<br>288 |514 minutos
211<br>81<br>27   |319 minutos
40<br>10<br>30    |87 90

[Voltar ao topo](#anchortextTopo)<br>

#

## <a id="anchortext06"/>Exercicio 06 - Professor, mas é só 0,5

Como é bom estar matriculado em um curso relacionado à computação! Há muitas disciplinas interessantes e um mundo de descobertas! Porém, como quase tudo na vida, para ter sucesso é necessário comprometimento e esforço para aprender os conteúdos que são passados pelos professores, pois exigem atenção e estudo extraclasse.

Você, um estudante exemplar, conquista notas elevadas e por isso não se preocupa com a média final nas disciplinas, pois sabe que será aprovado sem precisar de prova substitutiva. No entanto, alguns de seus colegas estão apreensivos, pois estavam acostumados a estudar "em cima da hora" e demoraram para perceber que essa "tática" não funciona mais. Por isso, querem saber se com as notas que possuem serão aprovados, reprovados ou se há a possibilidade de aprovação com a prova substitutiva.

Como em situações críticas também há compaixão, você resolveu criar um programa para ajudar seus colegas. Seu programa receberá como entrada dois números reais, o primeiro representando a nota de trabalhos e o segundo a nota da prova regular. Considerando que cada uma das duas notas representa 50% da média final, seu programa exibirá uma mensagem indicando a situação do aluno que poderá ser uma das três:

a) **Aprovado:** se a média final for maior ou igual a seis;

b) **Talvez com a prova substitutiva:** se existir alguma nota possível na prova substitutiva que permita que a média final fique maior ou igual a seis. Lembrando que, assim como a nota de trabalhos e da prova regular, a nota máxima na prova substitutiva é dez e que ela pode substituir apenas a nota da prova regular, não a de trabalhos;

c) **Reprovado:** se a média final for menor do que seis e não existir possibilidade de recuperação, mesmo com a nota máxima na prova substitutiva.

**Obs.:** O nome do problema é uma referência a clássica frase proferida no final do semestre pelos alunos que não estudam adequadamente.

### **Entrada:**<br>
Dois números reais que podem variar de 0.00 à 10.00, um por linha, que representam a nota de trabalhos e a nota da prova regular, respectivamente.

### **Saída:**<br>
Uma frase indicando a situação do aluno a quem pertencem as notas da entrada. A situação pode ser 'aprovado', 'reprovado' ou 'talvez com a sub', sem os apóstrofos e completamente em minúsculo. Veja nos exemplos como a saída deve ser exibida.<br>

Exemplo Input |Exemplo Output
:-------------|:-------------
6.00<br>6.00  |aprovado
5.95<br>7.34  |aprovado
10.00<br>0.00 |talvez com a sub
0.00<br>10.00 |reprovado
4.65<br>4.54  |talvez com a sub
1.99<br>0.00  |reprovado

[Voltar ao topo](#anchortextTopo)<br>

#

## <a id="anchortext07"/>Exercicio 07 - Triângulo alfabético

Como dito por um importante personagem de um igualmente memorável filme: "palavras são, na minha nada humilde opinião, nossa inesgotável fonte de magia [...]". Evidentemente, seria difícil formar palavras se não houve uma alfabeto bem estabelecido e divulgado, assim como em nosso alfabeto latino.

O alfabeto latino é composto por letras, começando em 'A' e encerrando em 'Z'. São vinte e seis caracteres diferentes, se desconsiderarmos as acentuações e as diferenças entre letras maiúsculas e minúsculas.

Harry, um garoto muito estudioso, percebeu que é possível inclusive desenhar usando letras. Em um dos desenhos, Harry escreve na primeira linha de uma folha o primeiro caractere do alfabeto, na segunda linha escreve duas vezes o segundo caractere, na terceira linha escreve três vezes o terceiro caractere e assim por diante. Harry percebeu que com isso consegue formar um triângulo alfabético, semelhante ao visto abaixo:

<img align="center" alt="Python" height="200" width="130" src="https://imgur.com/UqXhAuq.jpg"><br>

Como Harry precisa estudar para realizar uma prova de programação (que para ele também é uma forma de magia!), pediu para você ajudá-lo a automatizar os desenhos de "triângulos alfabéticos", criando um programa que receba como entrada um número inteiro N (1 <= N <= 26) e que desenhe um triângulo com exatas N linhas, seguindo a mesma estratégia descrita no texto.

### **Entrada:**<br>
Um número inteiro N (1 <= N <= 26).

### **Saída:**<br>
Um triângulo alfabético com exatas N linhas e com a mesma estratégia de construção mencionada no texto. Note que as letras são sempre maiúsculas.

Exemplo Input          |Exemplo Output
:----------------------|:----------------------
1                      |A
4                      |A<br>BB<br>CCC<br>DDDD<br>
3                      |A<br>BB<br>CCC

[Voltar ao topo](#anchortextTopo)<br>

#

## <a id="anchortext08"/>Exercicio 08 - Doação

Ao perceber que um de seus amigos estava com dificuldades financeiras, Victória, uma garota muito inteligente, decidiu ajudá-lo com uma "vaquinha digital", em que todos poderiam doar quanto pudessem para ajudar seu amigo.

Para isso, Victória criou uma criptomoeda, a Vic Coin, em que cada unidade equivale à R$ 2,50. Assim, as pessoas que doarão primeiro compram a criptomoeda e, em seguida, depositam uma parte delas para doação. A parte que não foi doada pode ficar guardada em uma carteira digital e poderá ser usada no futuro para outras doações. Genial!

Victória está ocupada implementando o que é necessário para o funcionamento do ambiente de doações, por isso pediu para que você a ajudasse com uma das partes essenciais: a contabilização de doações e a conversão para reais.

Seu papel é criar um programa que receba como entrada diversas doações feitas em Vic Coin e, ao final, exiba o total em Vic Coin (VC$) e o total convertido para reais (R$).

### **Entrada:**<br>
Diversos números reais, um por linha, que representam os valores das doações feitas em Vic Coin. A entrada será finalizada com o valor de doação -1.0 que não deverá ser contabilizado na soma das doações.

### **Saída:**<br>
Duas linhas. A primeira linha será um valor real com duas casas decimais indicando o total doado em Vic Coin (VC$); a segunda linha será um valor real com duas casas decimais que indica o total doado em reais (R$). Veja nos exemplos o formato de saída.

Exemplo Input |Exemplo Output
:-------------|:-------------
1.0<br>-1.0   |VC$ 1.00<br>R$ 2.50
-1.0          |VC$ 0.00<br>R$ 0.00
5.0<br>15.0<br>10.0<br>-1.0 |VC$ 30.00<br>R$ 75.00

[Voltar ao topo](#anchortextTopo)<br> 
