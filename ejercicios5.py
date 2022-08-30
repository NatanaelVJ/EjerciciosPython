'''Crear un programa que pida al usuario una letra, y si es vocal, muestre el mensaje "Es vocal". 
Sino, decirle al usuario que no es vocal'''

letra = input("Indica una letra: ")



if letra.lower() == 'a' or letra.lower() == 'e' or letra.lower() == 'i' or letra.lower() == 'o' or letra.lower() == 'u':
    print("Es vocal")

else:
    print("No es vocal")

'''Escribir un programa que, dado un número entero, muestre su valor absoluto. Nota: para los números positivos 
su valor absoluto es igual al número (el valor absoluto de 52 es 52), mientras que, para los negativos, su valor 
absoluto es el número multiplicado por -1 (el valor absoluto de -52 es 52).'''

numero = int(input("Indica un numero: "))

if numero < 0:
    print("El numero absoluto es:",abs(numero))
else:
    print("El numero absoluto es:",numero)