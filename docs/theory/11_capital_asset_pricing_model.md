## 1. Concept and context

The Capital Asset Pricing Model (CAPM) in discrete-time complete markets balances supply and demand among risk-averse investors who seek to maximize their expected utility of terminal wealth. Rather than pricing derivative contracts through dynamic replicating portfolios, Section 3.3 applies the mathematical machinery of the binomial model to solve the problem of optimal investment under the actual probability measure. This framework decomposes the exponentially-growing portfolio-optimization problem into two manageable steps: first, solving a static constrained maximization problem over terminal wealth states via Lagrange multipliers, and second, replicating that optimal terminal wealth as a synthetic derivative security using the backward-induction hedging algorithm of Chapter 1 (Section 3.3, p. 70).

## 2. Formal definitions

* **Utility Function ($U(x)$):** A nondecreasing, concave function defined on the real numbers, mapping wealth to satisfaction. It may take the value $-\infty$ but not $+\infty$. Assumed strictly concave everywhere it is finite (p. 71).
* **HARA Class ($U_p(x)$):** For a parameter $p<1$ ($p\ne0$) and subsistence level $c\in\mathbb{R}$:

$$U_p(x) = \begin{cases} \frac{1}{p}(x-c)^p & \text{if } x > c \\ 0 & \text{if } 0 < p < 1 \text{ and } x = c \\ -\infty & \text{if } p < 0 \text{ and } x = c \\ -\infty & \text{if } x < c \end{cases} \quad \text{(p. 71)}$$

  The index of absolute risk aversion, $-U''(x)/U'(x)$, is the hyperbolic function $1/(x-c)$ — hence "Hyperbolic Absolute Risk Aversion".
* **Logarithmic Utility ($U_0(x)$):** The $p\to0$ limiting case of the HARA family:

$$U_0(x) = \begin{cases} \ln(x-c) & \text{if } x > c \\ -\infty & \text{if } x \le c \end{cases} \quad \text{(p. 71)}$$

* **Adapted Portfolio Process ($\Delta_n$):** As in Chapter 2 — $\Delta_n$ depends only on the first $n$ coin tosses (p. 72).
* **Wealth Process ($X_n$):** Generated recursively from $X_0$ by the self-financing wealth equation (p. 72).
* **Marginal Utility Inverse Function ($I(y)$):** The functional inverse of the strictly decreasing derivative $U'$: $x=I(y)$ if and only if $y=U'(x)$ (p. 80).

## 3. Key equations

$$U(\alpha x + (1-\alpha)y) \ge \alpha U(x) + (1-\alpha)U(y) \quad \text{for every } x,y \in \mathbb{R}, \ \alpha \in (0,1) \quad \text{(3.3.1)}$$

$$\text{Maximize } \mathbb{E}[U(X_N)] \quad \text{(3.3.2)}$$

$$X_2(HH) = 6\Delta_1(H) + \frac{15}{4}\Delta_0 + \frac{25}{4} \quad \text{(3.3.3)}$$

$$X_2(HT) = -6\Delta_1(H) + \frac{15}{4}\Delta_0 + \frac{25}{4} \quad \text{(3.3.4)}$$

$$X_2(TH) = \frac{3}{2}\Delta_1(T) - \frac{15}{4}\Delta_0 + \frac{25}{4} \quad \text{(3.3.5)}$$

$$X_2(TT) = -\frac{3}{2}\Delta_1(T) - \frac{15}{4}\Delta_0 + \frac{25}{4} \quad \text{(3.3.6)}$$

$$\frac{4}{X_2(HH)} + \frac{2}{X_2(HT)} = \frac{2}{X_2(TH)} + \frac{1}{X_2(TT)} \quad \text{(3.3.7)}$$

$$\frac{2}{X_2(HH)} = \frac{1}{X_2(HT)} \quad \text{(3.3.8)}$$

