import math

a = int(input('Dime un número entero'))
b = int(input('Dime otro número entero'))
c = int(input('Dime un último número entero'))
e = (b**2)-(4*a*c)

if e >= 0:
    x1 = (-b+math.sqrt(e))/2*a
    x2 = (-b-math.sqrt(e))/2*a
    print('Las soluciones son:',x1, 'y',x2)
else:
    print('No se puede realizar esta operación')