


products = []
prices = []
while True :
    main_menu = input("1.add mahsol 2.show sabad kharid 3.delete mahsol 4.mohasebe number mahsols 5.find mahsol 6.exit:")
    while True :
        match main_menu :
            case "1" :
                esm_mahsol = input ("esme mahsol ro bezan :")
                gheymat = int(input("gheymat ro vared kon :"))
                products.append(esm_mahsol)
                prices.append(gheymat)
                print("mahsol ad shod")
                break
            case "2" :
                print(products)
                print(prices)
                print(sum(prices))
                break
            case "3" :
                hazf_mahsol = input("esme mahsoli ke mikhai hazf koni ron :")
                prices.pop(products.index(hazf_mahsol))
                products.remove(hazf_mahsol)
                print("\n" , products)
                break
            case "4":
                print(len(products))
                break
            case"5" :
                baresi_mahsol = input("esme mahsolo bego:")
                if baresi_mahsol in products :
                    print("hast")
                else:
                    print("nist")
                break
            case"6" :
                break

