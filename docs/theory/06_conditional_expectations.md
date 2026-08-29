1. **Concept and context**

   The concept of conditional expectation formalizes the process of updating estimates of a random variable as new information is revealed over time. By averaging a contingent payoff over all future continuations of a coin-toss sequence based on the tosses already observed, the conditional expectation resolves into a new random variable representing a dynamic estimate at that intermediate time. This mathematical construction acts as the essential bridge between the static, time-zero expectations of Chapter 2 and the dynamic, multiperiod martingales developed in the rest of the book (Section 2.3, pages 31–33).

2. **Formal definitions**

   * $n$: Given and fixed time index satisfying $1 \le n \le N$.
   * $\omega_1 \dots \omega_n$: Given and fixed sequence of the first $n$ coin tosses.
   * $\omega_{n+1} \dots \omega_N$: Continuation sequence of coin tosses, with $2^{N-n}$ possible continuations.
   * $\\#H(\omega_{n+1} \dots \omega_N)$: Number of heads in the continuation sequence.
   * $\\#T(\omega_{n+1} \dots \omega_N)$: Number of tails in the continuation sequence.
   * $\mathbb{E}_n[X]$: Conditional expectation of $X$ based on the information at time $n$ (Definition 2.3.1).
   * $\tilde{\mathbb{E}}_n[X]$: Conditional expectation of $X$ computed under the risk-neutral probabilities $\tilde{p}$ and $\tilde{q}$.
   * $\mathbb{E}_0[X]$: Conditional expectation based on no information, defined as $\mathbb{E}_0[X] = \mathbb{E}X$.
   * $\mathbb{E}_N[X]$: Conditional expectation based on full information, defined as $\mathbb{E}_N[X] = X$.

3. **Key equations**

   $$\tilde{p} = \frac{1+r-d}{u-d}, \quad \tilde{q} = \frac{u-1-r}{u-d} \quad \text{(2.3.1)}$$

   $$\frac{\tilde{p}u+\tilde{q}d}{1+r} = 1 \quad \text{(2.3.2)}$$

   $$S_n(\omega_1 \dots \omega_n) = \frac{1}{1+r} [ \tilde{p} S_{n+1}(\omega_1 \dots \omega_n H) + \tilde{q} S_{n+1}(\omega_1 \dots \omega_n T) ] \quad \text{(2.3.3)}$$

   ```math
   \tilde{\mathbb{E}}_n[S_{n+1}](\omega_1 \dots \omega_n) = \tilde{p} S_{n+1}(\omega_1 \dots \omega_n H) + \tilde{q} S_{n+1}(\omega_1 \dots \omega_n T) \quad \text{(2.3.4)}
   ```

   ```math
   S_n = \frac{1}{1+r} \tilde{\mathbb{E}}_n[S_{n+1}] \quad \text{(2.3.5)}
   ```

   ```math
   \mathbb{E}_n[X](\omega_1 \dots \omega_n) = \sum_{\omega_{n+1} \dots \omega_N} p^{\\#H(\omega_{n+1} \dots \omega_N)} q^{\\#T(\omega_{n+1} \dots \omega_N)} X(\omega_1 \dots \omega_n \omega_{n+1} \dots \omega_N) \quad \text{(2.3.6)}
   ```

   $$\tilde{\mathbb{E}}_0[X] = \tilde{\mathbb{E}}X \quad \text{(2.3.7)}$$

   $$\tilde{\mathbb{E}}_N[X] = X \quad \text{(2.3.8)}$$

4. **Assumptions and domain of validity**

   * **Random Variables:** $X$ and $Y$ must be random variables depending on the first $N$ tosses of a coin.
   * **Time Horizon:** The conditional expectation index $n$ must lie in the range $0 \le n \le N$.
   * **Probability Measure Constraints:** The actual probabilities $p, q$ (or risk-neutral probabilities $\tilde{p}, \tilde{q}$) must satisfy $0 < p < 1$, $0 < q < 1$, and $p+q=1$ (or $\tilde{p}+\tilde{q}=1$). If a transition probability is zero or outside this range, the expectation no longer represents a valid probability-weighted average.
   * **Conditional Jensen's Inequality (Theorem 2.3.2 (v)):** The function $\varphi(x)$ must be a **convex** function defined over the domain of $X$. If $\varphi(x)$ is concave, the inequality reverses strictly to $\mathbb{E}_n[\varphi(X)] \le \varphi(\mathbb{E}_n[X])$.

