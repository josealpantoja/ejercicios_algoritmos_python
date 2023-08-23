
print('')
print('*' * 20)
print('')

print('🚨1️⃣  Determinar la hipotenusa de un triángulo rectángulo conocidas las longitudes de sus dos catetos. Desarrolle el algoritmo correspondiente.')
print('')

catA = input('Escoje el cateto A de un triángulo 👉 ')
catB = input('Escoje el cateto A de un triángulo 👉 ')

catA = int(catA)
catB = int(catB)

print('')
for i in range(0,catA):
    print('🟨' * catA)
print('')
print('✚')
print('')
for i in range(0,catB):
    print('🟦' * catB)
print('')

hipotenusa = (catA ** 2 + catB ** 2) ** 0.5
print(hipotenusa)

print('=')
print('')
dib_catA = int(hipotenusa - catB)

for i in range(0, catB):
    print('🟦' * catB,'🟨' * dib_catA) 
for i in range(0, dib_catA):
    print('🟨' * catB, '🟨' * dib_catA) 

print('')
print('*' * 20)
print('')
for i in range(0,int(hipotenusa)):
    print('🟥' * int(hipotenusa))
        
print('')
print('👇' * 20)
print('')
for i in range(0,int(hipotenusa)):
    if i == 0:
        print('🟩' * int(hipotenusa))
    else:
        print('🟥' * int(hipotenusa))

print('')
print('Entonces...')
print('La Hipotenusa de un trianculo rectangulo cuyo Cateto A es', catA, 'y cateto B es', catB, 'es 👉 ', hipotenusa)

print('')
print('*' * 20)
print('')
print('')

print('🚨2️⃣  Desarrollar un algoritmo que calcule el área de un cuadrado.')
print('')

area = hipotenusa * hipotenusa
area_sting = str(area) + ' unidades^2'

print('El área del cuadrado de la hipotenusa:', hipotenusa, 'es 👉', area_sting)