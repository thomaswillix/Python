numero1 = input('Dime un núero entero')
numero1 = int(numero1)

numero2 = input('Dime otro número')
numero2 = int(numero2)

if numero1>numero2:
    print('El primer número es mayor que el segundo')
elif numero2>numero1:
    print('El segundo número es mayor que el primero')
elif numero1 == numero2:
    print('Los dos números son iguales')