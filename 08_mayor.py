a = float(input('Ingresa un numero 👉 '))
b = float(input('Ingresa un numero 👉 '))

def mayor(x, y):
    if x < y:
        return x, y
    else:
        return y, x
    
def lista_100():
    x = 0
    n = [0]
    while x < 100:
        x += 1
        n.append(x)
    return n


list = []
list = mayor(a, b)
print(list)

#Lista numero naturales

list_2 = [x for x in range (0,101)]
print(list_2)

list_3 = lista_100()
print(list_3)

