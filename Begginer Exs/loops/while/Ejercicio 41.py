respuesta = 'S'

while respuesta == 'S':
    año = int(input('Dime un año')) 

    if año%4==0:
        print('Ese año es bisiesto')
    else:
        print('ese año no es bisiesto')

    respuesta = (input('¿Quieres que te diga si otros año?(S/N)'))

print('¡Gracias por usar nuestro programa!')