from abc import ABC,abstractmethod

class methods(ABC):
    @abstractmethod
    def addition(self,num1,num2):
        pass

    @abstractmethod
    def subtraction(self,num1,num2):
        pass

    @abstractmethod
    def multiplication(self,num1,num2):
        pass

    @abstractmethod
    def division(self,num1,num2):
        pass

class definition(methods):
    def addition(self, num1, num2):
        sum=num1+num2
        return sum
    
    def subtraction(self, num1, num2):
        result=num1-num2
        return result
    
    def multiplication(self, num1, num2):
        result=num1*num2
        return result
    
    def division(self, num1, num2):
        result=num1/num2
        return result
    
num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
obj=definition()
print("Sum:",obj.addition(num1,num2))
print("Difference:",obj.subtraction(num1,num2))
print("Product:",obj.multiplication(num1,num2))
print("Quotient:",obj.division(num1,num2))