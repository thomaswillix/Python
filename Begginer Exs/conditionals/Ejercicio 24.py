lado1=int(input('Dime la medida de un lado'))

lado2=int(input('Dime la medida de otro lado'))

lado3=int(input('Dime la medida de su tercer lado'))

if lado1 == lado3 ==lado2:
    print('El triángulo es equilátero')
elif ((lado2==lado1) and (lado2!=lado3)) or ((lado1==lado3) and (lado1!=lado2)):
    print('El triángulo es isóceles')
elif lado1 != lado2 != lado3 :
    print('el triángulo es escaleno')