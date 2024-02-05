import random

def juego(n:int):
    
    v = random.randint(1, 20) 
    i = 1
    while i < 5:
        if(n!=v):
           
            if(v>n):
                print("El número es mayor")
            else:    
                print("El número es menor")
            n = int(input())
       
        else:
            print("Valor correcto")
            break 
        i += 1
    
    print ("Has fallado " + str(i) + " número de veces")

juego(5)