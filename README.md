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

### Chapter 3 — State Prices

* **Static Change of Measure:** Formalizes the Radon-Nikodym derivative $Z(\omega)$ and the state price density $\zeta(\omega)$ to execute a change of measure over the entire multiperiod tree, eliminating the need to solve replication equations directly (Section 3.1).
* **Dynamic Change of Measure:** Derives the Radon-Nikodym derivative process $Z_n$, which is a martingale under the actual measure (Theorem 3.2.1), and the state price density process $\zeta_n = Z_n/(1+r)^n$, which is **not** a martingale — dividing a martingale by a deterministic, strictly increasing discount factor makes it a supermartingale — to price intermediate nodes via the three-equality chain of Theorem 3.2.7 (Section 3.2).
* **Capital Asset Pricing:** Decouples optimal investment into a static Lagrangian constraint over terminal wealth states followed by standard replication. Implements exact closed-form solvers for the Logarithmic and Power utilities, a generic `scipy.optimize.brentq` solver for the general non-linear case, and a dedicated threshold-based solver for the non-differentiable Goal (probability-maximization) utility of Exercise 3.9, whose step-function marginal utility cannot be inverted continuously (Section 3.3).
* **Cross-Validation:** Golden examples guarantee numeric adherence between the generic `brentq` optimal-inversion algorithm and the closed-form Power-utility solution (Exercise 3.7); the closed-form Logarithmic-utility solution is validated independently via Example 3.3.2.

### Chapter 4 — American Derivative Securities

* **Early-Exercise Architecture:** Implementation of `AmericanEngine`, extending the backward-induction algorithm to handle early-exercise decisions. It reuses the state-reduction mechanics (e.g., evaluating $(S_n, M_n)$ or $(S_n, Y_n)$) while substituting the plain risk-neutral expectation with the maximum against the intrinsic value at every node.
* **The Consumption Process:** The engine computes the nonnegative consumption process ($C_n$), explicitly tracking the capital withdrawn from the replicating portfolio when early exercise is strictly optimal, keeping the hedge self-financing.
* **Stopping Times & Optional Sampling:** `stochastic_properties.py` introduces `is_stopping_time` to validate non-anticipating exercise policies and `stop_process` to freeze processes dynamically. Validates the Optional Sampling Theorem, demonstrating computationally that while the discounted American price is a supermartingale, stopping it at the optimal exercise time turns it into a martingale.
* **Path-Dependent Extensions:** Introduces `RunningAveragePut` to demonstrate the algorithm's capability to price path-dependent American options (Exercise 4.3) using generalized intrinsic value tracking ($G_n$).
* **Theorem Validation:** Computationally validates Theorem 4.5.1 across a full strike curve, proving the early-exercise premium for an American call on a non-dividend-paying stock is strictly zero. Automatically maps the multi-period early-exercise boundary (the critical stock price curve) for American puts.

### Chapter 5 — Random Walk

* **Random Walk and First Passage Times:** `random_walk.py` studies the symmetric random walk $M_n$ as a purely probabilistic object, with no dependency on `BinomialStockModel`. It provides the walk, the first passage time $\tau_m$ (Eq. 5.2.1), the exponential martingale of Lemma 5.2.1, the closed-form moment-generating function $\mathbb{E}\alpha^{\tau_m}$ (Theorem 5.2.3) and the exact distribution of $\tau_1$ for any up-step probability $p$ (Theorem 5.2.5).
* **Reflection Principle:** the same distribution is recomputed by pure path counting (Section 5.3) in a function that shares no code with the moment-generating-function route, so their agreement is a genuine cross-validation. The reflected-path formula of Exercise 5.5(i) for the joint law of the walk and its running maximum is extended to asymmetric walks (Exercise 5.5(ii)): the number of paths in the event is independent of $p$, and every path ending at $b$ has exponents $(n+b)/2$ and $(n-b)/2$ on $p$ and $q$.
* **Perpetual American Options:** `perpetual_american.py` gives the closed-form value, consumption and hedge of the perpetual American put (Section 5.4, Exercises 5.7 and 5.9, with the strike generalised through the smooth-pasting condition $s_B=K/2$, $B=(K/2)^2$) and the perpetual call of Exercise 5.8, together with a Bellman-equation residual (Eq. 5.4.16). Eq. (5.7.3) is printed in the book with a factor $\tfrac12$ missing on one term; the implementation uses the symmetric continuation value of Eq. (5.4.13).
* **Cross-Validation:** golden examples reproduce the first passage probabilities of p. 126, Figure 5.3.1, the policy values of p. 130, Figure 5.4.1 and the finite-horizon prices of Exercise 5.6 (0.80, 0.928, 0.96896). Generic tests check that Chapter 4's `AmericanEngine` converges monotonically to the perpetual put formula as the expiration grows, and that the perpetual call is never exercised early.

## Repository Structure

The codebase is organized to clearly separate mathematical theory from implementation and testing:

* **`docs/theory/`**: Theoretical notes in Markdown format. Chapter 1 covers the one-period and multi-period models, computational state reduction, and Asian options (`01`–`04`). Chapter 2 covers finite probability spaces, conditional expectations, martingales, and Markov processes (`05`–`08`). Chapter 3 covers the static and dynamic change of measure and capital asset pricing (`09`–`11`). Chapter 4 covers American derivatives, stopping times, and American calls (`12`–`15`). Chapter 5 covers first passage times, the reflection principle, and the perpetual American put (`16`–`18`).
* **`src/binomial_pricer/`**: Main source code. Contains the model classes, the tree generator (`lattice.py`), the payoff hierarchy (`payoffs.py`), the pricing engines (`engines.py`, `american_engine.py`), the finite probability space (`probability_space.py`), the martingale/Markov/stopping-time validators (`stochastic_properties.py`), the state price density and its process (`state_prices.py`), the optimal-investment utility solvers (`optimal_investment.py`), the random walk and first passage machinery (`random_walk.py`), and the perpetual American options (`perpetual_american.py`).
* **`tests/`**: Unit and integration testing suite. Each `test_<module>.py` exercises its module with generic parameters, while `test_golden_examples.py` reproduces the exact examples and exercises of the book, always cross-validating two independent computation routes.
* **`shreve_v1_notebook.ipynb`**: Jupyter Notebook for model analysis, sensitivity studies, and visualization, covering Chapters 1 to 5.

## Requirements and Usage

The project uses Python 3.10+ and leverages strict typing (Type Hints).

To run the mathematical and computational validation suite:

```bash
# Run all tests
pytest tests/

# Run tests with detailed output
pytest tests/ -v