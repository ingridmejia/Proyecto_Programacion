
a = [[(8,8),(1,10)],[(10,1),(2,2)]]

print (a [0]) #primera parte de la lista

print(a[0][0])#primera tupla de la lista

print(a[0][0][0]) # primer elemento de la tupla

print(a[0][1][0])# primera parte de la lista, segunda tupla, primer elemento



# comparar los Xi



# compara 8 vs 1

if a[0][0][0] > a[0][1][0]:

    print ("los Xi candidatos a equilibrio de nash son:"a[0][0][0])

else:

    print("los Xi candidatos a equilibrio de nash son:"a[0][1][0])

    

# compara 8 vs 10

    

if a[0][0][0] > a[1][0][0]:

    print (a[0][0][0])

else:

    print(a[1][0][0])

    

#compara 2 vs 1

if a[1][1][0] > a[0][1][0]:

    print (a[1][1][0])

else:

    print(a[0][1][0])



#compara 2 vs 10

if a[1][1][0] > a[1][0][0]:

    print (a[1][1][0])

else:

    print(a[1][0][0])



# comparar los Yi



#compara 8 vs 1

if a[0][0][1] > a[1][0][1]:

    print ("los Yi candidatos a equilibrio de nash son:"a[0][0][1])

else:

    print("los Yi candidatos a equilibrio de nash son:"a[1][0][1])



#compara 8 vs 10

if a[0][0][1] > a[0][1][1]:

    print (a[0][0][1])

else:

    print(a[0][1][1])



#compara 2 vs 1

if a[1][1][1] > a[1][0][1]:

    print (a[1][1][1])

else:

    print(a[1][0][1])



#compara 2 vs 10

if a[1][1][1] > a[0][1][1]:

    print (a[1][1][1])

else:

    print(a[0][1][1])
