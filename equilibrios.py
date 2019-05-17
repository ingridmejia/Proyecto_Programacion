a = [[[8,8],[1,10]],[[10,1],[2,2]]]
lista = []


#respuesta = ""
#while respuesta.lower()!="no":
   # fila=a.append(input("Ingrese la fila de la siguiente manera [(a,b),(c,d)...(y,z)]:"))
   # respuesta=input(" Si desea ingresar otra fila diga 'si' de lo contrario diga 'no':")
print (a)

#a = [[(8,8),(1,10)],[(10,1),(2,2)]]
#print (a [0]) #primera parte de la lista
#print(a[0][0])#primera tupla de la lista
#print(a[0][0][0]) # primer elemento de la tupla
#print(a[0][1][0])# primera parte de la lista, segunda tupla, primer elemento
################
#ME FALTA PARA CUANDO SON IGUALES AHI QUE HAGO ?


# comparar los Xi



# compara 8 vs 1
# ESTO NO RECIBE NINGUN ARGU,ENTO
def comparar_los_x ():
    if a[0][0][0] > a[0][1][0]:
        lista.append(a[0][0][0])
    #print ("los Xi candidatos a equilibrio de nash son:"a[0][0][0])
    elif a[0][0][0] == a[0][1][0]:
        lista.append(a[0][0][0])

    else:
        lista.append(a[0][1][0])
    #print("los Xi candidatos a equilibrio de nash son:"a[0][1][0])

    # compara 8 vs 10

    if a[0][0][0] > a[1][0][0]:
        lista.append(a[0][0][0])
        #print (a[0][0][0])
    else:
        lista.append(a[1][0][0])
        #print(a[1][0][0])

    #compara 2 vs 1
    if a[1][1][0] > a[0][1][0]:
        lista.append(a[1][1][0])
        #print (a[1][1][0])
    else:
        lista.append(a[0][1][0])
        #print(a[0][1][0])
        
    #compara 2 vs 10
    if a[1][1][0] > a[1][0][0]:
        lista.append(a[1][1][0])
        #print (a[1][1][0])
    else:
        lista.append(a[1][0][0])

    #print(a[1][0][0])
    print (lista)


######################################

# comparar los Yi

def comparar_los_y ():
    #compara 8 vs 1
    if a[0][0][1] > a[1][0][1]:
        lista.append(a[0][0][1])
        #print ("los Yi candidatos a equilibrio de nash son:"a[0][0][1])
    else:
        lista.append(a[1][0][1])
        #print("los Yi candidatos a equilibrio de nash son:"a[1][0][1])
        
    #compara 8 vs 10
    if a[0][0][1] > a[0][1][1]:
        lista.append(a[0][0][1])
        #print (a[0][0][1])
    else:
        lista.append(a[0][1][1])
        #print(a[0][1][1])
        
    #compara 2 vs 1
    if a[1][1][1] > a[1][0][1]:
        lista.append(a[1][1][1])
        #print (a[1][1][1])
    else:
        lista.append(a[1][0][1])
        #print(a[1][0][1])
        
    #compara 2 vs 10
    if a[1][1][1] > a[0][1][1]:
        lista.append(a[1][1][1])
        #print (a[1][1][1])
    else:
        lista.append(a[0][1][1])
        #print(a[0][1][1])
    print (lista)
  
def equilibrios ():
    final=[]
    for i in range (0,int(len(lista)/2)):
        for j in range (int(len(lista)/2),int(len(lista))):
            lista1 =[] 
            lista1.append(lista[i])
            lista1.append(lista[j])
            print(lista1)
            for z in range (2):
                for p in range(2):
                    print(a[z][p])
                    if lista1 == a[z][p]:
                        final.append(lista1)
    print(final)
    if len(final)==0:
        print ("no hay equilibrios de nash")
    else:
        print ("el equilibrio de nash es:" )
        print(final)
    return final
    
            
    

comparar_los_x() # esto me da los xi 
comparar_los_y() # esto me da los xi y yi 
equilibrios ()
