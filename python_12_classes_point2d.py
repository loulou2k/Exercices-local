# vos import ici
import math
class Point2D(object):
    """Point du plan cartÃ©sien

    >>> p1 = Point2D(3, 4)
    >>> p1.x
    3
    >>> p1.y
    4
    >>> print(p1)
    Point2D(3,4)
    >>> p2 = Point2D()
    >>> p2.x
    0
    >>> p2.y
    0
    >>> print(p2)
    Point2D(0,0)
    >>> p1.move(1,1)
    >>> p1.x
    4
    >>> p1.y
    5
    >>> print(p1)
    Point2D(4,5)
    >>> p1.distance(p2)
    6.4031242374328485
    """
    # attributs et mÃ©thodes ici...
    def __init__(self, x=0,y=0):
        """Constructeur

        Args:
            x (int, optional): Defaults to 0.
            y (int, optional): Defaults to 0.
        """
        self.x = x
        self.y = y

    def move(self, dx=0, dy=0):
        """dÃ©place le point

        Args:
            dx (int, optional): incrÃ©ment de translation. Defaults to 0.
            dy (int, optional): incrÃ©ment de translation. Defaults to 0.
        """
        self.x = self.x + dx
        self.y = self.y + dy

    def __str__(self):
        """description string

        Returns:
            str: description
        """
        return f"Point2D({self.x},{self.y})" 

    def distance(self, other):
        """Distance entre 2 points

        Args:
            other (Point2D): point de rÃ©fÃ©rence

        Returns:
            float: distance au point de rÃ©fÃ©rence
        """
        assert isinstance(other, Point2D)
        Dx = other.x - self.x
        Dy = other.y - self.y

        return math.hypot(Dx, Dy)
def main():
    X = Point2D(4,3)
    Y = Point2D(5,4)
    
    X1 = Point2D.distance(X,Y)
    print(X1)

if __name__ == "__main__":
        main()