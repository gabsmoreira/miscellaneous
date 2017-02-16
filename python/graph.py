
import math
import numpy as np
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt

print('Bem vindo ao MathSolver!')



print('Escreva os valores correspondentes à A, B e C!')

a = float(input('Valor de A:'))
b = float(input('Valor de B:'))
c = float(input('Valor de C:'))
equacao2 = a,'x² +', b,'x +', c,'= 0'
print('Equação--->', a,'x² +', b,'x +', c,'= 0')
delta1 = (b**2)-4*a*c



if a==0:
	Raiz1= -c/b
	print('A sua equação tem apenas uma raiz:',Raiz1)

else:
	if delta1<0:
		print('O delta é negativo, não existe raiz')


	if delta1==0:
		delta2 = math.sqrt(delta1)
		Raiz1 = (-b+delta2)/2*a
		print('A sua equação tem apenas uma raiz:',Raiz1)

	if delta1>0:
		delta2 = (delta1)**1/2
		Raiz1 = (-b+delta2)/2*a
		Raiz2 = (-b-delta2)/2*a
		print('A raiz 1 é',Raiz1)
		print('A raiz 2 é',Raiz2)


#rangeg1 = int(input('Ponto mínimo de seu gráfico:'))

#rangeg2 = int(input('Ponto máximo de seu gráfico:'))

listaX = np.linspace(-10,10,50)
add = 0 

    
listaY =[]
for i in (listaX):
	y = (a*(i**2)) + (b*i) + c
	listaY.append(y)
 

plt.plot(listaX,listaY)
plt.ylabel('Y')
plt.xlabel('X')
plt.grid(True)
plt.show()



#if opcao==2:


#grau = int(input('Grau do polinômio:'))

#for i in range(grau):
	#polinomio =+ 
