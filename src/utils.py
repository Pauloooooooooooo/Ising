import numpy as np

def sufficient_statistic(X):
    sum_x = X.sum()
    voisin_egaux = np.sum(X[:, :-1] == X[:, 1:]) + np.sum(X[:-1, :] == X[1:, :])                # Somme des voisins identiques entre décalage haut et droit (nepas faire l'autre côté, on compterait deux fois)
    return np.array([sum_x, voisin_egaux])