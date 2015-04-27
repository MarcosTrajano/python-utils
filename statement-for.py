# -*- coding: utf-8 -*-
#Esse script tem como objetivo mostrar as possiveis formas
#de se escrever for na linguagem Python
#Autor: Marcos Trajano
#Data: 26 de abril de 2015

#Enquanto o x estiver dentro do intervalo de 0 a 3
#sera impresso na tela os numeros desse intervalo
#neste caso vai de 0 a 2
for x in range(0, 3):
	print (x)

#usando uma variavel como intervalo para o x
#a saida sera os caracteres da variavel
#com uma quabra de linha apos cada caracter
string = "Hello World"
for x in string:
	print (x)

#usando uma colecao como intervalo para o x
collection = ['ola', 5, 4.5, 'm']
for x in collection:
	print (x)

#Acessando lista dentro de lista
#usando um for dentro de outro
list_of_list = [[1,2,3], [4,5,6],[7,8,9]]
for x in list_of_list:
	for y in x:
		print (y)

#Usando if dentro do for
#com um break como condicao de parada.
#so executara o break quando x for igual
#a 1
for x in range(3):
	if x == 1:
		break