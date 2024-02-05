numero1 = input('Dime un número entero ')
numero1 = int(numero1)

numero2 = input('Dime otro número ')
numero2 = int(numero2)

numero3 = input('Dime un último número ')
numero3 = int(numero3)

if numero1>numero2 and numero1>numero3:
    print('El primer número es mayor que los demás')
elif numero2>numero3 and numero2>numero1:
    print('El segundo número es mayor que los otros dos')
elif numero3>numero2 and numero3>numero1:
    print('El tercer número es mayor que los otros dos')
elif numero1 == numero2 == numero3:
    print('Los tres números son iguales')