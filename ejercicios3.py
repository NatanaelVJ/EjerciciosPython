''' Realizar un programa que haga el proceso de formula general para la resolución de ecuaciones, sabiendo que la formula general es 
la que está en la imagen, el usuario debe ingresar los valores de “a”, “b” y “c”, y el programa debe hacer el proceso para que al 
final muestre el mensaje: “La solución es: <solucion>” '''
import math

a = int(input("Indica el valor de a: "))
b = int(input("Indica el valor de b: "))
c = int(input("Indica el valor de c: "))

if ((b**2 - 4*a*c) <0):
    print("No se puede resolver, ya que hay numeros negativos bajo la raiz")
else:
    x1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a) 
    x2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a) 

    print("El resultado para x1 es:",x1,"\nY para x2:",x2)

    
'''Se desea tener un algoritmo que permita determinar y mostrar el promedio que ha obtenido un alumno en un determinado curso, 
conociendo las notas de: tres prácticas, el examen parcial y el examen final.
Considere:
PP = ( P1 + P2 +P3 ) / 3 PROM = ( PP + 2*EP + 3*EF ) / 6
Donde: P1, P2, P3 : Practicas
PP: promedio de práctica
PROM: promedio
EP: examen parcial
EF: examen final'''