## 1. Concept and context

In multiperiod financial models we work under two distinct probability measures on the same finite sample space $\Omega$: the actual (physical) measure $\mathbb{P}$, estimated empirically and dictating real-world frequencies, and the risk-neutral measure $\tilde{\mathbb{P}}$, under which discounted asset prices are martingales. These two measures agree on which paths are possible (i.e., they are equivalent), but assign different positive weights to individual paths. The Radon-Nikodym derivative is the algebraic multiplier that converts an expectation computed under one measure into an expectation computed under the other, without ever having to solve the replication equations of Chapter 1 again (Section 3.1, pp. 61-64).

## 2. Formal definitions

* **$\mathbb{P}$, $\tilde{\mathbb{P}}$**: The actual and risk-neutral probability measures on the finite sample space $\Omega$ of coin-toss sequences, both assumed to assign strictly positive probability to every path $\omega \in \Omega$.
* **$Z(\omega)$**: The Radon-Nikodym derivative of $\tilde{\mathbb{P}}$ with respect to $\mathbb{P}$; the strictly positive random variable equal to the quotient of the two measures at each outcome $\omega$.
* **$\zeta(\omega)$**: The state price density; the Radon-Nikodym derivative $Z(\omega)$ discounted by the money market account over the full $N$ periods of the model.
* **State price**: the product $\zeta(\omega)\mathbb{P}(\omega)$, the time-zero no-arbitrage price of a contract that pays $1$ at time $N$ if and only if the sequence $\omega$ occurs, and $0$ otherwise.

## 3. Key equations

$$Z(\omega) = \frac{\tilde{\mathbb{P}}(\omega)}{\mathbb{P}(\omega)} \quad \text{(3.1.1)}$$

$$\tilde{\mathbb{E}}[Y] = \mathbb{E}[ZY] \quad \text{(3.1.2)}$$

$$\mathbb{P}(HHH)=\frac{8}{27},\ \mathbb{P}(HHT)=\frac{4}{27},\ \mathbb{P}(HTH)=\frac{4}{27},\ \mathbb{P}(HTT)=\frac{2}{27},$$

$$\mathbb{P}(THH)=\frac{4}{27},\ \mathbb{P}(THT)=\frac{2}{27},\ \mathbb{P}(TTH)=\frac{2}{27},\ \mathbb{P}(TTT)=\frac{1}{27} \quad \text{(3.1.3)}$$

$$\tilde{\mathbb{P}}(\omega) = \frac{1}{8} \text{ for every } \omega \in \Omega \quad \text{(3.1.4)}$$

$$Z(HHH)=\frac{27}{64},\ Z(HHT)=\frac{27}{32},\ Z(HTH)=\frac{27}{32},\ Z(HTT)=\frac{27}{16},$$

$$Z(THH)=\frac{27}{32},\ Z(THT)=\frac{27}{16},\ Z(TTH)=\frac{27}{16},\ Z(TTT)=\frac{27}{8} \quad \text{(3.1.5)}$$

$$V_0 = \tilde{\mathbb{E}}\left[\frac{V_3}{(1+r)^3}\right] = \left(\frac{4}{5}\right)^3\sum_{\omega\in\Omega}V_3(\omega)\tilde{\mathbb{P}}(\omega) \quad \text{(3.1.6)}$$

$$V_0 = \mathbb{E}\left[\frac{V_3 Z}{(1+r)^3}\right] = \left(\frac{4}{5}\right)^3\sum_{\omega\in\Omega}V_3(\omega)Z(\omega)\mathbb{P}(\omega) \quad \text{(3.1.7)}$$

