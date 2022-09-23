from zooAnimales.animal import Animal
class Mamifero(Animal):
    listado=[]
    caballos=0
    leones=0
    def __init__(self, nombre, edad, habitat, genero,pelaje,patas):
        super().__init__(nombre, edad, habitat, genero)
        Animal.mamifero+=1
        self.pelaje=pelaje
        self.patas=patas
        self.listado.append(self)
    def cantidadMamifero(self):
        return len(self.listado)
    def crearCaballo(self,nombre,edad,s):
        Mamifero.caballos+=1
        return Mamifero(nombre,edad,"pradera",s,True,4)
    def crearLeon(self,nombre,edad,sexo):
        self.leones+=1
        return Mamifero(nombre,edad,"selva",sexo,True,4)
    def isPelaje(self):
        return self.pelaje
    def getPatas(self):
        return self.patas