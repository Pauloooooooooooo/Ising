# src/gibbs.py
"""Gibbs sampler for the Ising model"""

import numpy as np
import matplotlib.pyplot as plt

def gibbs_sampler_ising(alpha, beta, N, iterations):
    
    X = np.random.choice([0,1], size=(N,N))     # Initialisation aléatoire d'un point sur une grille en 2D,  N x N

    for it in range(iterations):                # Nombre de fois où on modifie notre grille (atteindre une situation de convergence suffisante)
        for i in range(N):
            for j in range(N):
                voisins = [
                    X[(i-1)%N,j], X[(i+1)%N,j],                  # Sur une grille 2D, chaque cellule a 4 voisins (Hypothèse de 'conditions aux bords périodiques')
                    X[i,(j-1)%N], X[i,(j+1)%N]
                ]
                sum_voisins_1 = sum(voisins)                     # Voisins_1 = nombre de voisins qui prennent la valeur 1
                sum_voisins_0 = 4 - sum_voisins_1                 

                proba_1 = np.exp(alpha + beta*sum_voisins_1)        
                proba_0 = np.exp(beta*sum_voisins_0)
                p = proba_1 / (proba_1 + proba_0)

                # Mise à jour du site (i,j)
                X[i,j] = np.random.rand() < p

    return X
