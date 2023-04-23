def main():
    arr=[]
    size=0
    def getArray():
        nonlocal arr
        nonlocal size 
        size= int(input("Enter the size of the array"))
        for i in range(size):
            arr.append(int(input("Enter each element followed by the return key")))
    def displayArray():
        nonlocal arr
        for x in arr:
            print(x," ")
    getArray()
    displayArray()

main()