


guesses =[]
while True :
    main_menu = input("1.sabt hads 2.show hads 3.show number hads 4.show big hads 5.delete hads 6.exit :")
    while True :
        match main_menu :
            case "1" :
                sabt_hads = int(input("hads khod ra vared kon :"))
                if sabt_hads in guesses :
                    print("in adad ghablan vared shode")
                else :
                    guesses.append(sabt_hads)
                    print("adad sabt shod")
                break
            case "2" :
                print(guesses)
                break
            case "3" :
                print(len(guesses))
                break 
            case "4" :
                if len(guesses)>0 :
                    print(max(guesses))
                else :
                    print("hads sabt nashod ")
                break
            case "5" :
                guesses.clear()
                print("hame hads ha delete shod")
                break
            case "6" :
                break
                
                
            
