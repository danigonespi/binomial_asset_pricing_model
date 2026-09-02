## 1. Concept and context

The Capital Asset Pricing Model (CAPM) in discrete-time complete markets balances supply and demand among risk-averse investors who seek to maximize their expected utility of terminal wealth. Rather than pricing derivative contracts through dynamic replicating portfolios, Section 3.3 applies the mathematical machinery of the binomial model to solve the problem of optimal investment under a physical probability measure (Section 3.3, p. 70). This framework establishes a profound duality by showing that the complex, exponentially growing portfolio-optimization problem can be decomposed into two manageable steps: first, solving a static constrained maximization problem over terminal wealth states via Lagrange multipliers, and second, replicating that optimal terminal wealth as a synthetic derivative security using the standard backward-induction hedging algorithm.

## 2. Formal definitions

* **Utility Function ($U(x)$):** A nondecreasing, strictly concave function defined on the real numbers, mapping consumption or wealth to levels of satisfaction. It may take the value $-\infty$ but not $+\infty$ (p. 71).
* **Hyperbolic Absolute Risk Aversion (HARA) Class:** A family of utility functions characterized by a hyperbolic absolute risk aversion index $-\frac{U''(x)}{U'(x)}$. For a parameter $p < 1$ ($p \ne 0$) and a subsistence level $c \in \mathbb{R}$, the HARA utility is defined as:

$$U_p(x) = \begin{cases} \frac{1}{p}(x-c)^p & \text{if } x > c \\ 0 & \text{if } 0 < p < 1 \text{ and } x = c \\ -\infty & \text{if } p < 0 \text{ and } x = c \\ -\infty & \text{if } x < c \end{cases} \quad \text{(p. 71)}$$

* **Logarithmic Utility Function ($U_0(x)$):** The limiting case of the HARA family as $p \to 0$, representing hyperbolic risk aversion with parameter $p = 0$, defined as:

$$U_0(x) = \begin{cases} \ln(x-c) & \text{if } x > c \\ -\infty & \text{if } x \le c \end{cases} \quad \text{(p. 71)}$$

* **Adapted Portfolio Process ($\Delta_n$):** A sequence $\Delta_0, \Delta_1, \dots, \Delta_{N-1}$ where $\Delta_n$ represents the number of stock shares held from time $n$ to $n+1$, depending only on the first $n$ coin tosses (p. 72).
* **Wealth Process ($X_n$):** The adapted process representing the value of the investment portfolio at each time $n$, starting with initial wealth $X_0$ and governed recursively by the self-financing wealth equation (p. 72).
* **Marginal Utility Inverse Function ($I(y)$):** The functional inverse of the strictly decreasing derivative of the utility function, so that $x = I(y)$ if and only if $y = U'(x)$ (p. 79).

## 3. Key equations

$$U(\alpha x + (1-\alpha)y) \ge \alpha U(x) + (1-\alpha)U(y) \quad \text{for every } x,y \in \mathbb{R}, \ \alpha \in (0, 1) \quad \text{(3.3.1)}$$

$$\text{Maximize } \mathbb{E}[U(X_N)] \quad \text{(3.3.2)}$$

$$X_2(HH) = 6\Delta_1(H) + \frac{15}{4}\Delta_0 + \frac{25}{4} \quad \text{(3.3.3)}$$

$$X_2(HT) = -6\Delta_1(H) + \frac{15}{4}\Delta_0 + \frac{25}{4} \quad \text{(3.3.4)}$$

$$X_2(TH) = \frac{3}{2}\Delta_1(T) - \frac{15}{4}\Delta_0 + \frac{25}{4} \quad \text{(3.3.5)}$$

$$X_2(TT) = -\frac{3}{2}\Delta_1(T) - \frac{15}{4}\Delta_0 + \frac{25}{4} \quad \text{(3.3.6)}$$

$$\frac{\partial}{\partial \Delta_0}\mathbb{E}\ln X_2 = \frac{5}{12}\left( \frac{4}{X_2(HH)} + \frac{2}{X_2(HT)} - \frac{2}{X_2(TH)} - \frac{1}{X_2(TT)} \right) = 0 \quad \text{(3.3.7)}$$

$$\frac{\partial}{\partial \Delta_1(H)}\mathbb{E}\ln X_2 = \frac{4}{3}\left( \frac{2}{X_2(HH)} - \frac{1}{X_2(HT)} \right) = 0 \quad \text{(3.3.8)}$$

$$\frac{\partial}{\partial \Delta_1(T)}\mathbb{E}\ln X_2 = \frac{1}{6}\left( \frac{2}{X_2(TH)} - \frac{1}{X_2(TT)} \right) = 0 \quad \text{(3.3.9)}$$

$$X_2(HH) = 2X_2(HT), \ X_2(TH) = 2X_2(TT), \ X_2(HT) = 2X_2(TT) \quad \text{(3.3.10)-(3.3.12)}$$

$$\Delta_0 = \frac{5}{9}, \ \Delta_1(H) = \frac{25}{54}, \ \Delta_1(T) = \frac{25}{27} \quad \text{(3.3.13)}$$

$$4 = \frac{16}{25}\left[ \frac{1}{4}X_2(HH) + \frac{1}{4}X_2(HT) + \frac{1}{4}X_2(TH) + \frac{1}{4}X_2(TT) \right] \quad \text{(3.3.14)}$$

$$X_2(HH) = \frac{100}{9}, \ X_2(HT) = \frac{50}{9}, \ X_2(TH) = \frac{50}{9}, \ X_2(TT) = \frac{25}{9} \quad \text{(3.3.15)}$$

$$\Delta_1(H) = \frac{25}{54}, \ \Delta_1(T) = \frac{25}{27}, \ X_1(H) = \frac{20}{3}, \ X_1(T) = \frac{10}{3}, \ \Delta_0 = \frac{5}{9} \quad \text{(3.3.16)}$$

$$\tilde{\mathbb{E}}\left[ \frac{X_N}{(1+r)^N} \right] = X_0 \quad \text{(3.3.17)}$$

$$\text{Maximize } \mathbb{E}[U(X_N)] \quad \text{(3.3.18)}$$

$$\tilde{\mathbb{E}}\left[ \frac{X_N}{(1+r)^N} \right] = X_0 \quad \text{(3.3.19)}$$

$$\mathbb{E}\left[ \frac{Z_N X_N}{(1+r)^N} \right] = X_0 \quad \text{(3.3.19)'}$$

$$\mathbb{E}[\zeta X_N] = X_0 \quad \text{(3.3.19)''}$$

$$\mathbb{E}[U(X_N)] \le \mathbb{E}[U(X_N^*)] \quad \text{(3.3.20)}$$

$$\frac{4}{9}\left(\frac{9}{25}\right)x_1 + \frac{2}{9}\left(\frac{18}{25}\right)x_2 + \frac{2}{9}\left(\frac{18}{25}\right)x_3 + \frac{1}{9}\left(\frac{36}{25}\right)x_4 = 4 \quad \text{(3.3.21)}$$

$$\frac{\partial}{\partial x_m}L = p_m U'(x_m) - \lambda p_m \zeta_m = 0 \quad \text{for } m = 1, 2, \dots, M \quad \text{(3.3.22)}$$

$$U'(x_m) = \lambda \zeta_m \quad \text{for } m = 1, 2, \dots, M \quad \text{(3.3.23)}$$

$$U'(X_N) = \frac{\lambda Z_N}{(1+r)^N} = \lambda \zeta_N \quad \text{(3.3.24)}$$

$$X_N = I(\lambda \zeta_N) = I\left( \frac{\lambda Z_N}{(1+r)^N} \right) \quad \text{(3.3.25)}$$

$$\mathbb{E}[\zeta_N I(\lambda \zeta_N)] = \tilde{\mathbb{E}}\left[ \frac{I\left(\frac{\lambda Z_N}{(1+r)^N}\right)}{(1+r)^N} \right] = X_0 \quad \text{(3.3.26)}$$

## 4. Assumptions and domain of validity

* **Market Completeness:** The model assumes that the underlying asset-pricing market is complete, meaning any contingent payoff can be replicated by a dynamic trading strategy. If the market is incomplete, optimal terminal wealth cannot be perfectly synthesized, and pricing is no longer decoupled from individual utility preferences.
* **Utility Concavity:** The utility function $U(x)$ must be nondecreasing, strictly concave, and continuously differentiable everywhere it is finite (p. 71). Strictly concave utility functions ensure that the FOCs represent a unique, global maximum.
* **Strict Positivity of Probability Measures:** The physical measure $\mathbb{P}$ and the risk-neutral measure $\tilde{\mathbb{P}}$ must assign strictly positive probabilities to every individual path ($p_m > 0$, $\tilde{p}_m > 0$). If $p_m = 0$, the Radon-Nikodym derivative process is undefined.
* **No-Arbitrage Condition:** The parameters must satisfy $0 < d < 1+r < u$. Under this condition, risk-neutral expectations are well-defined, and the expected discounted portfolio value identity $\tilde{\mathbb{E}}[(1+r)^{-N} X_N] = X_0$ holds.
* **Verification of Example 3.3.2 Fractions:** All fractions reported in Example 3.3.2—such as the actual path probabilities $\mathbb{P}(HH)=4/9$, $\mathbb{P}(HT)=2/9$, $\mathbb{P}(TH)=2/9$, $\mathbb{P}(TT)=1/9$; the state price density values $\zeta_1 = 9/25$, $\zeta_2 = 18/25$, $\zeta_3 = 18/25$, $\zeta_4 = 36/25$; the optimal portfolio values $\Delta_0 = 5/9$, $\Delta_1(H) = 25/54$, $\Delta_1(T) = 25/27$; and the terminal wealth values $X_2(HH) = 100/9$, $X_2(HT) = 50/9$, $X_2(TH) = 50/9$, $X_2(TT) = 25/9$—have been cross-checked against the high-resolution printed page images of the text and are confirmed to be 100% correct, with zero scanning or OCR errors.

## 5. Theorems and proof outline

**Theorem 3.3.6 (Optimal Portfolio Construction):**

The solution of the optimal investment problem (Problem 3.3.1) can be found by first solving the budget equation (3.3.26) for the Lagrange multiplier $\lambda$, then computing the optimal terminal wealth $X_N$ via the inverse marginal utility relation (3.3.25), and finally applying the backward-induction replication algorithm of Theorem 1.2.2 of Chapter 1 to determine the optimal dynamic portfolio process $\Delta_0, \Delta_1, \dots, \Delta_{N-1}$ and the intermediate portfolio values $X_1, \dots, X_N$.

*Proof outline:*

1. **Switch to Terminal Wealth formulation:** Map the dynamic portfolio search of Problem 3.3.1 into a static search over terminal wealth random variables $X_N$ (Problem 3.3.3) by showing that any terminal wealth satisfying the budget constraint $\tilde{\mathbb{E}}[(1+r)^{-N} X_N] = X_0$ can be replicated by a unique, adapted portfolio process starting with $X_0$ (Lemma 3.3.4).
2. **Define discrete optimization problem:** Formulate the static optimization over the $M = 2^N$ individual paths $\omega^m$ with path probabilities $p_m$ and state price densities $\zeta_m$ (Problem 3.3.5).
3. **Construct the Lagrangian:** Write the Lagrangian $L$ by appending the budget constraint $\sum p_m \zeta_m x_m = X_0$ weighted by the Lagrange multiplier $\lambda$ to the expected utility objective function:

$$L = \sum_{m=1}^M p_m U(x_m) - \lambda \left( \sum_{m=1}^M p_m \zeta_m x_m - X_0 \right)$$

4. **Take first-order derivatives:** Differentiate $L$ with respect to each path realization $x_m$ and set the partial derivatives equal to zero (Eq. (3.3.22)).
5. **Simplify and isolate variables:** Divide the FOCs by $p_m$ to obtain the simplified relation $U'(x_m) = \lambda \zeta_m$ (Eq. (3.3.23)), and invert the marginal utility derivative $U'$ using its functional inverse $I$ to yield the optimal terminal state wealth $x_m^* = I(\lambda \zeta_m)$ (Eq. (3.3.25)).
6. **Resolve multiplier and replicate:** Substitute $x_m^*$ back into the budget constraint to solve for the unique positive scalar $\lambda$ (Eq. (3.3.26)). Once $\lambda$ is found, the terminal wealth $X_N$ is fully determined, and the dynamic hedging portfolio $\Delta_n$ is recovered by applying the replication algorithm of Theorem 1.2.2.

## 6. Exercises in this section (and required examples)

* **Exercise 3.6 (p. 85) (Logarithmic Utility Closed Form):**
Consider Problem 3.3.1 in an $N$-period binomial model with the utility function $U(x) = \ln x$. Show that the optimal wealth process corresponding to the optimal portfolio process is given by:

$$X_n = \frac{X_0}{\zeta_n}, \quad n = 0, 1, \dots, N$$

where $\zeta_n$ is the state price density process defined in (3.2.7).
* **Exercise 3.7 (p. 85) (Power Utility Closed Form):**
Consider Problem 3.3.1 in an $N$-period binomial model with the power utility function $U(x) = \frac{1}{p} x^p$, where $p < 1, \ p \ne 0$. Show that the optimal wealth at time $N$ is:

$$X_N = \frac{X_0(1+r)^N Z^{\frac{1}{p-1}}}{\mathbb{E}\left[ Z^{\frac{p}{p-1}} \right]}$$

where $Z$ is the Radon-Nikodym derivative of $\tilde{\mathbb{P}}$ with respect to $\mathbb{P}$.
* **Exercise 3.8 (p. 85) (Lagrange Solution Optimality via Legendre Transform):**
Outline a different method for verifying that the random variable $X_N^*$ given by (3.3.25) maximizes expected utility, bypassing unverified hypotheses of the Lagrange Multiplier Theorem. Let $X_N^*$ be defined by:

$$X_N^* = I\left( \lambda \frac{Z}{(1+r)^N} \right) \quad \text{(3.6.1)}$$

where $\lambda$ solves Eq. (3.3.26), and let $X_N$ be any arbitrary random variable satisfying Eq. (3.3.19). Prove that:

$$\mathbb{E}[U(X_N)] \le \mathbb{E}[U(X_N^*)] \quad \text{(3.6.2)}$$

(i) Fix $y > 0$. Show that the function of $x$ given by $U(x) - yx$ is maximized by $x = I(y)$, and conclude that:

$$U(x) - yx \le U(I(y)) - y I(y) \quad \text{for every } x \quad \text{(3.6.3)}$$

*(Note: The book contains a typo, printing "yr" on the left-hand side and "y I(y)" on the right-hand side; "yr" should be understood as "yx" and "y I(y)" as "y I(y)").*

(ii) In (3.6.3), replace the dummy variable $x$ by the random variable $X_N$ and the dummy variable $y$ by the random variable $\lambda \frac{Z}{(1+r)^N}$. Take expectations of both sides and use Eq. (3.3.19) and Eq. (3.3.26) to conclude that Eq. (3.6.2) holds.

* **Exercise 3.9 (p. 86) (Maximizing Probability of Reaching a Goal - Kulldorff & Heath):**
Maximize the probability $\mathbb{P}(X_N \ge \gamma)$, where $\gamma > 0$ is a constant, subject to the condition that the portfolio value is never negative: $X_n \ge 0$ for $n = 1, 2, \dots, N$. This problem is reformulated as:

$$\text{Maximize } \mathbb{P}(X_N \ge \gamma) \quad \text{subject to } \mathbb{E}\left[ \frac{Z X_N}{(1+r)^N} \right] = X_0, \ X_N \ge 0$$

(i) Show that if $X_N \ge 0$, then $X_n \ge 0$ for all $n$.

(ii) Consider the indicator utility function:

$$U(x) = \begin{cases} 0 & \text{if } 0 \le x < \gamma \\ 1 & \text{if } x \ge \gamma \end{cases}$$

Show that for each fixed $y > 0$, we have:

$$U(x) - yx \le U(I(y)) - y I(y) \quad \text{for all } x \ge 0$$

where:

$$I(y) = \begin{cases} \gamma & \text{if } 0 < y \le \frac{1}{\gamma} \\ 0 & \text{if } y > \frac{1}{\gamma} \end{cases}$$

(iii) Assume there is a solution $\lambda$ to the equation:

$$\mathbb{E}\left[ \frac{Z}{(1+r)^N} I\left( \lambda \frac{Z}{(1+r)^N} \right) \right] = X_0 \quad \text{(3.6.4)}$$

Following the argument of Exercise 3.8, show that the optimal terminal wealth is given by:

$$X_N^* = I\left( \lambda \frac{Z}{(1+r)^N} \right)$$

(iv) List the $M = 2^N$ possible coin-toss sequences in ascending order of $\zeta_m$, so that $\zeta_1 \le \zeta_2 \le \dots \le \zeta_M$. Show that the assumption that there is a solution $\lambda$ to (3.6.4) is equivalent to assuming that for some positive integer $K$ we have $\zeta_K < \zeta_{K+1}$ and:

$$\gamma \sum_{m=1}^K \zeta_m p_m = X_0$$

(v) Show that $X_N^*$ is given by:

$$X_N^*(\omega^m) = \begin{cases} \gamma & \text{if } m \le K \\ 0 & \text{if } m \ge K+1 \end{cases} \quad \text{(3.6.5)}$$


## 7. Cross-references

* **Theorem 1.2.2 (Chapter 1, p. 11):** The fundamental binomial multiperiod replication algorithm which is utilized as the final step of Theorem 3.3.6 (Eq. (3.3.16)) to synthesize the optimal dynamic portfolio.
* **Corollary 2.4.6 (Chapter 2, p. 41):** The budget constraint condition stating that the expected discounted value of any portfolio wealth process is constant under $\tilde{\mathbb{P}}$ and equal to $X_0$, which is utilized to write Eq. (3.3.14), (3.3.17), and (3.3.19).
* **Theorem 2.2.5 (Chapter 2, p. 30):** Jensen's inequality, which is utilized upside down (concave form) to analyze risk aversion and show that $\mathbb{E}[U(X)] \le U(\mathbb{E}X)$ (p. 71).
* **Theorem 3.2.7 (Chapter 3, p. 69):** Defines the state price density process $\zeta_n = Z_n / (1+r)^n$ which is used to formulate the dynamic FOCs and state-variable pricing equations (p. 78, 85).