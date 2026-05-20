ntemp= input("ingrese temperatura a convertir ")
temp= int (ntemp)
foc= input("elija a que quieres convertir faranheit (F) o celsius (C) ").upper()
foci=(foc)
if foci == "F":
 resultf= temp * 1.8 + 32
 print(resultf)
 
elif foci == "C":
  resultc= (temp-32)*(5/9)
  print(resultc)
else :
  print("El valor es incorrecto para F o C")
   