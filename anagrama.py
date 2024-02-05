print("Introduce dos palabras y observaremos si son anagramas entre sí ")
c1 = input("Dame la primera palabra ")
c1 = c1.lower()
c2 = input("Ahora la segunda ")
c2 = c2.lower()

if (len(c1) == len(c2)):

    letras = {}
    for letra in c1:
        i = letras.get(letra, 0)   
        i+=1
        letras.update({letra: i})
    
    letras2 = {}
    for letra in c2:
        i = letras2.get(letra, 0)   
        i+=1
        letras2.update({letra: i})

    if letras == letras2:
        print("Las palabras son anagramas entre sí")
    else:
        print("Las palabras no son anagramas")
else:
    print("Las palabras no tienen la misma longitud")
