import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, beta as beta_dist
from src.gibbs_sampler import gibbs_sampler_ising_periodique_fast
from src.utils import sufficient_statistic
from tqdm import tqdm


def prior_density(alpha, beta, prior_name):
    if prior_name == "A":
        return norm.pdf(alpha, 0.5, 1.0) * beta_dist.pdf(beta, 2, 2)
    elif prior_name == "B":
        if -1 <= alpha <= 2 and 0 <= beta <= 2:
            return 1/3 * 1/2  # Uniformes
        else:
            return 0
    elif prior_name == "C":
        return norm.pdf(alpha, 1.0, 0.5) * beta_dist.pdf(beta, 3, 1.5)
    elif prior_name == "D":
        return norm.pdf(alpha, 0, 1.5) * beta_dist.pdf(beta, 1, 1)
    else:
        raise ValueError("Prior inconnue")


def mcmc_abc_flexible_prior(x_obs, N, epsilon, n_iter, gibbs_iter, sigma_alpha, sigma_beta, prior_name):
    S_obs = sufficient_statistic(x_obs)
    samples = []

    # Initialisation dans le support
    alpha_curr = np.random.uniform(-1, 2)
    beta_curr = np.random.uniform(0, 2)
    pi_curr = prior_density(alpha_curr, beta_curr, prior_name)

    for _ in tqdm(range(n_iter), desc=f"MCMC {prior_name}"):
        alpha_prop = alpha_curr + np.random.normal(0, sigma_alpha)
        beta_prop = beta_curr + np.random.normal(0, sigma_beta)

        if not (-1 <= alpha_prop <= 2 and 0 <= beta_prop <= 2):
            samples.append((alpha_curr, beta_curr))
            continue

        x_sim = gibbs_sampler_ising_periodique_fast(alpha_prop, beta_prop, N, gibbs_iter)
        S_sim = sufficient_statistic(x_sim)
        distance = np.linalg.norm(S_sim - S_obs)

        if distance <= epsilon:
            pi_prop = prior_density(alpha_prop, beta_prop, prior_name)
            if pi_curr == 0:
                ratio = 1
            else:
                ratio = pi_prop / pi_curr
            if np.random.rand() < min(1, ratio):
                alpha_curr, beta_curr = alpha_prop, beta_prop
                pi_curr = pi_prop

        samples.append((alpha_curr, beta_curr))

    return np.array(samples)


def plot_posteriors(samples_dict):
    fig, axes = plt.subplots(2, len(samples_dict), figsize=(16, 6))
    for i, (prior, samples) in enumerate(samples_dict.items()):
        axes[0, i].hist(samples[:, 0], bins=30, density=True, alpha=0.7)
        axes[0, i].set_title(f"alpha - Prior {prior}")
        axes[1, i].hist(samples[:, 1], bins=30, density=True, alpha=0.7)
        axes[1, i].set_title(f"beta - Prior {prior}")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    N = 10
    epsilon = 2.5
    n_iter = 1000
    gibbs_iter = 100
    sigma_alpha = 0.2
    sigma_beta = 0.1

    # Données observées simulées
    alpha_true, beta_true = 0.7, 1.0
    x_obs = gibbs_sampler_ising_periodique_fast(alpha_true, beta_true, N, gibbs_iter)

    priors = ["A", "B", "C", "D"]
    all_samples = {}
    for prior in priors:
        samples = mcmc_abc_flexible_prior(x_obs, N, epsilon, n_iter, gibbs_iter, sigma_alpha, sigma_beta, prior)
        all_samples[prior] = samples

    plot_posteriors(all_samples)