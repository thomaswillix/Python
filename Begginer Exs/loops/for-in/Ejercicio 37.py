import time
print('Bienvenidos a las campanadas de 2020')

numero = int(input('¿Cuánto tiempo quieres que pase entre campanada y campanada?:'))
for i in range(1,13,1):
    print('dong')
    time.sleep(numero)
    
print('¡Feliz año nuevo!')
