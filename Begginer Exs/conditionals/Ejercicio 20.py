# Sé que esto es horrible, lo hice cuando estaba aprendiendo a programar
# Así que se queda así para la posteridad lmao.

numero1 = input('Dime un núero entero')
numero1 = int(numero1)

numero2 = input('Dime otro número')
numero2 = int(numero2)

operacion = input ('¿Qué operación quieres realizar? (+,-,*,/,**,//,%)')


if operacion == '+':
    print(numero1,'+',numero2,'=',numero1+numero2)
elif operacion == '-':
    print(numero1,'-',numero2,'=',numero1-numero2)
elif operacion == '*':
    print(numero1,'*',numero2,'=',numero1*numero2)
elif operacion == '/':
    print(numero1,'/',numero2,'=',numero1/numero2)
elif operacion == '**':
    print(numero1,'**',numero2,'=',numero1**numero2)
elif operacion == '//':
    print(numero1,'//',numero2,'=',numero1//numero2)
elif operacion == '%':
    print(numero1,'%',numero2,'=',numero1%numero2)
else:
    print('Error')