$$\frac{2}{X_2(TH)} = \frac{1}{X_2(TT)} \quad \text{(3.3.9)}$$

$$X_2(HH) = 2X_2(HT) \quad \text{(3.3.10)}$$

$$X_2(TH) = 2X_2(TT) \quad \text{(3.3.11)}$$

$$X_2(HT) = 2X_2(TT) \quad \text{(3.3.12)}$$

$$\Delta_0 = \frac{5}{9}, \quad \Delta_1(H) = \frac{25}{54}, \quad \Delta_1(T) = \frac{25}{27} \quad \text{(3.3.13)}$$

$$4 = \frac{16}{25}\left[ \frac{1}{4}X_2(HH) + \frac{1}{4}X_2(HT) + \frac{1}{4}X_2(TH) + \frac{1}{4}X_2(TT) \right] \quad \text{(3.3.14)}$$

$$X_2(HH) = \frac{100}{9}, \ X_2(HT) = \frac{50}{9}, \ X_2(TH) = \frac{50}{9}, \ X_2(TT) = \frac{25}{9} \quad \text{(3.3.15)}$$

$$\Delta_1(H) = \frac{25}{54}, \ \Delta_1(T) = \frac{25}{27}, \ X_1(H) = \frac{20}{3}, \ X_1(T) = \frac{10}{3}, \ \Delta_0 = \frac{5}{9} \quad \text{(3.3.16)}$$

$$\tilde{\mathbb{E}}\left[ \frac{X_N}{(1+r)^N} \right] = X_0 \quad \text{(3.3.17)}$$

$$\text{Maximize } \mathbb{E}[U(X_N)] \quad \text{(3.3.18)}$$

$$\tilde{\mathbb{E}}\left[ \frac{X_N}{(1+r)^N} \right] = X_0 \quad \text{(3.3.19)}$$

