
a = [[(8,8),(1,10)],[(10,1),(2,2)]]
lista = []

#print (a [0]) #primera parte de la lista

#print(a[0][0])#primera tupla de la lista

#print(a[0][0][0]) # primer elemento de la tupla

#print(a[0][1][0])# primera parte de la lista, segunda tupla, primer elemento



# comparar los Xi



# compara 8 vs 1
# no se que argumento recibiria esto 
def comparar_los_x ():
    if a[0][0][0] > a[0][1][0]:
        lista.append(a[0][0][0])
    #print ("los Xi candidatos a equilibrio de nash son:"a[0][0][0])

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
    print lista


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
    print lista
comparar_los_x() # esto me da los xi 
comparar_los_y()# esto me da los xi y yi 
# necesito compararlos ahora todos esta lista con mi lista de tuplas inicial
    
