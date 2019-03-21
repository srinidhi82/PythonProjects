class computer():

    def __init__(self):
        self.name = 'Sri'
        self.age = 36


    def update(self):
        self.age = 37

    def compare(self,other):
            if self.age == other.age:
                return True
            else:
                return False
c1 = computer()
c2 = computer()

if c2.compare(c1):
    print("Age is same")

c1.age = 30

c2.update()
print(c1.age)

print (c2.age)

