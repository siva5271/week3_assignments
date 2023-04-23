arr=[20, 10, 50, 30, 40]
def selectionSort(arr):
    for i in range(len(arr)):
        flag=i
        for j in range(i,len(arr)):
            if(arr[j]>arr[flag]):
                flag=j
        temp=arr[flag]
        arr[flag]=arr[i]
        arr[i]=temp
    print(arr)

selectionSort(arr)