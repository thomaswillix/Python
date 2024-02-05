grade = int(input ('¿Cuál es la nota del alumno?'))

if grade>=9:
    print('Este alumno ha obtenido un "SOBRESALIENTE"')
elif grade>=7:
    print('Este alumno ha obtenido un "NOTABLE"')
elif grade>=6:
    print('Este alumno ha obtenido un "BIEN"')
elif grade>=5:
    print('Este alumno ha obtenido un "SUFICIENTE"')
elif grade<5:
    print('Este alumno ha obtenido un "INSUFICIENTE"')
