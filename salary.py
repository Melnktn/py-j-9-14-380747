



while True:
    salary = int(input("salary ro vared kon:"))

    if salary == 0 :
        break

    if salary > 200 or salary < 5 :
        print("eshtebah")
        continue

    if salary >= 100 :
         new_salary = salary * 0.65
    elif salary >= 90 : 
         new_salary = salary * 0.80 
    elif salary >= 70 :
         new_salary = salary * 0.85 
    elif salary >= 60 :
         new_salary = salary * 0.90
    elif salary >= 50 :
         new_salary = salary * 0.95
    elif salary >= 40 :
         new_salary = salary * 0.97 
    elif salary >= 30 :
         new_salary = salary * 0.98

    else:
         print("moaf az maliyat")
         continue
    print("salarye shoma ba mohasebe maliyat:" , new_salary)    


    print("salary_paid :" , new_salary)              