#Ejercicio 1
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