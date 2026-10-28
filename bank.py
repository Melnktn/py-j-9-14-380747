

transactions = []
balance = 0

while True :
    main_menu = input("1.variz pool 2.bardasht pool 3.show mojodi 4.show tarakonesh 5.show mojodi variziha 6.exit:" )
    while True :
        match main_menu :
            case "1" :
                variz_pool = int(input("pool ro variz kon :"))
                if variz_pool>0 :
                    balance += variz_pool
                    transactions.append(+variz_pool)
                else :
                    print("mablagh bayad mosbat bashe ")
                break

            case "2" :
                bardasht_pool = int(input("pool ro bardasht kon:"))
                if bardasht_pool>0 and bardasht_pool>=balance :
                    balance -= bardasht_pool
                    transactions.append(-bardasht_pool)
                else :
                    print("mojodit tah keshide dash ")
                break

            case "3" :
                print(balance)
                break

            case "4" :
                print(transactions)
                break

            case "5" :
                sum_variziha = 0
                for i in transactions :
                    if i >0 :
                        sum_variziha += i
                        print(sum_variziha)
                        break
            case "6" :
                break
                    


                    
             