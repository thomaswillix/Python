edad = input('Hola, ¿cuántos años tienes? ')

edad =int(edad)

nacionalidad = input ('¿Eres estadounidense?(S/N) ')

if edad >= 16 and nacionalidad==('s'):
    print('Puedes conducir dentro de EE.UU')
else:
    if edad >= 18 and nacionalidad ==('n'):
        print('Puedes conducir fuera de EE.UU')
    if edad <= 17:
        print('No puedes conducir')