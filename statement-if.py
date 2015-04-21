# -*- coding: utf-8 -*-
#Esse script tem como objetivo mostrar as possiveis formas
#de se escrever if's na linguagem Python
#Autor: Marcos Trajano
#Data: 21 de abril de 2015

val_x = 10
val_y = 20
val_z = 30

#Escrevendo apenas um statement, caso a condição seja válida,
#será impresso um texto.
if val_x == 10:
    print("O valor de X é 10")
    
#Escrevendo um statement com a captura do caso quando não 
#satisfizer a condição do statement.
if val_y < val_x:
    print("Y é menor que X")
else:
    print("X é maior que Y")
    
#Escrevendo vários statements
if val_y == val_z:
    print("Y é igual a Z")
    
elif val_y == val_x:
    print("Y é igual a X") 
    
elif val_z == val_x:
    print("Z é igual a X")
    
else:
    print("Nenhum statement foi válido!")
    
    
#Escrevendo if ternario, se o statement for válido a váriavel
#novo_val irá receber o valor da váriavel val_x, caso contrário
#receberá o valor da váriavel val_z
novo_val = val_x if val_y < val_z else val_z
print(novo_val)