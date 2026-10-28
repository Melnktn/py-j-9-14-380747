


notes = []
while True :
    main_menu = input("1.make notes 2.show all notes 3.corect notes 4.delete notes 5.find notes 6.exit:")
    while True :
        match main_menu :
            case "1" :
                make_yadasht = input("yadashto benevis :")
                notes.append(make_yadasht)
                print("yadasht sabt shod ")
                break
            case "2" :
                if len(notes)==0 :
                    print("hichi yadasht nashode")
                else :
                    print(notes)
                break
            case "3" :
                if len(notes)==0 :
                    print("hichi yadasht nashod")
                else :
                    shomare_yadasht=int(input("shomare ro vared kon:"))
                    if shomare_yadasht>=1 and shomare_yadasht<=len(notes):
                        notes[shomare_yadasht-1]=input("yadasht jadid ro bezan :")
                        print("virayesh shod")
                        for i in range(len(notes)) :
                            print(i+1, notes[i])
                    else :
                            print("shomare na motabare")
                    break
            case "4" :
                if len(notes)==0 :
                    print("hichi nist :")
                else :
                    shomare_yadasht = int(input("shomare ro bezan :"))
                    if shomare_yadasht>=1 and shomare_yadasht<=len(notes) :
                        notes.pop(shomare_yadasht-1)
                        print("hazf shod")
                        for i in range(len(notes)) :
                            print(i+1,notes[i])
                    else :
                            print("shomare na motabare")
                    break
            case "5" :
                kalame = input("kalame ro jostojo kon:")
                for i in range(len(notes)):
                    if kalame in notes[i] :
                        print(i+1 , notes[i])
                break
            case"6" :
                break


                    