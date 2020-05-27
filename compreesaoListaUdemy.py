separe=("======================")
"""x = [1,2,3,4,5]
y = []

for i in x:
	y.append(i**2)
	
print(x)
print(y)

print("Usando list comprehension")
x = [1,2,3,4,5]
y = [i**2 for  i in x]
z = [i for i in x if i%2==1]
	
print(x)
print(y)
print("Apanas ímpa")
print(z)
print(separe)"""
	
"""l = ['abacate', 'bola','cachoro']
for i in l:
		print(i)
for i in range(len(l)):
		print(i,l[i])"""

print("Com o enumerate")
l2 = ["abacate", "Cacau",'uva']
for i, nome in enumerate(l2):
	print(i,nome)