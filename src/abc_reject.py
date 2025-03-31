# src/abc_reject.py
"""ABC reject for the Ising model"""

# Statistique sommaire (suffisante)
def sufficient_statistic(X):
    sum_x = X.sum()
    voisins_egaux = np.sum(X[:, :-1]==X[:, 1:]) + np.sum(X[:-1, :]==X[1:, :])
    return np.array([sum_x, voisins_egaux])

def ABC_reject_final(X_obs, alpha_prior, beta_prior, N, epsilon, n_iter, gibbs_iter):
    accepted_params = []
    S_obs = sufficient_statistic(X_obs)

    for _ in range(n_iter):
        # Tirage selon la loi a priori (obligatoire avant chaque grille)
        alpha_star = np.random.uniform(*alpha_prior)
        beta_star = np.random.uniform(*beta_prior)

        # Simulation d'une grille selon les nouveaux paramètres candidats
        X_sim = gibbs_sampler_ising_periodique_fast(alpha_star, beta_star, N, gibbs_iter)

        # Calcul de la distance
        S_sim = sufficient_statistic(X_sim)
        distance = np.linalg.norm(S_sim - S_obs)

        # Acceptation ou rejet
        if distance <= epsilon:
            accepted_params.append((alpha_star, beta_star))

    return np.array(accepted_params)