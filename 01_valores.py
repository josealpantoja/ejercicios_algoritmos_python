a = 0.0
b = 0.0

a = float(input('Escribe un primer numero 👉 '))
b = float(input('Escribe un segundo numero 👉 '))

if a > b:
    print(a, 'es mayor que', b)
elif b > a:
    print(b, 'es mayor que', a)
else:
    print('Los numeros son iguales')

if a < b:
    print(a, 'es menor que', b)
elif b < a:
    print(b, 'es menor que', a)

print('La suma de los dos valores es: ', a + b)