def compare(x):
    if x.isdigit():
        x = int(x)
        result = comparador(x)
        print(result)   
    elif x.replace('.', '', 1).isdigit():
        x = float(x)
        print('ingresa un numero entero SIN DECIMALES')
    else:
        print('ingresa un numero, no texo ☺️')

comparador = lambda x : 'El numero PAR' if x % 2 == 0 else 'El numero es INPAR'
number = input('ingrese un numero entero 👉 ')
print('')
compare(number)
print('')
print('*' * 20)
print('')

'''
Desarrolle un algoritmo que le permita determinar de una lista de números:
b.1. ¿Cuántos están entre el 50 y 75, ambos inclusive? b.2. ¿Cuántos mayores de 80?
b.3. ¿Cuántos menores de 30?
El algoritmo debe finalizar cuando n (el total de números de la lista), sea igual a 0.

mi_lista = [1, 2, 3, 2, 4, 2, 5]

valor_a_contar = 2
cantidad = mi_lista.count(valor_a_contar)

print(f"El valor {valor_a_contar} aparece {cantidad} veces en la lista.")
'''
def espacio():
    print('')
    print('*' *20)
    print('')

def n50_75(x):
    number = 0
    for i in x:    
        if i >= 50 and i <= 75:
            number += 1
    return number

def mayor80(x):
    number = 0
    for i in x:    
        if i >= 80:
            number += 1
    return number

def menor30(x):
    number = 0
    for i in x:    
        if i <= 30:
            number += 1
    return number
   

lista = [x for x in range(1,101)]
print(lista)
espacio()

conteo = n50_75(lista)
print('el numero de numeros entre 50 y 75 son 👉', conteo)
espacio()

conteo = menor30(lista)
print('los numeros menores a 30 son 👉', conteo)
espacio()

