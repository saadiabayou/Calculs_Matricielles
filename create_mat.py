# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 17:34:10 2020

@author: Saadia Bayou
"""

"""
Création d'une matrice M de dimension d :

Saisie de la dimension et des coefficients de la matrice M  
Affichage de la matrice M 

"""

# Initialisation
v=[] # vecteur colonne matrice M
M=[] # matrice M carré

# d dimension de la matrice carrée
d=int(input("Entrer la dimension d de la matrice M : \n d= "))

# Créer une matrice 
for i in range(d):
    for j in range(d):
        c=int(input("Entrer les coefficient de la matrice M \nMij= ")) 
        v.append(c)
    M.append(v)
    v=[]
    print("La matrice M égale : \n M= ",M)






        
        
        
        
    
       