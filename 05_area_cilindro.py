import math

print('')
print('*' * 20)
print('')

print('🚨1️⃣  Desarrolle un algoritmo que permita determinar el área y volumen de un cilindro dado su radio (R) y altura (H).')
print('')

radio = float(input('Escribe el radio del cilindo 👉 '))
altura = float(input('Escribe la altura de un cilindo 👉 '))

area = math.pi * radio ** 2
area_l = 2 * math.pi * radio * altura
area_superficie = area + area_l
volumen = area * altura

print('')
print('*' * 20)
print('')
print('El área de la base del cilindro es', area, 'unidades^2, el área lateral es', area_l, 'unidades^2, por lo que el area de la superficie o área total es de', area_superficie)
print('')
print('El volumen del cilindo es 👉 ', volumen, 'unidades^3')