




while True:

    username = input("username ro bezan dige:")
    password = input("password ro bezan dashi:")

    if len(password) > 10:
        print("long password")
        continue

    if username != "Fariborz" and password !="frbz011cb09" :
        print("Error for both")
        continue

    elif username != "Fariborz" :
        print("Username error")
        continue

    elif password != "frbz00" :
        print("Password error")
        continue

    age = int(input("age ro bezan:"))

    if age < 16:
        print("senet ziade , mojadad test konid")
        continue

    else:
        print("login")
        break