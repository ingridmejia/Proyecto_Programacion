
class Point:
    def __init__(self,X,Y):
        self.x = X
        self.y = Y
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    def __add__(self,other):
        return Point(self.x + other.x , self.y + other.y)
    
#COMPARACION DE PUNTOS SOLOS 
#Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. 

#def max (n1, n2):
 #   if n1 < n2:
   #     print n2
    #elif n2 < n1:
    #    print n1
    #else:
  #      print "Son iguales"
        
#Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos. 

def max_de_tres (n1, n2, n3):
    if n1 > n2 and n1 > n3:
        print n1
    elif n2 > n1 and n2 > n3:
        print n2
    elif n3 > n1 and n3 > n2:
        print n3
    else:
        print "Son iguales"
        
#La función max() del ejercicio 1 (primera parte) y la función max_de_tres() del ejercicio 2 (primera parte), solo van a funcionar para 2 o 3 números. Supongamos que tenemos mas de 3 números o no sabemos cuantos números son. Escribir una función max_in_list() que tome una lista de números y devuelva el mas grande.
def max_in_list(lista):
    inicio = 0
    for i in lista:
    if i > inicio:
        inicio = i
    return inicio
    
# 1ER INTENTO 

def compararpuntos (p1,p2,p3,p4):
    if p1 > p2 and p1 > p3 and p3 > p4:
        print p1
    elif p2 > p1 and p2 > p3 and p3 > p4 :
        print p2
    elif p3 > p1 and p3 > p2 and p3 > p4:
        print p3
    elif p4 > p1 and p4 > p2 and p4 > p3:
        print p4
    
    else:
        print "Son iguales"

    
p1 = Point(8,8) # confiesa confiesa
p2 = Point(1,10) # confiesa no confiesa
p3 = Point(10,1)# no confiesa confiesa
p4 = Point(2,2) # no confiesa no confiesa

          
p1.x=8
p1.y=8
print("P1: ({0},{1})".format(p1.x,p1.y))
puntomayor = p1.x > p2.x +
(punto1.y-punto2.y)**2
