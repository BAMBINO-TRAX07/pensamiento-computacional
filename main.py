print("ejercicio 1")
for i in range (1, 11):
   if i % 2==1:
      print(i)
     
print("ejercicio 1")
x=1 
while x<11:
    if x%2==1:
        print(x)
    x+=1
    
print("escenario 1")
while True:
    palabra=(input("ingrese una palabra"))
    if palabra =="chupacabra":
        print("haz dejado el bucle con exito")
        break
 
 print("Aldy Abimael Ramos Mota 1589025")
    
print("escenario 2")
user_word=input("ingrese una palabra")
user_word=user_word.upper()
for i in user_word:
    if i in ["A", "E", "I", "O", "U"]:
        continue
    print(i)

