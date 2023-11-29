class vecteur2D :
    _count = 0
    def __init__(self , x = 0 , y = 0 ):
        self.x = x
        self.y = y
        vecteur2D._count = vecteur2D._count + 1
    
    def getcount(self):
        return self._count
    
    def setx(self,x):
        self.x = x
    
    def getx(self):
        return self.x
    
    def sety(self,y):
        self.y = y
    
    def getx(self):
        return self.y
    
    def tostring(self):
        return ("x = " + str(self.x) + " - y = " + str(self.y))
    
    def per(self,x,y):
        self.x = x
        self.Y = y
    
    def equals(self ,per):
        if self.x == per.x and self.y == per.y :
            return True
        else:
            return False
        
    def norme(self):
        return (self.x**2 + self.y**2)**1/2
    