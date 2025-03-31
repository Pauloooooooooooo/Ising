# Ising Model and Approximate Bayesian Computation (ABC)

This repository presents a complete implementation of simulation-based Bayesian inference for the Ising model using Approximate Bayesian Computation (ABC) and MCMC-ABC algorithms.

## Project Overview

The Ising model is a classical statistical physics model describing interactions between binary variables arranged on a 2D grid. The goal of this project is to estimate the parameters alpha and beta governing the model using simulation techniques that avoid evaluating the intractable likelihood.

## Objectives

- Implement a Gibbs sampler to simulate data from the Ising model.
- Use ABC-Reject to approximate the posterior distribution of the parameters.
- Implement MCMC-ABC to improve sampling efficiency.
- Compare the accuracy and performance of both approaches.
- Provide visual diagnostics (trace plots, posterior histograms, trajectory plots).

## The Ising Model

We consider the Ising model on an N x N grid. Each variable x_i ∈ {0, 1} interacts with its 4 neighbors (with periodic boundary conditions).

The probability distribution is defined up to a constant as:

    p(x) ∝ exp( alpha * sum_i x_i + beta * sum_{i~j} 1{x_i = x_j} )

Where:
- alpha controls the global tendency for spins to be 1,
- beta controls local alignment (higher beta favors similar neighboring values),
- sum_{i~j} runs over all neighboring pairs.

## Methods Implemented

- **Gibbs Sampling**: Iteratively updates each pixel using its full conditional distribution.
- **ABC-Reject**: Samples parameters from the prior, simulates data, and accepts if the simulated statistics are close to the observed ones.
- **MCMC-ABC**: Uses Metropolis-Hastings with ABC to explore the posterior distribution more efficiently.
- **Advanced MCMC-ABC**: Includes non-uniform priors and asymmetric proposal distributions, with proper Metropolis ratio calculation.

## Repository Structure



