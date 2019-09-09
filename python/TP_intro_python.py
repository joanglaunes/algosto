import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sps


def exo1():

n=10

if n==1:
    print(0)
else:
    tas_de_cartes=[k for k in range(n)]
    
    while len(tas_de_cartes)>2:
        print (tas_de_cartes[0])
        tas_de_cartes.append(tas_de_cartes[1])
        tas_de_cartes=tas_de_cartes[2:]
        
    print(tas_de_cartes[0])
    print(tas_de_cartes[1]) 
