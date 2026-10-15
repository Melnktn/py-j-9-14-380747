



while True :
    main_menu = input("1.chini 2.italiyai 3.irani 4.pish ghaza 5.noshidani 6.exit :")
    while True :
        match main_menu :
            case "1" :
                chini = input("1.dampling (15yuan) 2.fried rice(20yuan) 3.chow main(22yuan) 4.kung pao chicken(35yuan) 5.sweet and pork(38yuan) 6.peking duck(80yuan) 7.mapo tofu(25yuan) 8.spring roll(12yuan) 9.hot pot(60yuan) 10.wonton soup(18yuan) :")
                match chini :
                    case "1":
                        dumpling = int(input("tedade dumpling ra vared kon :"))
                        if str(dumpling).isdigit()==True and dumpling>0 :
                            gheymat = 1.1 * 15 * dumpling                    
                            print("gheymate_nahaii :" , gheymat)
                        else :
                            print("tedad eshtebahe")
                            break

                    case "2" :
                        fried_rice = int(input("chand pors mikhay? :"))
                        if str(fried_rice).isdigit()==True and fried_rice>2 :
                            gheymat = 1.1 * 20 * fried_rice                            
                            print("fride rice :" , gheymat)
                        else :
                            print("tedad yaft nashod")
                            break

                    case "3" :
                        chow_main = int(input("chan pors chow main mikhay :"))
                        if str(chow_main).isdigit()==True and chow_main>0 :
                            gheymat = 1.1 * 22 * chow_main                            
                            print("chow main:" , gheymat)
                        else :
                            print("tedad yaft nashod")
                            break

                    case "4" :
                        kung = int(input("tedad kung ro bego :"))
                        if str(kung).isdigit()==True and kung>0 :
                            gheymat = 1.1 * 35 * kung                            
                            print("kung pao chiken :" , gheymat )
                        else :
                            print("tedad yaft nashod")
                            break

                    case "5" :
                        sweet_and_pork = int(input("chanta mikhay :"))
                        if str(sweet_and_pork).isdigit()==True and sweet_and_pork>1 :
                            gheymat = 1.1 * 38 * sweet_and_pork                            
                            print("sweet and pork :" , gheymat )
                        else :
                            print("nadarim")
                            break

                    case "6" :
                        peking_duck = int(input("chanta peking duck mikhay? :"))
                        if str(peking_duck).isdigit()==True and peking_duck>5 :
                            gheymat = 1.1 * 80 * peking_duck                            
                            print("peking:" , gheymat )
                        else :
                            print("tedad yaft nashod")
                            break

                    case "7" :
                        tufo = int(input("chanta tufo mikhori? :"))
                        if str(tufo).isdigit()==True and tufo>10 :
                            gheymat = 1.1 * 25 * tufo                           
                            print("tufo :" , gheymat )
                        else :
                            print("yaft nashod")
                            break

                    case "8" :
                        spring_roll = int(input("chand roll mikhay? :"))
                        if str(spring_roll).isdigit()==True and spring_roll>0 :
                            gheymat = 1.1 * 12 * spring_roll                           
                            print("spring roll:" , gheymat )
                        else :
                            print("tedad yaft nashod")
                            break

                    case "9" :
                        hot_pot = int(input("chanta mail mikonid ? :"))
                        if str(hot_pot).isdigit()==True and hot_pot>1 :
                            gheymat = 1.1 * 60 * hot_pot                            
                            print("hot pot:" , gheymat )
                        else :
                            print("nadarim")
                            break

                    case "10" :
                        suop = int(input("chand kase mail miloni? :"))
                        if str(suop).isdigit()==True and suop>0 :
                            gheymat = 1.1 * 18 * suop                            
                            print("suop:" , gheymat )
                        else :
                            print("nadarim")
                            break

            
            



    
            case "2" :
                    itali = input("1.pizza (10 euro) 2.espageti(14 euro) 3.lazaniya (15 euro) 4.risoto (16 euro) 5.tiramiso (7 euro) 6.ravioli(13 euro) 7.gnoocchi(14 euro) 8.bruschetta (6 euro) 9.minestrone (9 euro) 10.buco (24 euro) :")
                    match itali :
                        case "1":
                            pizza = int(input("chand slais mikhai? :"))
                            if str(pizza).isdigit()==True and pizza>0 :
                                gheymat = 1.1 * 10 * pizza                    
                                print("gheymate_nahaii :" , gheymat)
                            else :
                                print("tedad eshtebahe")
                                break

                        case "2" :
                            espageti = int(input("chand pors mikhay? :"))
                            if str(espageti).isdigit()==True and espageti>2 :
                                gheymat = 1.1 * 14 * espageti                            
                                print("gheymate_nahaii :" , gheymat)
                            else :
                                print("tedad yaft nashod")
                                break

                        case "3" :
                            lasaniya = int(input("chan pors lasaniya mikhay :"))
                            if str(lasaniya).isdigit()==True and lasaniya>0 :
                                gheymat = 1.1 * 15 * lasaniya                            
                                print("gheymate_nahaii:" , gheymat)
                            else :
                                print("tedad yaft nashod")
                                break

                        case "4" :
                            rissoto = int(input("tedad risotto ro bego :"))
                            if str(rissoto).isdigit()==True and rissoto>0 :
                                gheymat = 1.1 * 16 * rissoto                            
                                print("gheymate_nahaii :" , gheymat )
                            else :
                                print("tedad yaft nashod")
                                break

                        case "5" :
                            tiramiso = int(input("chanta mikhay :"))
                            if str(tiramiso).isdigit()==True and tiramiso>1 :
                                gheymat = 1.1 * 7 * tiramiso                            
                                print("gheymate_nahaii :" , gheymat )
                            else :
                                print("nadarim")
                                break

                        case "6" :
                            ravioli = int(input("chanta mikhay? :"))
                            if str(ravioli).isdigit()==True and ravioli>5 :
                                gheymat = 1.1 * 13 * ravioli                            
                                print("gheymate_nahaii:" , gheymat )
                            else :
                                print("tedad yaft nashod")
                                break

                        case "7" :
                            gnoocchi = int(input("chanta gnoocchi mikhori? :"))
                            if str(gnoocchi).isdigit()==True and gnoocchi>10 :
                                gheymat = 1.1 * 14 * gnoocchi                           
                                print("gheymate_nahaii :" , gheymat )
                            else :
                                print("yaft nashod")
                                break

                        case "8" :
                            bruschetta = int(input("chand mikhay? :"))
                            if str(bruschetta).isdigit()==True and bruschetta>0 :
                                gheymat = 1.1 * 6 * bruschetta                           
                                print("gheymate_nahaiim:" , gheymat )
                            else :
                                print("tedad yaft nashod")
                                break

                        case "9" :
                            minestrone = int(input("chanta mail mikonid ? :"))
                            if str(minestrone).isdigit()==True and minestrone>1 :
                                gheymat = 1.1 * 9 * minestrone                            
                                print("gheymate_nahaii:" , gheymat )
                            else :
                                print("nadarim")
                                break

                        case "10" :
                            buco = int(input("chand kase mail miloni? :"))
                            if str(buco).isdigit()==True and buco>0 :
                                gheymat = 1.1 * 24 * buco                            
                                print("gheymate_nahaii:" , gheymat )
                            else :
                                print("nadarim")
                            break

                        



    
            case "3" :
                    irani = input("1.kabab (1milyoon) 2.ghorme sabzi(500 toman) 3.fesengoon(850 toman) 4.zereshk polo(700 toman) 5.dizi(350 toman) 6.baghali polo ba mahi(900 toman) 7.kashke bademgoon(300 toman) 8.mirza ghasemi(289 toman) 9.ash(400 toman) 10.tahchin(500 toman) :")
                    match chini :
                        case "1":
                            kabab = int(input("chand sikh mikhay :"))
                            if str(kabab).isdigit()==True and kabab>0 :
                                gheymat = 1.1 * 1000000 * kabab                    
                                print("gheymate_nahaii :" , gheymat)
                            else :
                                print("tedad eshtebahe")
                                break

                        case "2" :
                            ghorme = int(input("chand pors mikhay? :"))
                            if str(ghorme).isdigit()==True and ghorme>2 :
                                gheymat = 1.1 * 400000 * ghorme                            
                                print("gheymate_nahaii :" , gheymat)
                            else :
                                print("tedad yaft nashod")
                                break

                        case "3" :
                            fesengoon = int(input("chan pors fesengoon mikhay :"))
                            if str(fesengoon).isdigit()==True and fesengoon>0 :
                                gheymat = 1.1 * 850000 * fesengoon                            
                                print("gheymate_nahaii:" , gheymat)
                            else :
                                print("tedad yaft nashod")
                                break

                        case "4" :
                            zereshkpolo = int(input("chand pors zereshk olo mikhay :"))
                            if str(zereshkpolo).isdigit()==True and zereshkpolo>0 :
                                gheymat = 1.1 * 700000 * zereshkpolo                            
                                print("gheymate_nahaii :" , gheymat )
                            else :
                                print("tedad yaft nashod")
                                break

                        case "5" :
                            dizi = int(input("chand kase dizi mikhay :"))
                            if str(dizi).isdigit()==True and dizi>1 :
                                gheymat = 1.1 * 350000 * dizi                            
                                print("gheymate_nahaii :" , gheymat )
                            else :
                                print("nadarim")
                                break

                        case "6" :
                            baghalipolo_mahi = int(input("chand pors mikhay? :"))
                            if str(baghalipolo_mahi).isdigit()==True and baghalipolo_mahi>5 :
                                gheymat = 1.1 * 900000 * baghalipolo_mahi                            
                                print("gheymate_nahaii:" , gheymat )
                            else :
                                print("tedad yaft nashod")
                                break

                        case "7" :
                            kashke_bademjoon = int(input("chanta kase mikhori? :"))
                            if str(kashke_bademjoon).isdigit()==True and kashke_bademjoon>1 :
                                gheymat = 1.1 * 100000 * kashke_bademjoon                           
                                print("gheymate_nahaii:" , gheymat )
                            else :
                                print("yaft nashod")
                                break

                        case "8" :
                            mirzaghasemi = int(input("chand ta mikhay? :"))
                            if str(mirzaghasemi).isdigit()==True and mirzaghasemi>0 :
                                gheymat = 1.1 * 150000 * mirzaghasemi                           
                                print("gheymate_nahaii:" , gheymat )
                            else :
                                print("tedad yaft nashod")
                                break

                        case "9" :
                            ash = int(input("chand kilo mikhay ? :"))
                            if str(ash).isdigit()==True and ash>1 :
                                gheymat = 1.1 * 400000 * ash                            
                                print("gheymate_nahaii:" , gheymat )
                            else :
                                print("nadarim")
                                break

                        case "10" :
                            tahchin = int(input("chand pors mikhay? :"))
                            if str(tahchin).isdigit()==True and tahchin>0 :
                                gheymat = 1.1 * 500000 * tahchin                            
                                print("gheymate_nahaii:" , gheymat )
                            else :
                                print("nadarim")
                                break


            case "4" :
                          pish_ghaza = input("1.salad (5 dolar) 2.soup(8dolar) 3.garlic bread(3dolar) 4.jele(5dolar) 5.humus(6dolar) 6.rolete morgh(45dolar) 7.mozarwla stik(12dolar) 8.saladolviye(34dolar) 9.mive(15 doloa) 10.esfenaj(21dolar) :")
                          match chini :
                              case "1":
                                  salad = int(input("chanta mikhay :"))
                                  if str(salad).isdigit()==True and salad>0 :
                                      gheymat = 1.1 * 5 * salad                    
                                      print("gheymate_nahaii :" , gheymat)
                                  else :
                                      print("tedad eshtebahe")
                                      break
      
                              case "2" :
                                  suop = int(input("chanta mikhay? :"))
                                  if str(suop).isdigit()==True and suop>2 :
                                      gheymat = 1.1 * 8 * suop                            
                                      print("gheymate_nahaii :" , gheymat)
                                  else :
                                      print("tedad yaft nashod")
                                      break
      
                              case "3" :
                                  garlic_bread = int(input("chanta mikhay :"))
                                  if str(garlic_bread).isdigit()==True and garlic_bread>0 :
                                      gheymat = 1.1 * 3 * garlic_bread                            
                                      print("gheymate_nahaii:" , gheymat)
                                  else :
                                      print("tedad yaft nashod")
                                      break
      
                              case "4" :
                                  jele = int(input("chanta mikhay :"))
                                  if str(jele).isdigit()==True and jele>0 :
                                      gheymat = 1.1 * 5 * jele                            
                                      print("gheymate_nahaii :" , gheymat )
                                  else :
                                      print("tedad yaft nashod")
                                      break
      
                              case "5" :
                                  humus = int(input("chanta mikhay :"))
                                  if str(humus).isdigit()==True and humus>1 :
                                      gheymat = 1.1 * 6 * humus                            
                                      print("gheymate_nahaii :" , gheymat )
                                  else :
                                      print("nadarim")
                                      break
      
                              case "6" :
                                  rolet_morgh = int(input("chand pors mikhay? :"))
                                  if str(rolet_morgh).isdigit()==True and rolet_morgh>5 :
                                      gheymat = 1.1 * 45 * rolet_morgh                            
                                      print("gheymate_nahaii:" , gheymat )
                                  else :
                                      print("tedad yaft nashod")
                                      break
      
                              case "7" :
                                  mozarela = int(input("chanta mikhay:"))
                                  if str(mozarela).isdigit()==True and mozarela>1 :
                                      gheymat = 1.1 * 12 * mozarela                           
                                      print("gheymate_nahaii:" , gheymat )
                                  else :
                                      print("yaft nashod")
                                      break
      
                              case "8" :
                                  saladolviye = int(input("chand ta mikhay? :"))
                                  if str(saladolviye).isdigit()==True and saladolviye>0 :
                                      gheymat = 1.1 * 34 * saladolviye                           
                                      print("gheymate_nahaii:" , gheymat )
                                  else :
                                      print("tedad yaft nashod")
                                      break
      
                              case "9" :
                                  mive = int(input("chanta mikhay ? :"))
                                  if str(mive).isdigit()==True and mive>1 :
                                      gheymat = 1.1 * 15 * mive                            
                                      print("gheymate_nahaii:" , gheymat )
                                  else :
                                      print("nadarim")
                                      break
      
                              case "10" :
                                  esfenaj = int(input("chanta mikhay:"))
                                  if str(esfenaj).isdigit()==True and esfenaj>0 :
                                      gheymat = 1.1 * 21 * esfenaj                            
                                      print("gheymate_nahaii:" , gheymat )
                                  else :
                                      print("nadarim")
                                      break

            case "5" :
                                pish_ghaza = input("1.water (1 dolar) 2.cola(2dolar) 3.abporteghal (3dolar) 4.tea(2dolar) 5.cofee(3dolor) 6.lemon(8dolar) 7.doogh(2dolar) 8.milkshake(5dolar) 9.icetea(3 dolar) 10.macha(15dolar) :")
                                match chini :
                                    case "1":
                                        water = int(input("chanta mikhay :"))
                                        if str(water).isdigit()==True and water>0 :
                                            gheymat = 1.1 * 1 * water                    
                                            print("gheymate_nahaii :" , gheymat)
                                        else :
                                            print("tedad eshtebahe")
                                            break
            
                                    case "2" :
                                        cola = int(input("chanta mikhay? :"))
                                        if str(cola).isdigit()==True and cola>2 :
                                            gheymat = 1.1 * 2 * cola                            
                                            print("gheymate_nahaii :" , gheymat)
                                        else :
                                            print("tedad yaft nashod")
                                            break
            
                                    case "3" :
                                        abporteghal = int(input("chanta mikhay :"))
                                        if str(abporteghal).isdigit()==True and abporteghal>0 :
                                            gheymat = 1.1 * 3 * abporteghal                            
                                            print("gheymate_nahaii:" , gheymat)
                                        else :
                                            print("tedad yaft nashod")
                                            break
            
                                    case "4" :
                                        tea = int(input("chanta mikhay :"))
                                        if str(tea).isdigit()==True and tea>0 :
                                            gheymat = 1.1 * 2 * tea                            
                                            print("gheymate_nahaii :" , gheymat )
                                        else :
                                            print("tedad yaft nashod")
                                            break
            
                                    case "5" :
                                        cofee = int(input("chanta mikhay :"))
                                        if str(cofee).isdigit()==True and cofee>1 :
                                            gheymat = 1.1 * 3 * cofee                            
                                            print("gheymate_nahaii :" , gheymat )
                                        else :
                                            print("nadarim")
                                            break
            
                                    case "6" :
                                        lemon = int(input("chand  mikhay? :"))
                                        if str(lemon).isdigit()==True and lemon>5 :
                                            gheymat = 1.1 * 8 * lemon                            
                                            print("gheymate_nahaii:" , gheymat )
                                        else :
                                            print("tedad yaft nashod")
                                            break
            
                                    case "7" :
                                        doogh = int(input("chanta mikhay:"))
                                        if str(doogh).isdigit()==True and doogh>1 :
                                            gheymat = 1.1 * 2 * doogh                           
                                            print("gheymate_nahaii:" , gheymat )
                                        else :
                                            print("yaft nashod")
                                            break
            
                                    case "8" :
                                        milkshake = int(input("chand ta mikhay? :"))
                                        if str(milkshake).isdigit()==True and milkshake>0 :
                                            gheymat = 1.1 * 5 * milkshake                           
                                            print("gheymate_nahaii:" , gheymat )
                                        else :
                                            print("tedad yaft nashod")
                                            break
            
                                    case "9" :
                                        icetea = int(input("chanta mikhay ? :"))
                                        if str(icetea).isdigit()==True and icetea>1 :
                                            gheymat = 1.1 * 3 * icetea                            
                                            print("gheymate_nahaii:" , gheymat )
                                        else :
                                            print("nadarim")
                                            break
            
                                    case "10" :
                                        macha = int(input("chanta mikhay:"))
                                        if str(macha).isdigit()==True and macha>0 :
                                            gheymat = 1.1 * 15 * macha                            
                                            print("gheymate_nahaii:" , gheymat )
                                        else :
                                            print("nadarim")
                                            break

            case "6" :
                print("khodafez")
                exit()

            case _ :
                print("gozine eshtebah")
                break
            
                      
      
                