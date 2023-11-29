from vecteur2D import vecteur2D
from vecteur3D import vecteur3D

per1 = vecteur2D(2,3)
per2 = vecteur2D(2,3)

print(per1.tostring())
print(per2.tostring())
print(per1.norme())
print(per1.equals(per2))

stg1 = vecteur3D(3,6,2)
stg2 = vecteur3D(5,8,1)

print(stg1.tostring())
print(stg2.tostring())
print(stg1.norme())
print(stg1.equals(stg2))