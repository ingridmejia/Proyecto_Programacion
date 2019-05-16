import numpy as np
a =[]
lista = []
respuesta = ""
while respuesta.lower()!="no":
    fila=a.append(input("Ingrese la fila de la siguiente manera [(a,b),(c,d)...(y,z)]:"))
    respuesta=raw_input(" Si desea ingresar otra fila diga 'si' de lo contrario diga 'no':")
print a

# aqui identifica estrategias de dominancia estricta para reducir a una matriz 2x2
########
#dudas too los cositos van en parentesis ?
def comparar_filas(i,l):
    cond == a[i][0][0] >= a[l][0][0]
    for j in range (1,b-1):
        cond=cond ^ a[i][j][0] >= a[l][j][0]
        
        if cond == True :
            np.delete(a,l,axis=1)
            #ponga_fila-enceros(l)
        else:
            cond == a[i][0][0] < a[l][0][0]
            cond=cond ^ a[i][j][0] < a[l][j][0]
            np.delete(a,i,axis=1)
            #ponga_fila_en_x(i)
            
def comparar_columnas(i,l):
    cond == a[i][0][1] >= a[l][0][1]
    for j in range (1,b-1):
        cond=cond ^ a[i][j][1] >= a[l][j][1]
        
        if cond == True :
            np.delete(a,l,axis=1)
            #ponga_columna_en_x(l) ## en vez de esto lo elimino usando la funcion de numpy 
        else:
            cond == a[i][0][1] < a[l][0][1]
            cond=cond ^ a[i][j][1] < a[l][j][1]
            np.delete(a,i,axis=1)
            #ponga_columna_en_ceros(i)
    #es mejor ponerlas en x para luego poderlas eliminar con  remove
    # es mjor eliminarlas de una para ir reduciendo la matriz 

 # asi ya no necesitaria estas dos funciones 
def ponga_columna_en_x(z):
  # toca poner las tuplas en ceros   
    
def ponga_fila_en_x(y):
    

# PARA COMPARAR TODAS LAS FILAS CON CADA FILA MENOS CON SI MISMA PARA ELIMINAR POR DOMINANCIA ESTRICTA
    
for i in range (0,c-2):
    for l in range (i+1,c-1):
        comparar_filas(i,l)
###############################
        
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
