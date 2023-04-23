size=int(input("Enter the size of the array"))
arr1=[]
arr2=[]
for i in range(size):
    ele=int(input("Enter the element followed by the return key:"))
    arr1.append(ele)
    arr2.append(ele)
newElement=int(input("Enter the new element:"))
arr2.append(newElement)
print("old array:",arr1)
print("new array:",arr2)

