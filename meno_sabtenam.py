



while True :
    main_menu = input("1.voorod 2.sabtenam 3.exit :")
    while True :
        match main_menu :
            case "1" :
                voorod = input("1.username 2.password :")
                match voorod :
                    case "1" :
                        username = input("usero bezan :")
                        password = input("passo bezan :")
                        if username.isalnum()==True and password.isalnum()==True :
                            print("user ok")
                            print("pass ok")

                            if len(username)>=8 and len(password)>=8 :
                                print("user va pass ok")
                            else :
                                print("user va pas nokey")
                                break

            case "2" :
                sabtenam = input("1.esm 2.famili 3.sen 4.email 5.asress 6.telefon 7.kode posti 8.jensiyat 9.tahsilat :")
                match sabtenam :
                    case "1" :
                        esm = input("esmet ghiye? :")
                        if esm.isalpha()==True :
                            print("esm ok ")
                        else :
                            print("esm nokey")
                            break

                    case "2" :
                        famili = input("familito begooo")
                        if famili.isalpha()==True :
                            print("famili ok")
                        else :
                            print("famili nokey")
                            break

                    case "3" :
                        sen = input("chan salete? :")
                        if sen.isdigit()==True and 10<=int(sen)<=100 :
                            print("sen mojaze")
                        else :
                            print("sen mojaz ni")
                            break

                    case "4" :
                        email = input("emailo bezan :")
                        if email.endswith("@gmail.com")==True :
                            print("email ok")
                        else :
                            print("email ghalate")
                            break

                    case "5" :
                        adress = input("adress ra vared konid :")
                        if len(adress)>=5 :
                            print("adress dorost vared shode")
                        else :
                            print("adress eshtebah ast")
                            break

                    case "6" :
                        telefon = input("shomare khod ra vared konid :")
                        if telefon.isalnum()==True and len(telefon)==11 :
                            print("shomare vared shode ok")
                        else : 
                            print("shomare vared shode ghalate")
                            break

                    case "7" :
                        kode_psti = input("kod ra vared konid :")
                        if kode_psti.isalnum()==True and len(kode_psti)==10 :
                            print("kod is ok")
                        else :
                            print("cod is wrong")
                            break

                    case "8" :
                        jensiyat = input("che jensi hasti :")
                        if jensiyat=="mard" or jensiyat=="zan" or jensiyat=="other" :
                            print("jensiyat doroste")
                        else :
                            print("jensiyat eshtebahe")
                            break

                    case "9" :
                        tahsilat = input("tahsilate shoma chist :")
                        if tahsilat.isalpha()==True :
                            print("tahsilat ok")
                        else :
                            print("tahsilat not ok")
                            break

            case "3" :
                exit()
                                                                       
    