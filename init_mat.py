# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 12:12:20 2020

@author: Saadia Bayou
"""

"""
Initialiser une matrice carré à zéro :  
- Saisie de la dimension d de la matrice M0
- Affichage de la matrice M0
 
"""
# Boucle initialisation à zéro pour une matrice carrée

# Initilisations - données
u=[] # Vecteur colonne de la matrice M0
M0=[] # Matrice M0

# d dimension de la matrice M0
d=int(input("Entrer la dimension de la  matrice : \nd = "))
if d > 0 :
    for nc in range(d):
        u.append(0)
        M0.append(u)
    print("\nMatrice nulle: \nM0 =",M0)
else :
    print("dimension de la matrice nulle ou négative : dim = ", d)
    
 


    

    
    
    