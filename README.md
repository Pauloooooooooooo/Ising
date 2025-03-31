Ising Model and Approximate Bayesian Computation (ABC)

This repository presents a full implementation of simulation-based Bayesian inference for the Ising model using Approximate Bayesian Computation (ABC) and MCMC-ABC algorithms.

Project Overview

The Ising model is a classical statistical physics model that describes interactions between binary variables arranged in a 2D grid. In this project, we aim to estimate the parameters  and  governing the model by leveraging ABC techniques that bypass the intractable likelihood function.

Objectives

Implement a Gibbs sampler to simulate data from the Ising model.

Use ABC-Reject to approximate the posterior distribution of the parameters.

Implement MCMC-ABC for more efficient posterior approximation.

Compare the performance and accuracy of both approaches.

Provide visual diagnostics (trace plots, histograms, posterior comparisons).

The Ising Model

We consider the Ising model defined on an  grid:



Each variable  interacts with its four neighbors (with periodic boundary conditions).

Methods Implemented

Gibbs Sampling: Local updates based on conditional probabilities to simulate from the joint distribution.

ABC-Reject: Samples parameter values and accepts those leading to simulated data sufficiently close to observed data.

MCMC-ABC: Incorporates Metropolis-Hastings steps within ABC to explore the posterior more efficiently.

Advanced MCMC-ABC: Uses non-uniform priors and asymmetric proposal distributions, with explicit Metropolis ratios.

Repository Structure

ising-abc/
├── src/                        # Python modules
│   ├── gibbs.py                # Gibbs sampler
│   ├── abc_reject.py           # ABC-Reject algorithm
│   ├── mcmc_abc.py             # MCMC-ABC implementations
│   └── utils.py                # Helper functions
├── ising_abc_mcmc.ipynb        # Complete notebook with results
├── figures/                    # Output plots
├── requirements.txt            # Required Python packages
└── README.md                   # This file

Usage

Install dependencies:

pip install -r requirements.txt

Run the code:

python src/run_mcmc.py

Or explore the results in the Jupyter notebook:

jupyter notebook ising_abc_mcmc.ipynb

Key Features

Modular and extensible codebase

Clear comparison between ABC and MCMC-based methods

Visualizations for understanding posterior shape and convergence

Practical demonstration of likelihood-free inference techniques

Author

Developed by [Your Name] as part of a statistical modeling project. For questions or collaborations, feel free to reach out via GitHub or email.

This repository demonstrates applied Bayesian computation using ABC methods on a well-known probabilistic model, with careful implementation, optimization, and diagnostics.
