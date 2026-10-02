


for i in range(1,10):

    for j in range(1,10):

        if j <= i and i+j <= 10 and (j == 1 or j == i or i+j == 10)  : 

            print("*" , end=" ")

        else:
             print(" " , end=" ")

    print()          