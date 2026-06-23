class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,p1):
        p3=Point(0,0)
        p3.x=self.x+p1.x
        p3.y=self.y+p1.y
        return p3

p11=Point(2,4)
p22=Point(12,14)

p33=p11+p22

print(p33.x,",",p33.y)
