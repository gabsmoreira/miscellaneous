
word = input("Pesquise algo:")
lista = ['x']

def search (lista,word):
	for i in range(len(lista)):
		if word in lista[i]:
			return 1
		else:
			return 0


x = search(lista,word)
		
if x==1:
	print('True')
else:
	print('False')
