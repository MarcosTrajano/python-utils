# -*- coding: utf-8 -*-
#Esse script tem como objetivo mostrar as possiveis formas
#de se usar o while na linguagem Python
#Autor: Marcos Trajano
#Data: 02 de maio de 2015

#enquanto x for maior que 10
#sera impresso o valor de x
#e em seguida esse valor e decrementado 
#em menos um ao final é impresso 
#o nome fim

x = 20
while x > 10:
	print(x)
	x = x - 1
print('fim')

#neste caso sera impresso todos os numeros
#de 0 a 10 inclusive o 10
x = 0
while x <= 10:
	print(x)
	x=x+1 
#neste caso a incrementação vem antes da impressao
#logo nao sera impresso o 0 e sera impresso o 10 
#mesmo que nao o inclua na condicao
x = 0
while x < 10:
	x=x+1
	print(x)

#neste caso os numeros pares de 0 a 8
#sao adicionados em uma lista e so serao
#impressos apos as iteracoes
nums = list()
x = 0
while (x <=9) :
	nums.append(x)
	x = x + 2
print(nums)