


books =[]
kharej = False
while True :
    main_menu = input("1.add book 2.show books 3.find book 4.number books 5.delete all books 6.exit :")
    while True :
        match main_menu :
            case "1" :
                esm_ketab = input("che ketabi mikhai ? :")
                if esm_ketab in books :
                    print("ketabe mored nazar ghablan add shode")
                else :
                    books.append(esm_ketab)
                    print("ketabet add shod ")
                break
            case "2" :
                print(books)
                break
            case "3" :
                find_bool = input("baraye peyda shodan ketab esmesho bezan :")
                if find_bool in books :
                    print("ketab find shod")
                else :
                    print("ketab couldnt find")
                break
            case "4" :
                print(len(books))
                break
            case "5" :
                books.clear()
                print("hame ketabha pak shod")
                break
            case "6" :
                kharej=True
                break
        if kharej:
            break
                 
 