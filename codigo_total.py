a =[[[1,0],[0,1],[2,1]],[[0,0],[2,4],[4,3]],[[2,1],[1,0],[3,2]]]

lista = []
respuesta = ""
#while respuesta.lower()!="no":
   # fila=a.append(input("Ingrese la fila de la siguiente manera [[a,b],[c,d]...[y,z]]:"))
   # respuesta=input(" Si desea ingresar otra fila diga 'si' de lo contrario diga 'no':")


# aqui identifica estrategias de dominancia estricta para reducir a una matriz 2x2


b=len(a)
c=len(a[0])

def borrarfilas(a,x):
    del a[x]
def borraColumnas(a,y):
    for i in range(len(a)):
        del a[i][y]
    
def comparar_filas(i,l):
    cond = a[i][0][0] >= a[l][0][0]
   
    for j in range (1,b-1):
        cond=cond and a[i][j][0] >= a[l][j][0]
        
        if cond == True :
            borrarfilas(a,l)
        
            #ponga_fila-enceros(l)
        else:
            cond = a[i][0][0] < a[l][0][0]
            cond=cond and a[i][j][0] < a[l][j][0]
            borrarfilas(a,i)
            #ponga_fila_en_x(i)
            
def comparar_columnas(i,l):
    cond = a[i][0][1] >= a[l][0][1]
   
    for j in range (1,c-1):
        cond=cond and a[i][j][1] >= a[l][j][1]
        
        if cond == True :
        
            borraColumnas(a,l-1)
            
            
        else:
            cond = a[i][0][1] < a[l][0][1]
            cond=cond and a[i][j][1] < a[l][j][1]
            borraColumnas(a,i)
            
           
 


# PARA COMPARAR TODAS LAS FILAS CON CADA FILA MENOS CON SI MISMA PARA ELIMINAR POR DOMINANCIA ESTRICTA
    

        
#hasta aqui reduce a una matrioz 2*2        
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
    #print (lista)


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
    #print (lista)
  
def equilibrios ():
    final=[]
    
    
    for i in range (0,int(len(lista)/2)):
        for j in range (int(len(lista)/2),int(len(lista))):
            lista1 =[] 
            lista1.append(lista[i])
            lista1.append(lista[j])
            #print(lista1)
            for z in range (2):
                for p in range(2):
                    if lista1 == a[z][p]:
                        final.append(lista1)
    
    #aqui elimino las sublistas repetidas
    listanueva=[]
    for h in final:
        if h not in listanueva:
            listanueva.append(h)
    
            
    
    
    if len(listanueva)==0:
        print ("no hay equilibrios de nash")
    else:
        print ("el equilibrio de nash es:" )
        print(listanueva)
    return listanueva

    
#EJECUCION  
print("matriz inicial")
print (a)
print()  
    
for i in range (0,b-2):
    for l in range (i+1,b-1):
        comparar_filas(i,l)
        print("elimino fila")
        print(a)
        print()
        
for i in range (0,c-2):
    for l in range (i+1,c-1):
        comparar_columnas(i,l)
        print("elimino columna")
        print(a)
        print()
        
comparar_los_x() # esto me da los xi 
comparar_los_y() # esto me da los xi y yi 
