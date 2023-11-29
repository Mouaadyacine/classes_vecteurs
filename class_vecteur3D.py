from vecteur2D import vecteur2D
class vecteur3D(vecteur2D):
    def __init__(self, x=0, y=0,z=0):
        super().__init__(x, y)
        self.z = z
    
    def setz(self,z):
        self.z = z
    
    def getz(self):
        return self.z
    
    def tostring(self):
        return super().tostring() + ("z = " + self.z)
    
    def equals(self, per1):
        if self.x == per1.x and self.y == per1.Y and self.z == per1.z:
            return True
        else:
            return False
    
    def norme(self):
        return (self.x**2 + self.y**2 + self.z**2)**1/2

    