$$Z(\omega_1\dots\omega_N) = \frac{\tilde{\mathbb{P}}(\omega_1\dots\omega_N)}{\mathbb{P}(\omega_1\dots\omega_N)} = \left(\frac{\tilde{p}}{p}\right)^{\#H(\omega_1\dots\omega_N)}\left(\frac{\tilde{q}}{q}\right)^{\#T(\omega_1\dots\omega_N)} \quad \text{(3.1.8)}$$

$$\zeta(\omega) = \frac{Z(\omega)}{(1+r)^N} \quad \text{(3.1.9)}$$

$$V_0 = \mathbb{E}[\zeta V_N] = \sum_{\omega\in\Omega}V_N(\omega)\zeta(\omega)\mathbb{P}(\omega) \quad \text{(3.1.10)}$$

## 4. Assumptions and domain of validity

* **Equivalence of measures:** Both $\mathbb{P}$ and $\tilde{\mathbb{P}}$ must assign strictly positive probability to every path $\omega \in \Omega$. If $\mathbb{P}(\omega)=0$ for some $\omega$, the quotient in (3.1.1) is undefined. In finance models, the actual and risk-neutral measures must always be equivalent — they agree about what is possible and what is impossible.
* **Finiteness of $\Omega$:** Theorem 3.1.1 is stated for a finite sample space. For infinite (continuous-time) sample spaces, the Radon-Nikodym derivative can no longer be expressed as a simple pointwise quotient and requires the general Radon-Nikodym theorem from measure theory (Volume II).
* **Positivity of $(1+r)$:** For $\zeta(\omega)$ in (3.1.9) to be well-defined and strictly positive, $(1+r)^N$ must be strictly positive. This is not a new hypothesis of this section — it is already guaranteed by the standing no-arbitrage condition $0<d<1+r<u$ inherited from Section 1.1.

## 5. Theorems and proof outline

**Theorem 3.1.1 (Properties of the Radon-Nikodym derivative):** Let $\mathbb{P}$ and $\tilde{\mathbb{P}}$ be probability measures on a finite sample space $\Omega$, assume $\mathbb{P}(\omega)>0$ and $\tilde{\mathbb{P}}(\omega)>0$ for every $\omega \in \Omega$, and define $Z$ by (3.1.1). Then:
(i) $\mathbb{P}(Z>0)=1$;
(ii) $\mathbb{E}Z=1$;
(iii) for any random variable $Y$, $\tilde{\mathbb{E}}[Y] = \mathbb{E}[ZY]$.

*Proof outline:*

1. **Property (i):** Since $\tilde{\mathbb{P}}(\omega)>0$ and $\mathbb{P}(\omega)>0$ for every $\omega$, the quotient $Z(\omega)$ is strictly positive for every $\omega$, so $\mathbb{P}(Z>0)=\mathbb{P}(\Omega)=1$.
2. **Property (ii):** Write $\mathbb{E}Z = \sum_{\omega\in\Omega} Z(\omega)\mathbb{P}(\omega)$.
3. Substitute $Z(\omega)=\tilde{\mathbb{P}}(\omega)/\mathbb{P}(\omega)$, cancelling $\mathbb{P}(\omega)$: $\mathbb{E}Z = \sum_{\omega\in\Omega}\tilde{\mathbb{P}}(\omega)$.
4. Since $\tilde{\mathbb{P}}$ is a probability measure, this sum equals $1$.
5. **Property (iii):** Write $\tilde{\mathbb{E}}Y = \sum_{\omega\in\Omega}Y(\omega)\tilde{\mathbb{P}}(\omega)$, then multiply and divide each term by $\mathbb{P}(\omega)$ to get $\sum_{\omega\in\Omega}Y(\omega)Z(\omega)\mathbb{P}(\omega) = \mathbb{E}[ZY]$.

## 6. Exercises in this section (and required examples)

* **Example 3.1.2:** In the three-period model of Example 1.2.4 ($S_0=4$, $u=2$, $d=1/2$, $r=1/4$), take $p=2/3$, $q=1/3$ as the actual probabilities, giving the actual measure (3.1.3). With $\tilde{p}=\tilde{q}=1/2$, the risk-neutral measure is $\tilde{\mathbb{P}}(\omega)=1/8$ for every $\omega$ (3.1.4), and the resulting Radon-Nikodym derivative values are given by (3.1.5). Recomputing the time-zero price of the lookback option of Example 1.2.4 ($V_3(HHH)=0$, $V_3(HHT)=8$, $V_3(HTH)=0$, $V_3(HTT)=6$, $V_3(THH)=0$, $V_3(THT)=2$, $V_3(TTH)=2$, $V_3(TTT)=3.50$) via the risk-neutral formula (3.1.6) and via the actual measure weighted by $Z$ (3.1.7) both give $V_0=1.376$ — the same value found in Example 1.2.4 of Chapter 1. This demonstrates that pricing can be done entirely under the actual probability measure, as long as payoffs are weighted by the Radon-Nikodym derivative.
* **Exercise 3.1:** Under the conditions of Theorem 3.1.1, show the following analogues of properties (i)-(iii) of that theorem:
  (i') $\tilde{\mathbb{P}}(1/Z>0)=1$;
  (ii') $\tilde{\mathbb{E}}[1/Z]=1$;
  (iii') for any random variable $Y$, $\mathbb{E}Y = \tilde{\mathbb{E}}[(1/Z)Y]$.
  In other words, $1/Z$ facilitates the switch from $\tilde{\mathbb{E}}$ back to $\mathbb{E}$, in the same way $Z$ facilitates the switch from $\mathbb{E}$ to $\tilde{\mathbb{E}}$.
* **Exercise 3.2:** Let $\mathbb{P}$ be a probability measure on a finite probability space $\Omega$, allowing the possibility that $\mathbb{P}(\omega)=0$ for some $\omega \in \Omega$. Let $Z$ be a random variable on $\Omega$ with $\mathbb{P}(Z\ge0)=1$ and $\mathbb{E}Z=1$. For $\omega\in\Omega$, define $\tilde{\mathbb{P}}(\omega)=Z(\omega)\mathbb{P}(\omega)$, and for events $A\subseteq\Omega$, define $\tilde{\mathbb{P}}(A)=\sum_{\omega\in A}\tilde{\mathbb{P}}(\omega)$. Show the following:
  (i) $\tilde{\mathbb{P}}$ is a probability measure; i.e., $\tilde{\mathbb{P}}(\Omega)=1$.
  (ii) If $Y$ is a random variable, then $\tilde{\mathbb{E}}Y = \mathbb{E}[ZY]$.
  (iii) If $A$ is an event with $\mathbb{P}(A)=0$, then $\tilde{\mathbb{P}}(A)=0$.
  (iv) Assume $\mathbb{P}(Z>0)=1$. Show that if $A$ is an event with $\tilde{\mathbb{P}}(A)=0$, then $\mathbb{P}(A)=0$.
  (When two measures agree on which events have probability zero, they are said to be equivalent. From (iii) and (iv), $\mathbb{P}$ and $\tilde{\mathbb{P}}$ are equivalent under the assumption $\mathbb{P}(Z>0)=1$.)
  (v) Show that if $\mathbb{P}$ and $\tilde{\mathbb{P}}$ are equivalent, then they agree on which events have probability one.
  (vi) Construct an example in which we have only $\mathbb{P}(Z\ge0)=1$ and $\mathbb{P}$ and $\tilde{\mathbb{P}}$ are not equivalent.
* **Exercise 3.4 (parts (i)-(ii) only):** This problem refers to the model of Example 3.1.2.
  (i) Compute the state price densities $\zeta(HHH)$, $\zeta(HHT)=\zeta(HTH)=\zeta(THH)$, $\zeta(HTT)=\zeta(THT)=\zeta(TTH)$, and $\zeta(TTT)$ explicitly using (3.1.9).
  (ii) Use these values in formula (3.1.10) to find the time-zero price of the Asian option of Exercise 1.8 of Chapter 1. You should get $v_0(4,4)$ computed in part (ii) of that exercise.
  (Parts (iii)-(iv) of this same exercise use the Radon-Nikodym derivative *process* $Z_n$ and Theorem 3.2.7, and are covered in the Section 3.2 card.)

## 7. Cross-references

* **Example 1.2.4 (Chapter 1, p. 14):** Source of the payoffs and the benchmark price $V_0=1.376$ for the three-period lookback option used in Example 3.1.2.
* **Exercise 1.8 (Chapter 1, p. 22):** Formulates the three-period Asian call option priced via state price densities in Exercise 3.4(i)-(ii).
* **Theorem 1.2.2 (Chapter 1, p. 11):** The multiperiod backward replication algorithm, verified here to give the same $V_0$ as the change-of-measure formulas (3.1.6)-(3.1.7).
* **Section 3.2:** Extends the static Radon-Nikodym derivative $Z$ to the dynamic, adapted Radon-Nikodym derivative process $Z_n = \mathbb{E}_n[Z]$.
* **Section 3.3:** Uses the state price density $\zeta(\omega)$ as the budget-constraint multiplier in the utility maximization problem.