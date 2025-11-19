# vos imports ici
import math
from python_12_classes_point2d import Point2D

class Vector2D(object):
    """
    Vecteur dans un plan
    >>> O = Point2D()
    >>> A = Point2D(1, 0)
    >>> B = Point2D(1, 1)
    >>> C = Point2D(0, 1)
    >>> v1 = Vector2D(O,A)
    >>> v2 = Vector2D(O,B)
    >>> v3 = Vector2D(O,C)
    >>> print(v1)
    Vector2D(1,0)
    >>> print(v2)
    Vector2D(1,1)
    >>> print(v3)
    Vector2D(0,1)
    >>> print(abs(v1))
    1.0
    >>> print(abs(v2))
    1.4142135623730951
    >>> print(-v1)
    Vector2D(-1,0)
    >>> print(v1+v2)
    Vector2D(2,1)
    >>> print(v1+v3)
    Vector2D(1,1)
    >>> print(v1-v3)
    Vector2D(1,-1)
    >>> print(v1+v3 == v2)
    True
    """
    # attributs et mÃ©thodes ici...
    def __init__(self, A=Point2D(), B=Point2D()):
        self.x = B.x - A.x
        self.y = B.y - A.y
 
    def __abs__(self):
        return math.hypot(self.x, self.y)
    
    def __str__(self):
        return f"Vector2D({self.x},{self.y})"
        
    def __eq__(self, other):
        return abs(self) == abs(other)
        
    def __neg__(self):
        neg = Vector2D()
        neg.x = -self.x
        neg.y = -self.y
        return neg      
        
    def __add__(self, other):
        res = Vector2D()
        res.x = self.x + other.x
        res.y = self.y + other.y
        return res
        
    def __sub__(self, other):
        res = Vector2D()
        res.x = self.x - other.x
        res.y = self.y - other.y
        return res

def main():
    pass
    O = Point2D()
    A = Point2D(1, 0)
    B = Point2D(1, 1)
    v1 = Vector2D(O,A)
    v2 = Vector2D(O,B)
    print(v1)
    print(v2)
    print(abs(v1))
    print(abs(v2))
    print(-v1)
    print(v1+v2)

if __name__ == "__main__":
    main()