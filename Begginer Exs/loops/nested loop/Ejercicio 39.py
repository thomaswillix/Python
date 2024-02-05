print('Este programa calcula las tablas de multiplicar')

respuesta = 'S'

while respuesta =='S':
    tabla=int(input('¿De qué numero quieres averiguar su tabla de multiplicar?'))

    for a in range(1,11):
        print(tabla,'x',a,'=',tabla*a)

    respuesta = input('¿Quieres seguir calculando otras tablas? (S/N)')

print('FIN')