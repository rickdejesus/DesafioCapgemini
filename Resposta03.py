
import math

s = 'tenha um bom dia'
s1 = s.replace(' ','')
t = len(s1)
raiz = round(math.sqrt(t))
lista  = []
lista1 = []
lista2 = []
lista3 = []
lista4 = []

for i in range(t):
    if i == 0 and i < raiz:

        lista.append(list(s1[i:raiz]))
    if i == 1 and i < raiz:

        lista1.append(list(s1[raiz:raiz*2]))
    if i == 2 and i < raiz:

        lista2.append(list(s1[raiz*2:raiz*3]))
    if i == 3 and i < raiz:

        lista3.append(list(s1[raiz*3:raiz*4]))
    if i == 4 and i < raiz:

        lista4.append(list(s1[raiz*4:raiz*5]))

if  t == 8:
    print(f'{lista[0][0]}{lista1[0][0]}{lista2[0][0]} {lista[0][1]}{lista1[0][1]}{lista2[0][1]} {lista[0][2]}{lista1[0][2]}')
if  t == 13:
    print(f'{lista[0][0]}{lista1[0][0]}{lista2[0][0]}{lista3[0][0]} {lista[0][1]}{lista1[0][1]}{lista2[0][1]} {lista[0][2]}{lista1[0][2]}{lista2[0][2]} {lista[0][3]}{lista1[0][3]}{lista2[0][3]}')