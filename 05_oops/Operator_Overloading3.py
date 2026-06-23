class Point:
    def __init__(self,x,y):
        self.x=x 
        self.y=y
    #Magic method,/special methods
    def __add__(self,p):
        return Point(self.x+p.x,self.y+p.y)
    def __sub__(self,p):
        return Point(self.x-p.x,self.y-p.y)
    def __mul__(self,p):
        return Point(self.x*p.x,self.y*p.y)
    def __truediv__(self,p):
        return Point(self.x/p.x,self.y/p.y)
    def display(self):
        print(self.x,self.y)
        
p1=Point(2,4)
p2=Point(3,6)
print("Point 1:")
p1.display()
print("Point 2:")
p2.display()
print("Addition:")
(p1+p2).display()
print("Subtraction:")
(p1-p2).display()
print("Multiplication:")
(p1*p2).display()
print("Division:")
(p1/p2).display()
