#Ejercicio 1
print('')
print('EJERCICIO 1')
print('')
print('🚨 Desarrolle un algoritmo que realice la sumatoria de los números enteros comprendidos entre el 1 y el 10, es decir, 1 + 2 + 3 + .... + 10.')
print('')
print('*' * 20)
print('')


numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
n = 0

for i in numbers:
    n = n + i

print('El resultado de la sumatoria de', numbers, 'es', n)

print('')
print('*' * 20)
print('')

#Ejericcio 2

print('')
print('EJERCICIO 2')
print('')
print('🚨 Desarrolle un algoritmo que realice la sumatoria de los números enteros múltiplos de 5, comprendidos entre el 1 y el 100, es decir, 5 + 10 + 15 +.... + 100. El programa deberá imprimir los números en cuestión y finalmente su sumatoria')
print('')
print('*' * 20)
print('')

multiple = 5
i = 1
sum = 0

while multiple < 100:

    multiple = i * 5
    i += 1
    sum = sum + multiple
    print(multiple)


print('La suma de los multimos del 5 entre el 1 y el 100 es 👉 ', sum)

print('')
print('*' * 20)
print('')

#Ejericcio 3
print('')
print('EJERCICIO 3')
print('')
print('🚨 Desarrolle un algoritmo que realice la sumatoria de los números enteros pares comprendidos entre el 1 y el 100, es decir, 2 + 4 + 6 +.... + 100. El programa deberá imprimir los números en cuestión y finalmente su sumatoria')
print('')
print('*' * 20)
print('')

multiple = 2
i = 1
sum = 0

while multiple < 100:

    multiple = i * 2
    i += 1
    sum = sum + multiple
    print(multiple)

print('La suma de los multimos del 2 entre el 1 y el 100 es 👉 ', sum)

print('')
print('*' * 20)
print('')


#EJERCICIO 4


print('')
print('EJERCICIO 4')
print('')
print('🚨 Desarrolle un algoritmo que lea los primeros 300 números enteros y determine cuántos de ellos son impares; al final deberá indicar su sumatoria.')
print('')
print('*' * 20)
print('')

sum = 0
for i in range(1, 31):
    if (i / 2) - float(i // 2) == 0.5:
        print(i)
        sum = sum + i

print('')
print('La sumatoria de los números inpares del 1 al', i, 'es 👉', sum)

print('')
print('*' * i)
print('')

#EJERCICIO 4


print('')
print('EJERCICIO 4-B')
print('')
print('🚨 Usando list comprehension')
print('')
print('*' * 20)
print('')

suma = 0
impares = [i for i in range(1, 31) if i % 2 != 0]
for n in impares:
    suma = suma + n

print('')
print(impares, 'La sumatoria de los números inpares del 1 al', i, 'es 👉', suma)