5. **Theorems and proof outline**

   **Theorem 2.3.2 (Fundamental properties of conditional expectations):** Let $N$ be a positive integer, and let $X$ and $Y$ be random variables depending on the first $N$ coin tosses. Let $0 \le n \le N$ be given. The following properties hold under both the actual probabilities ($\mathbb{E}_n$) and risk-neutral probabilities ($\tilde{\mathbb{E}}_n$):

   1. **Linearity of conditional expectations:** For all constants $c_1$ and $c_2$, $\mathbb{E}_n[c_1 X + c_2 Y] = c_1 \mathbb{E}_n[X] + c_2 \mathbb{E}_n[Y]$.
   2. **Taking out what is known:** If $X$ actually depends only on the first $n$ coin tosses, then $\mathbb{E}_n[XY] = X \cdot \mathbb{E}_n[Y]$.
   3. **Iterated conditioning:** If $0 \le n \le m \le N$, then $\mathbb{E}_n[\mathbb{E}_m[X]] = \mathbb{E}_n[X]$. In particular, $\mathbb{E}[\mathbb{E}_m[X]] = \mathbb{E}[X]$.
   4. **Independence:** If $X$ depends only on tosses $n+1$ through $N$, then $\mathbb{E}_n[X] = \mathbb{E}X$.
   5. **Conditional Jensen's inequality:** If $\varphi(x)$ is a convex function of the dummy variable $x$, then $\mathbb{E}_n[\varphi(X)] \ge \varphi(\mathbb{E}_n[X])$.

   *Proof outline (Deferring formal calculations to the Appendix, as stated in the book):*
   1. **Proof of (i) Linearity:** Expressing $\mathbb{E}_n[c_1 X + c_2 Y]$ as a summation over the remaining coin tosses $\omega_{n+1} \dots \omega_N$ under Definition 2.3.1 allows the summation to be split into two parts due to algebraic linearity of sums. The constants $c_1$ and $c_2$ factor outside their respective sums (Illustrated in Example 2.3.3).
   2. **Proof of (ii) Taking out what is known:** Since $X$ depends only on the first $n$ tosses, for any fixed sequence $\omega_1 \dots \omega_n$, the term $X(\omega_1 \dots \omega_n)$ is constant relative to the summation over future outcomes $\omega_{n+1} \dots \omega_N$ and factors out of the sum (Illustrated in Example 2.3.4).
   3. **Proof of (iii) Iterated conditioning:** Let $Z = \mathbb{E}_m[X]$. Since $n \le m$, $\mathbb{E}_n[Z]$ sums over tosses $n+1$ through $m$. Substituting the definition of $Z$ (which sums over tosses $m+1$ through $N$) yields a double summation over all tosses from $n+1$ through $N$, collapsing into the single-stage sum $\mathbb{E}_n[X]$ (Illustrated in Example 2.3.5).
   4. **Proof of (iv) Independence:** Since $X$ only depends on tosses $n+1$ through $N$, the sequence values do not depend on the first $n$ tosses. The summation over $\omega_{n+1} \dots \omega_N$ with joint transition probabilities is mathematically identical to the unconditional expectation sum $\mathbb{E}X$ (Illustrated in Example 2.3.6).
   5. **Proof of (v) Conditional Jensen's inequality:** Characterize the convex function $\varphi$ as the upper envelope of all linear support lines $\ell(y) = ay+b$ below it. For any such line, $\mathbb{E}_n[\varphi(X)] \ge \mathbb{E}_n[\ell(X)] = \ell(\mathbb{E}_n[X])$ by linearity. Taking the supremum over all such support lines at $y = \mathbb{E}_n[X]$ yields $\varphi(\mathbb{E}_n[X])$.

6. **Exercises in this section**

   **There are no exercises in Section 2.8 of the book that are specific and exclusive to Section 2.3.**

   Instead, the fundamental properties of conditional expectations established in Theorem 2.3.2 are treated as essential mathematical tools used to solve subsequent exercises throughout Chapter 2, such as:
   * Proving symmetric random walk martingales in **Exercise 2.4**.
   * Verifying Markov properties of stochastic integrals in **Exercise 2.5**.
   * Proving discrete-time stochastic integrals in **Exercise 2.6**.
   * Proving put-call parity relations in **Exercise 2.11**.

7. **Cross-references**

   * **Chapter 1 (Sections 1.1, 1.2):** The multiperiod stock price tree and parameters $u,d,r$ supply the primary random variables analyzed here.
   * **Section 2.1 & 2.2:** Introduces finite probability spaces and defines the unconditional expectation operator $\mathbb{E}X$.
   * **Section 2.4:** Direct application of Theorem 2.3.2 to define and analyze martingales, submartingales, and supermartingales.
   * **Section 2.5:** Introduces Markov processes and defines the Independence Lemma (Lemma 2.5.3) as a generalization of the "taking out what is known" property.
   * **Section 3.2:** Employs iterated conditioning and taking out what is known to establish properties of the Radon-Nikodym derivative process $Z_n$.
   * **Section 6.2:** Generalizes Definition 2.3.1 to non-independent coin tosses (Definition 6.2.2) and verifies that all properties of Theorem 2.3.2 still hold.