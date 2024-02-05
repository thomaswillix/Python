table = 7

for i in range(1,13):

    print('¿Cuánto es ',i,'x',table,'?')
    calculo = input ()

    respuesta = i*table

    if int(calculo)==respuesta:
        print('¡Correcto!')
    else:
        print('No, es ',respuesta)

print('Fin')