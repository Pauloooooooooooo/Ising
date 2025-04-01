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

def gibbs_sampler_ising_periodique_fast(alpha, beta, N, iterations):

    X = np.random.choice([0, 1], size=(N, N))

    for _ in range(iterations):
        voisins = (
            np.roll(X, 1, axis=0) + np.roll(X, -1, axis=0) +                  # commande qui permet de faire la somme des 4 matrices des voisins (on décale à droite, gauche, haut et bas)
            np.roll(X, 1, axis=1) + np.roll(X, -1, axis=1)                    # On se retouve avec un mlatrice contenant des nbs entre 0 et 4
        )
        p1 = np.exp(alpha + beta * voisins)
        p0 = np.exp(beta * (4 - voisins))
        proba = p1 / (p1 + p0)
        X = (np.random.rand(N, N) < proba).astype(int)

    return X
