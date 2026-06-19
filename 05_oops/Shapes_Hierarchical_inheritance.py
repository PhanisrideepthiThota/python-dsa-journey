#hierarchical inheritance
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
    
class Sphere(Circle):
    def __init__(self,radius):
        
        super().__init__(radius)
        
    def volume(self):
        return (4/3)*3.14*self.radius*self.radius*self.radius
    
class Cylinder(Circle):
    def __init__(self,radius,height):
        super().__init__(radius)
        self.height=height
    def vol_cyclinder(self):
        return 3.14*self.radius*self.radius*self.height
  
       

c=Cylinder(6,2)
r=Sphere(4)

print("Area of the circle:",r.area())
print("Volume of Sphere : ",r.volume())
print("Volume of the cylinder:",c.vol_cyclinder())

