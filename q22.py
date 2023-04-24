class accountDetails:
    def __init__(self) -> None:
        self.__name=""
        self.__accountNumber=0
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,value):
        self.__name=value
    
    @property
    def accountNumber(self):
        return self.__accountNumber
    
    @accountNumber.setter
    def accountNumber(self,value):
        self.__accountNumber=value
    
obj=accountDetails()
obj.name="Siva"
obj.accountNumber=11111111
print(obj.name)
print(obj.accountNumber)