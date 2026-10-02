



while True :
     score = float(input("score ro begoo:"))

     if score < 0 or score > 20 :
          print("eshtebah")
          continue

     if score >= 17 and score <= 20 :
          if score >= 19.5:
               print("A++")
          elif score >= 18:
               print("A+")
          else:
               print("A")

     elif score >= 14 and score < 17:
          if score >= 16:
               print("B++")                      
          elif score >= 15:
               print("B+")
          else:
               print("B") 

     elif score >= 11 and score < 14:
          if score >= 13:
               print("C++")
          elif score >= 12:
               print("C+")
          else:
               print("C")

     elif score >= 8 and score < 11:
          if score >= 10:
               print("D++") 
          elif score >= 9:
               print("D+")
          else:
               print("D")

     else:
          print("kharab kardi")                                                 

    
                    