n = 10
arr = [[0 for i in range (n)] for j in range (n)]

for i in range(n):
    for j in range(n):
        arr[0][0] = 1
        arr[3][5] = 3
        arr[4][5] = 3
        arr[5][5] = 3
        arr[7][9] = 2
        arr[8][9] = 2
        arr[9][9] = 2
        print(arr[i][j], end=' ')

    print( )
print('new array')
for i in range(n):
    for j in range(n):
        if i == j:
            if arr[i][j] != 3:
                arr[i][j] = 1
            else:
                arr[i][j-1] = 1
        elif i != j:
            if arr[i][j] == 3:
                arr[i][j-1] == 1
           # elif arr[i][j] == 3:
               # arr[i+1][j] =1
        else:
            arr[i][j] = 1
            #arr[i+1][j]=1

               # arr[i+2][j] = 1
            #elif arr[i][j] != 3:
              #  arr[i][j] = 1
                #arr[i][j-3]=1
        #else:
            #arr[i-1][j-1]=1


                #arr[i+1][j]=1

        print(arr[i][j], end=' ')
    print()


    # for i in range(n):
    #    for j in range(n):
    #        print(arr[i][j], end=' ')
    #    print( )

        #while arr [i+1][j] != 2:
           # if arr[i+1][j] == 3:
            #    arr[i-1][j] =1
            #else:
             #   arr[i+1][j] = 1
            #arr[i+1][j]=1
        #print(arr[i][j], end=' ')
    #print()

#m = 10
#a = []
#for i in range(n):
#    a.append([0] * m)
#    print(a[i])
#for j in range(n):
#    if a[i][j] == [0][9]:
#        print(a[0][9] == 1, " = начало")

