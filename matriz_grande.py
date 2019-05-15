# juego para nxm
a = [[(8,8),(1,10)],[(10,1),(2,2)]]
b= []

# aqui identifica estrategias de dominancia estricta para reducir a una matriz 2x2

def comparar_filas(i,l):
    cond == a[i][0][0] >= a[l][0][0]
    for j in range (1,b-1):
        cond=cond ^ a[i][j][0] >= [l][j][0]
        
        if cond == True :
            ponga_fila-enceros(l)
        else:
            cond == a[i][0][0] < a[l][0][0]
            cond=cond ^ a[i][j][0] < [l][j][0]
            ponga_fila_en_x(i)
            
def comparar_columnas(i,l):
    cond == a[i][0][1] >= a[l][0][1]
    for j in range (1,b-1):
        cond=cond ^ a[i][j][1] >= [l][j][1]
        
        if cond == True :
            #ponga_columna_en_x(l) ## en vez de esto lo elimino usando la funcion de numpy 
        else:
            cond == a[i][0][1] < a[l][0][1]
            cond=cond ^ a[i][j][1] < [l][j][1]
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
        
 # https://es.stackoverflow.com/questions/71462/eliminar-filas-y-columnas-de-una-matriz-tomando-en-cuanta-sus-elementos
# ese link es para importar una libreria que elimina filas y columnas de una matriz tomando en cuenta sus elementos 
# https://codeday.me/es/qa/20190120/97078.html otra opcion 
        
    
