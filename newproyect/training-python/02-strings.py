texto = "Hola mundo"
print(texto)
print(texto.upper())
print(texto.lower())
print(texto.find("m"))
print(texto.replace("mundo" , "cristianoronaldo"))
nuevotexto = texto.replace("mundo" , "cristianoronaldo")
print(texto,nuevotexto)
print("cristianoronaldo" in nuevotexto)
print(len(texto))
print(texto[0])
print(texto[0:4])
print(texto[10:])
print(texto[:10])
print(texto[:])
nombre= "pepino"
apellido = "martinez"
nombre_completo = f"{nombre} {apellido}"
print (nombre_completo)
prueba = f"{nombre[0]} {2 + 5}"
print (prueba)