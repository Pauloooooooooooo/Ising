# src/mcmc_abc.py
"""MCMC ABC for the Ising model"""

# MCMC-ABC pour estimer (alpha, beta)
def mcmc_abc(x_obs, N, epsilon, n_iter, gibbs_iter, sigma_alpha, sigma_beta):
    S_obs = sufficient_statistic(x_obs)
    samples = []

    # Initialisation aléatoire dans le support de l'a priori
    alpha_curr = np.random.uniform(-1, 2)
    beta_curr = np.random.uniform(0, 2)

    for t in range(n_iter):
        # Proposition par marche aléatoire
        alpha_prop = alpha_curr + np.random.normal(0, sigma_alpha)
        beta_prop  = beta_curr + np.random.normal(0, sigma_beta)

        # Vérifie que le paramètre reste dans le support de l’a priori
        if not (-1 <= alpha_prop <= 2 and 0 <= beta_prop <= 2):
            samples.append((alpha_curr, beta_curr))
            continue

        # Simulation et statistique
        x_sim = gibbs_sampler_ising_periodique_fast(alpha_prop, beta_prop, N, gibbs_iter)
        S_sim = sufficient_statistic(x_sim)

        distance = np.linalg.norm(S_sim - S_obs)

        # Critère ABC : accepter seulement si les données simulées sont proches
        if distance <= epsilon:
            # Ratio des a priori (uniformes ici) = 1, donc Metropolis sans correction
            alpha_curr = alpha_prop
            beta_curr = beta_prop

        samples.append((alpha_curr, beta_curr))  # toujours ajouter l'état courant (même en cas de rejet)

    return np.array(samples)