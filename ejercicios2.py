#.lower poner en minusculas .upper poner todo en mayuscula .capitalize poner primera palabra en mayuscula
#.title cada inicial en mayuscula .case mayuscula en miniscula y minuscula en mayuscula

#. Imprima los dos primeros caracteres.

#. Imprima los tres últimos caracteres.

#. Imprima dicha cadena cada dos caracteres. Ej.: Si la cadena fuera “recta” debería imprimir rca

#. Dicha cadena en sentido inverso. Ej.: Si la cadena fuera hola mundo! debe imprimir !odnum aloh

#. Imprima la cadena en un sentido y en sentido inverso. Ej: Si la cadena es “reflejo” imprime reflejoojelfer


cadena = 'Te quiero solo como amigo'
x = len(cadena)

print(cadena[0:2])
print(cadena[-3:])
c1 = cadena[: :2]
c2 = cadena[: : -1]
print(c1)
print(c2)
print(cadena+c2)


#Crear un programa que tenga una variable con la cadena “Separado” y un carácter de coma (,); e inserte el carácter 
#entre cada letra de la cadena. Ej: separar y , debería devolver s,e,p,a,r,a,r    

palabra = 'Separado'
caracter = ','

ca2 = palabra[ : :1]

reemplazar = palabra.replace("",caracter)
print(reemplazar[1:])