# Calculadora Intergaláctica
Trata-se de um desafio de programação que consistia em uma calculadora de números romanos para transações intergalácticas desenvolvido em python3.

Para utilizar o programa, salve o arquivo de texto referente à conversão entre unidades intergalácticas e numerais romanos na mesma pasta que contém o programa.

As entradas para o programa consistem de linhas de texto em um arquivo texto detalhando as anotações sobre a conversão entre unidades intergalácticas e numerais romanos.
Como se pode ver abaixo, as entradas podem ter até 7 linhas iniciais indicando a notação intergaláctica dos símbolos romanos, seguida de 0 ou mais linhas indicando o valor em créditos do número de unidades (expresso em intergaláctico) de metal sendo vendido. Na sequência, linhas com perguntas “quanto vale” / ”quantos créditos são”. Na última linha, um exemplo do que deve acontecer com uma anotação inválida.

Exemplo de arquivo de entrada:

------------

snob representa I
                
krok representa V
                
squid representa X
                
leij representa L
                
snob snob Silver valem 34 créditos
                
snob krok Gold valem 57800 créditos
                
squid squid Iron valem 3910 créditos
                
quanto vale squid leij snob snob ?
                
quantos créditos são snob krok Silver ?
                
quantos créditos são snob krok Gold ?
                
quantos créditos são snob krok Iron ?
                
quanto vale wood could woodchuck mood ?

------------


Exemplo de arquivo de saída:
------------
squid leij snob snob vale 42
snob krok Silver custa 68 créditos
snob krok Gold custa 57800 créditos
snob krok Iron custa 782 créditos
Nem ideia do que isto significa!
------------
