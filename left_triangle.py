



for i in range(1,10):

    for j in range(1,10):

        if j >= 10-i and j >= i and (j == 9 or j == 10-i or j == i):

            print("*" , end=" ")

        else: 

            print(" " , end=" ") 

    print()           