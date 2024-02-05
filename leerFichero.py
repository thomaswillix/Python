import random 

def leerGalleta():
    
    with open('mensajes.txt', "r+") as file:
        contents = file.readlines()           # reads a string from a file
    x = random (1, contents[-1])
    print(contents[x])

leerGalleta()