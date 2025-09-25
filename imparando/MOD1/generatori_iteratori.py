import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



#generatore è un tipo particolare di iteratore

#sia generatori che iteratori ti permettono di scorrere una sequenza.
#L' iteratore ha la proprietà di saperti dare il valore successivo nella sequenza usando
# la funzione next e sa anche quando fermarsi usando la funzione StopIteration
#dovendo tenere tutto in memoria se la lista fosse lunga sprecherei un sacco di memoria

#i generatori invece fanno la solita cosa ma sono in grado di salvare un elemento alla 
#volta, cioè non legge da una lista già pronta ma li genera mano a mano


quadrati = [x**2 for x in range(10)] #qui ho una lista già pronta


for i in quadrati: #in questo caso l' iteratore scorre la lista già pronta salvato in memoria e
    #stampa uno ad uno i valori, più veloce però ho rischio che se la lista 
    #è troppo lunga il vantaggio non c'è più
    print(i)

print("\n\n\n")

 
def quadratis(n):  #qui possiamo vedere un uso di un generatore
    #usando lo yield il ciclo si blocca ogni volta che incontra la parola "yield" e passa
    # il valore al ciclo for sottostante per farlo stampare

    for c in range(n): #questo ciclo for genera i quadrati da 0 a n ù
        #ma lo fa in modo particolare, interrompendosi ogni volta che incontra yield per poter
        #passare il valore generato alla funzione
        
        yield c**2 #quando arriva qui il ciclo for c in range(n):
        #si blocca per passare il valore di c**2 (che lui stesso ritorna) al ciclo for q in 
        #quadratis(10) così che quest' ultimo può stamparlo

    

for q in quadratis(10):  #il ciclo for q in quadratis(10) che vuole stampare 10 numeri
   # non legge da una lista già pronta ma comunica con il ciclo della funzione quadratis che contendo
   #lo yield si blocca ogni volta che restituisce un c 
    print(q)


print("\n\n\n")



#un un programma simile ma con ciclo che usa un iteratore sarebbe...



lista = []

def iteratore(n):
    for i in range(n):
        lista.append(i)

    return lista #qui non sto usando lo yield quindi l' esecuzione cambia... sto facendo un 
#iteratore  e non un generatore

for q in iteratore(10): #quando io chiamo la funzione iteratore(10) in questo ciclo for
    #quello che succede, non avendo messo lo yield è che lui ora
    #esegue per intero da 1 a n il ciclo for i in range(n) lista.append(i)
    #andando a creare una lista di 10 elementi 
    #solo dopo aver creato qiesta lista allora il ciclo for q in iteratore(10)
    #potrà partire e stampare i valori della lista
    print(q)
