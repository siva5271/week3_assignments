for i in range(3,-1,-1):
    for j in range(1,i+2):
        print(int((i*(i+1)/2)+j),end=" "),
    print()