#para utilizar las clases se deben importar al archivo
#from archivo import clase


from gato import Gato

if __name__ == "__main__":
    #Para instanciar un ojb debemos usar el constructor
    gato1 = Gato("Garfield", "Macho", 60, 30, "Naranjo", "Esponjoso")

    print("El gato se llama: " + gato1.name)
    gato1.eat("Lassagna")
    gato1.move()
    gato1.meow()
    gato1.purr()
    gato1.huntMice()