$$\mathbb{E}\left[ \frac{Z_N X_N}{(1+r)^N} \right] = X_0 \quad \text{(3.3.19)'}$$

$$\mathbb{E}[\zeta X_N] = X_0 \quad \text{(3.3.19)''}$$

$$\mathbb{E}[U(X_N)] \le \mathbb{E}[U(X_N^*)] \quad \text{(3.3.20)}$$

$$\frac{4}{9}\cdot\frac{9}{25}x_1 + \frac{2}{9}\cdot\frac{18}{25}x_2 + \frac{2}{9}\cdot\frac{18}{25}x_3 + \frac{1}{9}\cdot\frac{36}{25}x_4 = 4 \quad \text{(3.3.21)}$$

$$\frac{\partial}{\partial x_m}L = p_m U'(x_m) - \lambda p_m \zeta_m = 0, \quad m = 1, 2, \dots, M \quad \text{(3.3.22)}$$

$$U'(x_m) = \lambda \zeta_m, \quad m = 1, 2, \dots, M \quad \text{(3.3.23)}$$

$$U'(X_N) = \frac{\lambda Z}{(1+r)^N} \quad \text{(3.3.24)}$$

$$X_N = I\left( \frac{\lambda Z}{(1+r)^N} \right) \quad \text{(3.3.25)}$$

$$\mathbb{E}\left[ \frac{Z}{(1+r)^N} I\left( \frac{\lambda Z}{(1+r)^N} \right) \right] = X_0 \quad \text{(3.3.26)}$$

*(Note: (3.3.24)-(3.3.26) are printed in the book using the plain terminal random variable $Z$, not the subscripted $Z_N$/$\zeta_N$ notation of Section 3.2 — even though $Z_N=Z$ by Definition 3.2.4. Preserved here exactly as printed rather than harmonized.)*

## 4. Assumptions and domain of validity

* **Market Completeness:** The market must be complete — any contingent payoff can be replicated by a dynamic trading strategy. If incomplete, optimal terminal wealth cannot be perfectly synthesized and pricing is no longer decoupled from individual utility preferences.
* **Utility Concavity:** $U(x)$ must be nondecreasing and strictly concave everywhere it is finite. The book does not separately name "continuous differentiability" as a hypothesis, but Theorem 3.3.6's construction of $I$ as the inverse of $U'$ implicitly requires $U'$ to exist and be (strictly) decreasing.
* **Strict Positivity of Probability Measures:** $\mathbb{P}$ and $\tilde{\mathbb{P}}$ must assign strictly positive probability to every path ($p_m>0$). If $p_m=0$, the Radon-Nikodym derivative process is undefined.
* **No-Arbitrage Condition:** $0<d<1+r<u$, inherited from Section 1.1, so that risk-neutral expectations are well-defined and $\tilde{\mathbb{E}}[(1+r)^{-N}X_N]=X_0$ holds for any self-financing wealth process.

## 5. Theorems and proof outline

**Lemma 3.3.4:** Suppose $\Delta_0^*,\Delta_1^*,\dots,\Delta_{N-1}^*$ is an optimal portfolio process for Problem 3.3.1, and $X_N^*$ is the corresponding optimal wealth random variable at time $N$. Then $X_N^*$ is optimal for Problem 3.3.3. Conversely, suppose $X_N^*$ is optimal for Problem 3.3.3. Then there is a portfolio process $\Delta_0^*,\dots,\Delta_{N-1}^*$ that starts with initial wealth $X_0$ and has value $X_N^*$ at time $N$, and this portfolio process is optimal for Problem 3.3.1.

*Proof outline:*

1. **Forward direction:** assume $\Delta_0^*,\dots$ optimal for Problem 3.3.1 with terminal wealth $X_N^*$. Since it is generated by a portfolio process starting at $X_0$, it satisfies the constraint (3.3.17)=(3.3.19).
2. Let $X_N$ be any other random variable satisfying (3.3.19). Regard $X_N$ as a derivative security; by the risk-neutral pricing formula (2.4.11) of Chapter 2, its time-zero price is $X_0$.
3. Using the replication algorithm of Theorem 1.2.2 of Chapter 1, construct a portfolio process starting at $X_0$ whose value at time $N$ is $X_N$.
4. Since $\Delta_0^*,\dots$ is optimal for Problem 3.3.1 and this is another admissible portfolio process, $\mathbb{E}U(X_N)\le\mathbb{E}U(X_N^*)$ — proving $X_N^*$ optimal for Problem 3.3.3.
5. **Converse direction:** suppose $X_N^*$ is optimal for Problem 3.3.3. Using Theorem 1.2.2 again, construct a portfolio process starting at $X_0$ with terminal value $X_N^*$.
6. For any other portfolio process starting at $X_0$ with terminal wealth $X_N$, $X_N$ satisfies (3.3.19), and since $X_N^*$ is optimal for Problem 3.3.3, $\mathbb{E}U(X_N)\le\mathbb{E}U(X_N^*)$ — establishing optimality of this portfolio process for Problem 3.3.1.

---

**Theorem 3.3.6 (Optimal Portfolio Construction):** The solution of Problem 3.3.1 can be found by first solving equation (3.3.26) for $\lambda$, then computing $X_N$ by (3.3.25), and finally using $X_N$ in the algorithm of Theorem 1.2.2 of Chapter 1 to determine the optimal portfolio process $\Delta_0,\dots,\Delta_{N-1}$ and the corresponding portfolio value process $X_1,\dots,X_N$. The function $I$ appearing in (3.3.26) is the functional inverse of $U'$.

*(The book states this theorem as a summary of the preceding derivation rather than proving it separately — the "proof" below recaps that derivation, it is not a new argument.)*

1. Map the dynamic search of Problem 3.3.1 into the static search over terminal wealth of Problem 3.3.3, via Lemma 3.3.4.
2. Reformulate over the $M=2^N$ paths $\omega^m$ with probabilities $p_m$ and state price densities $\zeta_m$ (Problem 3.3.5).
3. Form the Lagrangian $L=\sum_m p_mU(x_m) - \lambda(\sum_m p_m\zeta_mx_m - X_0)$ and differentiate to obtain (3.3.22).
4. Divide by $p_m$ to get $U'(x_m)=\lambda\zeta_m$ (3.3.23), equivalently $U'(X_N)=\lambda Z/(1+r)^N$ (3.3.24).
5. Invert $U'$ via $I$ to get $X_N=I(\lambda Z/(1+r)^N)$ (3.3.25).
6. Substitute into the budget constraint (3.3.19)' to solve for $\lambda$ via (3.3.26); then replicate $X_N$ using Theorem 1.2.2.

## 6. Exercises in this section (and required examples)

* **Example 3.3.2 (Two-period optimal investment under log utility):** In the two-period model of Figure 3.3.1 ($S_0=4$, $S_1(H)=8$, $S_1(T)=2$, $S_2(HH)=16$, $S_2(HT)=S_2(TH)=4$, $S_2(TT)=1$, $r=1/4$), with actual probabilities $\mathbb{P}(HH)=4/9,\mathbb{P}(HT)=2/9,\mathbb{P}(TH)=2/9,\mathbb{P}(TT)=1/9$ and $X_0=4$, an agent maximizes $\mathbb{E}\ln X_2$. The first (direct) method substitutes the wealth formulas (3.3.3)-(3.3.6) into the first-order conditions (3.3.7)-(3.3.9), yielding the linear system (3.3.10)-(3.3.12) and the solution (3.3.13). The second (state-price) method instead adds the budget-constraint equation (3.3.14) from Corollary 2.4.6 of Chapter 2, solves for $X_2$ directly (3.3.15), and recovers $\Delta_1(H),\Delta_1(T),X_1(H),X_1(T),\Delta_0$ via the backward-induction algorithm of Theorem 1.2.2 (3.3.16) — matching (3.3.13). The example is then continued (p. 76-78) using the Radon-Nikodym derivative $Z(HH)=9/16$, $Z(HT)=Z(TH)=9/8$, $Z(TT)=9/4$, giving state price densities $\zeta_1=9/25$ (HH), $\zeta_2=\zeta_3=18/25$ (HT, TH), $\zeta_4=36/25$ (TT); Problem 3.3.3 is rewritten as a Lagrangian over $x_1,\dots,x_4$ (3.3.21), giving $\lambda=1/4$ and reproducing (3.3.15).
* **Exercise 3.6 (Logarithmic utility closed form):** Consider Problem 3.3.1 in an $N$-period binomial model with $U(x)=\ln x$. Show that the optimal wealth process is $X_n = X_0/\zeta_n$, $n=0,1,\dots,N$, where $\zeta_n$ is the state price density process of (3.2.7).
* **Exercise 3.7 (Power utility closed form):** Consider Problem 3.3.1 with $U(x)=\frac{1}{p}x^p$, $p<1$, $p\ne0$. Show that the optimal wealth at time $N$ is

$$X_N = \frac{X_0(1+r)^N Z^{\frac{1}{p-1}}}{\mathbb{E}\left[Z^{\frac{p}{p-1}}\right]}$$

  where $Z$ is the Radon-Nikodym derivative of $\tilde{\mathbb{P}}$ with respect to $\mathbb{P}$.
* **Exercise 3.8 (Verifying optimality via a direct argument):** The Lagrange Multiplier Theorem used in solving Problem 3.3.5 has hypotheses not verified there. This exercise outlines a different method to confirm that $X_N^*=I\left(\frac{\lambda}{(1+r)^N}Z\right)$ (3.6.1), with $\lambda$ solving (3.3.26), maximizes expected utility among all $X_N$ satisfying (3.3.19), i.e. $\mathbb{E}U(X_N)\le\mathbb{E}U(X_N^*)$ (3.6.2).
  (i) Fix $y>0$. Show the function of $x$ given by $U(x)-yx$ is maximized at $x=I(y)$, concluding $U(x)-yx \le U(I(y))-yI(y)$ for every $x$ (3.6.3).
  (ii) In (3.6.3), replace $x$ by $X_N$ and $y$ by $\lambda Z/(1+r)^N$; take expectations of both sides and use (3.3.19) and (3.3.26) to conclude (3.6.2) holds.
* **Exercise 3.9 (Maximizing probability of reaching a goal) (Kulldorff, Heath):** An investor provides initial wealth $X_0$; the goal is to

$$\text{Maximize } \mathbb{P}(X_N \ge \gamma)$$

  where $X_N$ is generated by a portfolio process beginning at $X_0$ with $X_n\ge0$, $n=1,\dots,N$, and $\gamma>0$ is a constant. As Problem 3.3.1 was reformulated as Problem 3.3.3, this may be reformulated as: Maximize $\mathbb{P}(X_N\ge\gamma)$ subject to $\tilde{\mathbb{E}}[X_N/(1+r)^N]=X_0$, $X_n\ge0$, $n=1,\dots,N$.
  (i) Show that if $X_N\ge0$, then $X_n\ge0$ for all $n$.
  (ii) Consider the indicator utility $U(x)=0$ if $0\le x<\gamma$, $U(x)=1$ if $x\ge\gamma$. Show that for each fixed $y>0$, $U(x)-yx \le U(I(y))-yI(y)$ for all $x\ge0$, where $I(y)=\gamma$ if $0<y\le1/\gamma$, $I(y)=0$ if $y>1/\gamma$.
  (iii) Assume there is a solution $\lambda$ to $\mathbb{E}\left[\frac{Z}{(1+r)^N}I\left(\frac{\lambda Z}{(1+r)^N}\right)\right]=X_0$ (3.6.4). Following the argument of Exercise 3.8, show the optimal terminal wealth is $X_N^*=I\left(\frac{\lambda Z}{(1+r)^N}\right)$.
  (iv) List the $M=2^N$ coin-toss sequences $\omega^1,\dots,\omega^M$ in ascending order of $\zeta_m=\zeta(\omega^m)$, so $\zeta_1\le\zeta_2\le\dots\le\zeta_M$. Show that the assumption of a solution $\lambda$ to (3.6.4) is equivalent to assuming that for some positive integer $K$, $\zeta_K<\zeta_{K+1}$ and $\sum_{m=1}^K\zeta_mp_m = X_0/\gamma$.
  (v) Show that $X_N^*$ is given by $X_N^*(\omega^m)=\gamma$ if $m\le K$, $X_N^*(\omega^m)=0$ if $m\ge K+1$ (3.6.5).

## 7. Cross-references

* **Theorem 1.2.2 (Chapter 1, p. 11):** The multiperiod replication algorithm, used both in Lemma 3.3.4's proof and as the final step of Theorem 3.3.6.
* **Corollary 2.4.6 (Chapter 2, p. 41):** The identity $\tilde{\mathbb{E}}[(1+r)^{-N}X_N]=X_0$ for any self-financing wealth process, used to write (3.3.14), (3.3.17), and (3.3.19).
* **Theorem 2.2.5 (Chapter 2):** Jensen's inequality used "upside down" (concave form) to motivate risk aversion, $\mathbb{E}[U(X)]\le U(\mathbb{E}X)$ (p. 71).
* **Theorem 2.4.7 (Chapter 2, risk-neutral pricing formula, eq. 2.4.11):** Used in Lemma 3.3.4's proof to price an arbitrary terminal wealth as a derivative security.
* **Theorem 3.2.7 (Section 3.2, p. 69):** Defines $\zeta_n=Z_n/(1+r)^n$, used throughout the FOCs and Exercise 3.6.