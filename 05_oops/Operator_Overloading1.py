class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __lt__(self,p1):
        print("Comparing...")
        return self.age<p1.age
    def __str__(self):
            return f"person(name={self.name},name={self.age})"
p1=person("Krishna",34)
p2=person("Radhe",45)
#p1.__lt__(p2)
print(p1)
print(p2)
print(p1<p2)
