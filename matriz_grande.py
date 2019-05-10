a = [[(8,8),(1,10)],[(10,1),(2,2)]]

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
            ponga_fila_enceros(i)
            
def comparar_columnas(i,l):
    cond == a[i][0][1] >= a[l][0][1]
    for j in range (1,b-1):
        cond=cond ^ a[i][j][1] >= [l][j][1]
        
        if cond == True :
            ponga_columna_enceros(l)
        else:
            cond == a[i][0][1] < a[l][0][1]
            cond=cond ^ a[i][j][1] < [l][j][1]
            ponga_columna_en_ceros(i)
    
def ponga_columna_en_ceros(z):
  # toca poner las tuplas en ceros   
    
def ponga_fila_enceros(y):
    

# PARA COMPARAR TODAS LAS FILAS CON CADA FILA MENOS CON SI MISMA PARA ELIMINAR POR DOMINANCIA ESTRICTA
    
for i in range (0,c-2):
    for l in range (i+1,c-1):
        comparar_filas(i,l)
        
    
