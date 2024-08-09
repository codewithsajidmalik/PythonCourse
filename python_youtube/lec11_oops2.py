class car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False


    def start(self):
         self.clutch = True #abstaction
         self.acc = True #abstaction
         print("start the car ........")




car1  = car()
car1.start()   
        