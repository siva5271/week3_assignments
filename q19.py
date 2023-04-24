class ArrayOperations:
    def getArray(self):
        global size
        arr=[]
        for i in range(size):
            print("Enter array number ",i+1)
            temp=[]
            for j in range(size):
                temp.append(int(input("Enter each element followed by the return key")))
            arr.append(temp)
        return arr
    def addArray(self,arr1,arr2):
        for i in range(size):
            global result
            resultTemp=[]
            for j in range(size):
                resultTemp.append(arr1[i][j]+arr2[i][j])
            result.append(resultTemp)
    def displayArray(self,res):
        global size
        for i in range(size):
            for x in res[i]:
                print(x,end=" ")
            print()

size=int(input("Enter the size of the array"))
obj=ArrayOperations()
arr1=obj.getArray()
arr2=obj.getArray()
result=[]
obj.addArray(arr1,arr2)
obj.displayArray(result)