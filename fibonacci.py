numeros = int(raw_input("Cantidad de numeros: "))
a = 0
b = 1
print("La serie de fibonacci de los "+ str(numeros) +" primeros numeros es:")
for i in range(numeros):
	print str(b)+",",
	a = b
	b = a + b
raw_input()