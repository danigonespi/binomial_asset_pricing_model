1. **Concept and context**

   Sections 2.1 and 2.2 construct the discrete-time probability space that underpins the entire multiperiod binomial model. Section 2.1 formalizes the notion of coin-toss space and path probabilities by defining finite probability spaces and events (Section 2.1, p. 25). Section 2.2 introduces random variables as real-valued functions on these spaces, along with their distributions and expectations, culminating in Jensen's inequality, which governs how convex functions behave under the expectation operator (Section 2.2, p. 27).

2. **Formal definitions**

   * $\Omega$: Sample space — a nonempty finite set whose elements $\omega$ represent the possible outcomes of the coin-tossing experiment.
   * $\mathbb{P}$: Probability measure — a function assigning to each $\omega \in \Omega$ a number in $[0,1]$ such that the probabilities of all outcomes sum to $1$ (Definition 2.1.1, p. 26).
   * $A$: An event — any subset of $\Omega$.
   * $X$: A random variable — a real-valued function defined on $\Omega$ (sometimes also permitted to take the values $+\infty$ and $-\infty$) (Definition 2.2.1, p. 27).
   * Distribution of $X$: the specification of the probabilities that $X$ takes each of its possible values, denoted $\mathbb{P}\{X=j\}$ (p. 28–29; described conceptually, not a separately numbered definition).
   * $\mathbb{E}X$: Expectation of $X$ (Definition 2.2.4, p. 29). When computed under the risk-neutral measure $\tilde{\mathbb{P}}$, denoted $\tilde{\mathbb{E}}X$.
   * $\text{Var}(X)$: Variance of $X$ (p. 29–30).

3. **Key equations**

$$
\Omega = \{HHH, HHT, HTH, HTT, THH, THT, TTH, TTT\} \quad \text{(2.1.1)}
$$

$$
\mathbb{P}(HHH)=p^3,\ \mathbb{P}(HHT)=p^2q,\ \mathbb{P}(HTH)=p^2q,\ \mathbb{P}(HTT)=pq^2,
$$

$$
\mathbb{P}(THH)=p^2q,\ \mathbb{P}(THT)=pq^2,\ \mathbb{P}(TTH)=pq^2,\ \mathbb{P}(TTT)=q^3 \quad \text{(2.1.2)}
$$

$$
\mathbb{P}(\omega_1 = H) = p \quad \text{(2.1.3)}
$$

$$
\sum_{\omega \in \Omega} \mathbb{P}(\omega) = 1 \quad \text{(2.1.4)}
$$

$$
\mathbb{P}(A) = \sum_{\omega \in A} \mathbb{P}(\omega) \quad \text{(2.1.5)}
$$

$$
\mathbb{P}(\Omega) = 1 \quad \text{(2.1.6)}
$$

$$
\mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B), \quad A \cap B = \emptyset \quad \text{(2.1.7)}
$$

$$
\mathbb{E}X = \sum_{\omega \in \Omega} X(\omega)\mathbb{P}(\omega) \quad \text{(Definition 2.2.4)}
$$

$$
\varphi(x) = \max\{\ell(x);\ \ell \text{ linear},\ \ell(y) \le \varphi(y)\ \forall y \in \mathbb{R}\} \quad \text{(2.2.1)}
$$


4. **Assumptions and domain of validity**

   * **Finiteness of $\Omega$:** $\Omega$ must be finite and nonempty. For infinite (continuous-time) sample spaces, probabilities can no longer be defined by summing over individual $\omega$; this requires $\sigma$-algebras and Lebesgue integration, treated in Volume II.
   * **$\mathbb{P}$ well-defined:** requires $0 \le \mathbb{P}(\omega) \le 1$ for every $\omega$ and $\sum_\omega \mathbb{P}(\omega)=1$ (Eq. 2.1.4). Outcomes with $\mathbb{P}(\omega)=0$ are explicitly permitted.
   * **Jensen's inequality (Theorem 2.2.5):** requires $X$ defined on a finite probability space and $\varphi$ convex. If $\varphi$ is instead strictly concave, the inequality reverses: $\mathbb{E}[\varphi(X)] \le \varphi(\mathbb{E}X)$.

5. **Theorems and proof outline**

   **Theorem 2.2.5 (Jensen's inequality):** Let $X$ be a random variable on a finite probability space and $\varphi$ a convex function. Then $\mathbb{E}[\varphi(X)] \ge \varphi(\mathbb{E}X)$.

   *Proof outline:*
   1. A convex function equals the maximum of all linear functions lying below it (Eq. 2.2.1).
   2. For any point $x$, convexity guarantees a "support line" $\ell$ with $\ell(x)=\varphi(x)$ and $\ell(y)\le\varphi(y)$ for all $y$.
   3. For any such $\ell$, $\ell(X(\omega)) \le \varphi(X(\omega))$ for every $\omega$; taking expectations preserves the inequality: $\mathbb{E}[\varphi(X)] \ge \mathbb{E}[\ell(X)]$.
   4. By linearity of expectation, $\mathbb{E}[\ell(X)] = \ell(\mathbb{E}X)$.
   5. Since this holds for every such $\ell$, it holds for the maximum over all of them evaluated at $\mathbb{E}X$, which equals $\varphi(\mathbb{E}X)$ by step 1.

6. **Exercises in this section**

   * **Exercise 2.1:** Using Definition 2.1.1, show (i) $\mathbb{P}(A^c) = 1-\mathbb{P}(A)$ for an event $A$ with complement $A^c$; (ii) for a finite set of events $A_1,\dots,A_N$, $\mathbb{P}(\bigcup_{n=1}^N A_n) \le \sum_{n=1}^N \mathbb{P}(A_n)$ (Eq. 2.8.1), with equality when the events are disjoint.
   * **Exercise 2.2:** Consider the stock price $S_3$ of Figure 2.3.1. (i) Give the distribution of $S_3$ under the risk-neutral probabilities $p=\tilde p=\frac12,\ q=\tilde q=\frac12$. (ii) Compute $\mathbb{E}S_1,\mathbb{E}S_2,\mathbb{E}S_3$ and the average growth rate of the stock under $\tilde{\mathbb{P}}$. (iii) Repeat (i) and (ii) under the actual probabilities $p=\frac23,\ q=\frac13$.

7. **Cross-references**

   * **Chapter 1 (Sections 1.1, 1.2):** the multiperiod stock price tree and parameters $u,d,r$ supply the primary random variables analyzed here.
   * **Section 2.3:** the expectation $\mathbb{E}X$ is extended to conditional expectation $\mathbb{E}_n[X]$; this is also where the general $p^{\\#H}q^{\\#T}$ notation is actually introduced.
   * **Theorem 2.3.2(v):** Jensen's inequality (2.2.5) is the conceptual template for the Conditional Jensen's inequality.
   * **Section 2.7 / Volume II, Chapters 1–2:** the finite-$\Omega$ framework is linked to Kolmogorov's axiomatization needed for continuous-time models.
