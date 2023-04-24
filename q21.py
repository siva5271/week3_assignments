class Home:
    def room1(self): 
         width=100 
         breadth = 100 
         print('area of room1',width*breadth) 
    def kitchen(self): 
        width = 1222
        breadth = 4888 
        print('area of kitchen',width*breadth) 

class FirstHome(Home):
    def studyRoom(self):
        width=100
        breadth=150
        print("area of study room:",width*breadth)
    def display(self):
        self.room1()
        self.kitchen()
        self.studyRoom()

class SecondHome(Home):
    def workArea(self):
        width=80
        breadth=100
        print("area of work area:",breadth*width)
    def display(self):
        self.room1()
        self.kitchen()
        self.workArea()

objFirstHome=FirstHome()
print("Dimensions of first home is:")
objFirstHome.display()

objSecondHome=SecondHome()
print("Dimension of second home:")
objSecondHome.display()