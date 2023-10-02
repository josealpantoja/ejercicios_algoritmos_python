import time
'''
El módulo time en Python proporciona funciones relacionadas con el tiempo y el reloj. Se puede utilizar este módulo para realizar diversas operaciones relacionadas con el tiempo, como medir el tiempo que lleva ejecutar una porción de código, pausar la ejecución del programa durante un período específico o trabajar con representaciones de fecha y hora.
'''
separador = '*' * 30 #esta variable solo es con fines estéticos, imprimir * como separadores.

def minuto_ciclo(minutos):
    '''
    Esta función cuenta los minutos, usaremos el método sleep del módulo time, para esperar 1 segundo.
    
    :hora_local.tm_sec Extraemos los segundos de la hora local
    '''
    hora_local = time.localtime()  # Obtiene la estructura de tiempo para la hora local
    #segundos = hora_local.tm_sec # Extraemos los segundos de la estructura de tiempo
    segundos = 0
    while segundos < 59:
        hora_local = time.localtime()
        segundos = hora_local.tm_sec
        #segundos += 1
        print(f'{segundos} segundos')
        time.sleep(1) #es para que espere 1 segundos para supervisar el local time
    return minutos + 1
    
def hora_ciclo(horas):
    minutos = 0
    while minutos < 59:
        minutos = minuto_ciclo(minutos)
        hora_formateada = imprime_hora_local() #extraemos la hora local para imprimirla cada minuto
        print(f'{separador} {minutos} minutos, la hora es: {hora_formateada} {separador}')
    return horas + 1

def dia_ciclo(dia):
    horas = 0
    while horas < 24:
        horas = hora_ciclo(horas)
        if horas < 24:
            hora_formateada = imprime_hora_local()
            print(f'{separador} {horas} horas, la hora es: {hora_formateada} {separador}')
        else:
            hora_formateada = imprime_hora_local()
            print(f'{separador} {dia} dias, la hora es: {hora_formateada} {separador}')
    return dia + 1

def run(dia):
    dia = dia_ciclo(dia)
    if dia < 993:
        run(dia) #la función run() se vuelve a llamar a si misma de forma infinita. OJO en el día 993 se quiebra el programa
    else:
        print('holis')
        time.sleep(4) #es para que espere 1 segundos para supervisar el local time
        run(dia = 0) # reseteamos la variable dia, para que el reloj sea infinito PERO NO FUNCIONO ¿me ayudan?

def imprime_hora_local():
    hora_local = time.localtime()  # Obtiene la estructura de tiempo para la hora local
    hora_formateada = time.strftime("%Y-%m-%d %H:%M:%S", hora_local) # Formatea la hora como una cadena
    return hora_formateada

print("Hora local actual:", imprime_hora_local())
run(dia = 0)
