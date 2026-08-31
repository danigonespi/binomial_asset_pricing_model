# The Binomial Asset Pricing Model

Python implementation of financial derivative pricing models based on the theoretical framework of *Stochastic Calculus for Finance I* (Steven E. Shreve). This project translates rigorous stochastic calculus equations into a modular, scalable, and computationally optimized software architecture.

## Project Status: Milestones Achieved

### Chapter 1 — The Binomial Asset Pricing Model

The core pricing engine is complete and validated, covering the fundamentals of the multi-period binomial model:

* **Decoupled Architecture:** Strict separation between the underlying asset dynamics (`equity_model.py`), payoff definitions (`payoffs.py`), and algorithmic resolution logic (`engines.py`).
* **Payoff Polymorphism:** Unified interface supporting both standard (European) and path-dependent options (e.g., Lookback and Asian Options) without breaking SOLID principles.
* **Algorithmic Optimization (State Reduction):** Implementation of a `ReducedStateEngine` that collapses recombining paths. For path-independent derivatives (call, put), this reduces time complexity from $O(2^N)$ to $O(N^2)$; for path-dependent derivatives like the lookback option, the state reduction to $(S_n, M_n)$ remains polynomial $(O(N^3))$ compared to exhaustive enumeration, allowing trees of $N=50$ to be priced in fractions of a second.
* **Stress Validation:** Exhaustive test suite (`pytest`) that ensures the absence of exponential leaks in compute time and guarantees mathematical fidelity against theoretical examples ("Golden Examples").

### Chapter 2 — Probability Theory on Coin Toss Space

The probabilistic machinery underlying Chapter 1's pricing formulas is now formalized as first-class, independently testable code:

* **Finite Probability Space:** `probability_space.py` introduces `CoinTossSpace`, encapsulating $\Omega_N$, its probability measure, distribution, expectation, and conditional expectation (Definition 2.3.1). It is deliberately decoupled from `BinomialStockModel` — probability (real-world or risk-neutral) is a property of the measure, not of the price process, mirroring Shreve's own separation of the two concepts.
* **Stochastic Property Validators:** `stochastic_properties.py` provides `is_martingale`, `is_submartingale`, `is_supermartingale`, and `is_markov` (both one-dimensional and $K$-dimensional) — standalone computational checks for the properties Shreve proves algebraically in Theorems 2.4.4, 2.4.5, and 2.5.8.
* **New Path-Dependent Payoff:** `DelayedAsianOption` implements the delayed-averaging Asian option of Exercise 2.14, reusing the same `PathDependentPayoff` interface from Chapter 1 without any change to the pricing engines.
* **Extended Theorem Validation:** The golden-example test suite now verifies, against the engines already built in Chapter 1: the divergence between real-world and risk-neutral expectations (Exercise 2.2); the five fundamental properties of conditional expectation (Theorem 2.3.2); the martingale property of the discounted stock price and of the discounted self-financing wealth process (Theorems 2.4.4 and 2.4.5); the exact equivalence between Chapter 1's backward-recursion algorithm and the risk-neutral pricing formula (Exercise 2.8); put-call parity and the chooser option (Exercises 2.11 and 2.12); and the Markov vs. non-Markov distinction, including the book's own running-maximum counterexample (Example 2.5.4) and the Asian-option Markov proofs (Exercises 2.7, 2.13, 2.14).

## Repository Structure

The codebase is organized to clearly separate mathematical theory from implementation and testing:

* **`docs/theory/`**: Theoretical notes in Markdown format. Chapter 1 covers the one-period and multi-period models, computational state reduction, and Asian options (`01`–`04`). Chapter 2 covers finite probability spaces, conditional expectations, martingales, and Markov processes (`05`–`08`).
* **`src/binomial_pricer/`**: Main source code. Contains the model classes, the tree generator (`lattice.py`), the payoff hierarchy (`payoffs.py`), the pricing engines (`engines.py`), the finite probability space (`probability_space.py`), and the martingale/Markov validators (`stochastic_properties.py`).
* **`tests/`**: Unit and integration testing suite validating correct model instantiation, payoff evaluation, algorithmic efficiency of the engines, and the probabilistic properties (martingale, submartingale, supermartingale, Markov) formalized in Chapter 2.
* **`shreve_v1_notebook.ipynb`**: Jupyter Notebook for model analysis, sensitivity studies, and visualization, covering both the deterministic core of Chapter 1 and the probabilistic formalization of Chapter 2.

## Requirements and Usage

The project uses Python 3.10+ and leverages strict typing (Type Hints).

To run the mathematical and computational validation suite:

```bash
# Run all tests
pytest tests/

# Run tests with detailed output
pytest tests/ -v
```

## License

Released under the MIT License — see [LICENSE](LICENSE).