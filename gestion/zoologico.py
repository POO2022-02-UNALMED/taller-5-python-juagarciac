class Zoologico:
    def __init__(self,nombre,ubicacion):
        self.nombre=nombre
        self.ubicacion=ubicacion
        self.zonas=None
    def agregarZonas(self,zona):
        if self.zonas==None:
            self.zonas=[]
            self.zonas.append(zona)
            zona.agregarZoo(self)
        else:
            self.zonas.append(zona)
            zona.agregarZoo(self)
    def cantidadTotalAnimales(self):
        p=0
        for r in len(self.zonas):
            m=self.zonas[r].cantidadAnimales()
            p+=m
        return p 
    def getNombre(self):
        return self.nombre
    def getZona(self):
        return self.zonas