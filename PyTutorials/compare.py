class computer():

    def __init__(self):
        self.name = 'Sri'
        self.age = 36

    def compare(self,c2):
            if self.age == c2.age:
                return True
            else:
                return False
c1 = computer()
c1.age = 39
c2 = computer()

if c1.compare(c2):
    print("Age is same")
else:
    print("Age is different")


