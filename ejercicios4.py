'''Escribir un programa que solicite al usuario un vocal en minuscula, y luego una letra en mayúsculas. El programa 
debe convertir la letra en minúscula y la vocal en mayúscula, y al final, deben ser concatenadas ambas'''

vocal = input("Indica una vocal en minuscula: ")

letra = input("Indica una letra en mayúsculas: ")

print("El resultado es: ",vocal.upper()+letra.lower())

'''Hacer un programa que pida al usuario su nombre, su edad y su sexo y los muestre de la siguiente forma:
Te llamas: <nombre>
Tu edad es: <edad>
Eres: <sexo>'''

nombre = input("Indica tu nombre: ")
edad = int(input("Indica tu edad: "))
sexo = input("Indica tu sexo: ")

print("Te llamas: {} \nTu edad es {} \nEres: {}".format(nombre, edad, sexo) )