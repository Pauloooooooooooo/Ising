# Ising Model and Approximate Bayesian Computation (ABC)

This repository presents a full implementation of simulation-based Bayesian inference for the Ising model using Approximate Bayesian Computation (ABC) and MCMC-ABC algorithms.

## Project Overview

The Ising model is a classical statistical physics model that describes interactions between binary variables arranged in a 2D grid. In this project, we aim to estimate the parameters \( \alpha \) and \( \beta \) governing the model by leveraging ABC techniques that bypass the intractable likelihood function.

## Objectives

- Implement a Gibbs sampler to simulate data from the Ising model.
- Use ABC-Reject to approximate the posterior distribution of the parameters.
- Implement MCMC-ABC for more efficient posterior approximation.
- Compare the performance and accuracy of both approaches.
- Provide visual diagnostics (trace plots, histograms, posterior comparisons).

## The Ising Model

We consider the Ising model defined on an \( N \times N \) grid:

\[
p(x) \propto \exp\left( \alpha \sum_i x_i + \beta \sum_{i \sim j} \mathbb{1}(x_i = x_j) \right)
\]

Each variable \( x_i \in \{0,1\} \) interacts with its four neighbors (with periodic boundary conditions).

## Methods Implemented

- **Gibbs Sampling**: Local updates based on conditional probabilities to simulate from the joint distribution.
- **ABC-Reject**: Samples parameter values and accepts those leading to simulated data sufficiently close to observed data.
- **MCMC-ABC**: Incorporates Metropolis-Hastings steps within ABC to explore the posterior more efficiently.
- **Advanced MCMC-ABC**: Uses non-uniform priors and asymmetric proposal distributions, with explicit Metropolis ratios.

## Repository Structure


