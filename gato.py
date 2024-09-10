
class Gato:

    #El constructor en python siempre se llama __init__()
    def __init__(self,name:str,sex:str,age:int,weight:int,color:str,texture:str):
        #En el constructor se definden e instancian los atributos del obj
        self.name=name
        self.sex=sex
        self.age=age
        self.weight=weight
        self.color=color
        self.texture=texture
 
    def eat(self, comida:str):
        print(self.name + " va a comer: " +  comida)
    
    def move(self):
        print(self.name + " Se va a mover")

    def meow(self):
        print(self.name + " Hace meow")

    def purr(self):
        print(self.name + " ronrronea")

    def huntMice(self):
        print(self.name + " caza al raton")
    
