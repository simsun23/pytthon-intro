# variabler för att komma ihåg namn och ålder

#läsa in namn 
name = input("vad heter du: ")
#läsa in ålder
age = int(input("hur gammal är du: "))


#skriv ut hej namn och du är x gammal
print ("hejsan", name , ", välkommen till mitt program.")
print ("du är", age , "gammal!")
#om du är 18 eller inte
if age < 19:
    print("du har inte fyllt 19 ännu")
else:
     print("du har fyllt 19")