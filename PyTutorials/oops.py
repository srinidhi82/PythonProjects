class computer():

    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram


    def config(self):

        print("COnfig is "  + self.cpu + " & " + str(self.ram))

comp = computer('i8',8)
comp2 = computer('i6',16)

comp.config()
comp2.config()
