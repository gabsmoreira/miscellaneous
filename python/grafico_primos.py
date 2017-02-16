
import matplotlib.pyplot as plt

a= int(input('Selecione o alcance:'))
lista=[]
lista_primos=[]
x=1
y=2
while x in range(a):
	x+=1
	y=2
	while y <= x/2:
		if x%y==0:
			lista.append('np')
		y+=1

	if 'np' not in lista:
		lista_primos.append(x)
	lista=[]

print(lista_primos)

lista_x = []
for i in range (len(lista_primos)):
    lista_x.append(i)


plt.plot(lista_x,lista_primos)
plt.show()
