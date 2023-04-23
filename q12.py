size=int(input("Enter the size of the arrays"))
arr1=[]
for i in range(size):
    print("Enter array 1-d number ",i+1)
    temp=[]
    for j in range(size):
        temp.append(int(input("Enter each element followed by the return key")))
    arr1.append(temp)
print("Now for the second 2-d array")
arr2=[]
for i in range(size):
    print("Enter array 1-d number ",i+1)
    temp=[]
    for j in range(size):
        temp.append(int(input("Enter each element followed by the return key")))
    arr2.append(temp)
result=[]
for i in range(size):
    resultTemp=[]
    for j in range(size):
        resultTemp.append(arr1[i][j]+arr2[i][j])
    result.append(resultTemp)
print(result)