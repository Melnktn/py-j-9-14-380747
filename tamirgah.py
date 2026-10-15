



while True :
    main_menu = input("1.sabtenam 2.khadamat khodro 3.exit :")
    while True :
        match main_menu :
            case "1" :
                sabtenam = input("1.esm 2.famili 3.shomare telefon 4.modele mashin 5.shomare pelak 6.rang 7.sale sakht :")
                match sabtenam :
                    case "1" :
                        esm = input("esmeto bego :")
                        if esm.isalpha()==True :
                            print("esme shoma doros ast")
                        else :
                            print("esm eshtebahe")
                            break

                    case "2" :
                        famili = input("familiti bego :")
                        if famili.isalpha()==True :
                            print("familit doroste")
                        else :
                            print("familit eshtebahe")
                            break

                    case "3" :
                        shomare_telefon = input("shomarat chande? :")
                        if shomare_telefon.isalnum()==True and len(shomare_telefon)==11 :
                            print("shomarat doroste")
                            break

                    case "4" :
                        model_mashin = input("modele morede nazareto bego :")
                        print("mrc sabt shod")
                        break

                    case "5" :
                        shomare_pelak = input("pelake madhin ra vared kon:")
                        if shomare_pelak.isalnum()==True and shomare_pelak.isdigit()==False and len(shomare_pelak)==8 :
                            print("pelak dorost vared shode")
                        else :
                            print("pelak shtebah vared sgode")
                            break

                    case "6" :
                        model = input("range morede nazareto bego :")
                        print("in rang sabt shod")
                        break

                    case "7" :
                        sale_sakht = input("sale sakht ro bezan :") 
                        if sale_sakht.isdigit()==True and len(sale_sakht)==4 :
                            if int(sale_sakht)<=1380 :
                                print("khodro yaft nashod")
                            if 1381<=int(sale_sakht)<=1405 :
                                print("khodro yaft shod")
                        else :
                            print("sale sakht eshtebahe")
                        break

                    case _ :
                        print("gozine ehtebahe")
                        break

            case "2" :
                khadamat = input("1.taviz lent 2.taviz roghan 3.tamire kooler :")
                match khadamat :
                    case "1" :
                        khedmat = "taviz lent"
                        print("tavize lent sabt shod")
                        break

                    case "2" :
                        khedmat = "taviz roghan"
                        print("taviz roghan anjam shod")
                        break

                    case "3" :
                        khedmat = "tamire kooler"
                        print("tamire kooler sabt shod")
                        break

                    case _ :
                        print("gozine eshtebah ast")
                        break

            case "3" :
                exit()

            case _ :
                print("gozine eshtebah ast")
                break    
                        
                
                                

                    

                                

                            

                                


                

                    

