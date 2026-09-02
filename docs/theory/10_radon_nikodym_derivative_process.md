## 1. Concept and context

While the Radon-Nikodym derivative $Z$ allows a static change of measure over the entire life of the model, we often need to update our probability estimates dynamically as new coin tosses are observed. The Radon-Nikodym derivative process $Z_n$ is defined by estimating $Z$ via conditional expectation under the actual probability measure based on the information available at time $n$. This process is a martingale under the actual measure, starting at $1$ and ending at $Z$ at maturity. Acting as a dynamic density multiplier, $Z_n$ converts both unconditional and conditional expectations between the actual and risk-neutral measures over any intermediate period, providing the mathematical foundation for multiperiod risk-neutral pricing via state price densities (Section 3.2, pp. 65-69).

## 2. Formal definitions

* **Radon-Nikodym Derivative Process ($Z_n$):** For an $N$-period binomial model with actual measure $\mathbb{P}$ and risk-neutral measure $\tilde{\mathbb{P}}$ (both assigning strictly positive probability to every path), the adapted stochastic process defined as the conditional expectation of $Z$ at time $n$ under the actual probability measure (Definition 3.2.4, p. 67).
* **State Price Density Process ($\zeta_n$):** The Radon-Nikodym derivative process discounted at the risk-free rate, representing the time-zero cost per unit of actual probability for a security paying out at time $n$ (Theorem 3.2.7, p. 69).
* **Prefix Ratio ($Z_n(\omega_1 \dots \omega_n)$):** The ratio of the risk-neutral probability of obtaining the sequence of first $n$ coin tosses to the actual probability of obtaining that same sequence (p. 69).

## 3. Key equations

$$Z_n = \mathbb{E}_n[Z], \quad n = 0, 1, \dots, N \quad \text{(3.2.1)}$$

$$Z_n = \mathbb{E}_n[Z], \quad n = 0, 1, \dots, N \quad \text{(3.2.2)}$$
*(restated in Definition 3.2.4, where $Z_N = Z$ and $Z_0 = 1$)*

$$\tilde{\mathbb{E}}[Y] = \mathbb{E}[Z_n Y] \quad \text{(3.2.3)}$$
*(for any random variable $Y$ depending only on the first $n$ tosses)*

$$Z_n(\omega_1 \dots \omega_n) = \left(\frac{\tilde{p}}{p}\right)^{\#H(\omega_1\dots\omega_n)} \left(\frac{\tilde{q}}{q}\right)^{\#T(\omega_1\dots\omega_n)} \quad \text{(3.2.4)}$$

$$\tilde{\mathbb{E}}_n [Y] = \frac{1}{Z_n} \mathbb{E}_n [Z_m Y] \quad \text{(3.2.5)}$$
*(for $n \le m$ and $Y$ depending only on the first $m$ tosses)*

$$V_n = \tilde{\mathbb{E}}_n\left[\frac{V_N}{(1+r)^{N-n}}\right] = \frac{1}{Z_n}\mathbb{E}_n\left[\frac{Z_N V_N}{(1+r)^{N-n}}\right] = \frac{1}{\zeta_n}\mathbb{E}_n[\zeta_N V_N] \quad \text{(3.2.6)}$$

$$\zeta_n = \frac{Z_n}{(1+r)^n}, \quad n = 0, 1, \dots, N \quad \text{(3.2.7)}$$

## 4. Assumptions and domain of validity

* **Strict Positivity of Paths:** $\mathbb{P}$ and $\tilde{\mathbb{P}}$ must assign strictly positive probability to all $2^N$ paths in $\Omega$. If $\mathbb{P}(\omega)=0$ or $\tilde{\mathbb{P}}(\omega)=0$ for any path, $Z(\omega)$ and $Z_n$ are undefined.
* **Information Adaptedness:** $Y$ in Lemma 3.2.5 must depend only on the first $n$ coin tosses; $Y$ in Lemma 3.2.6 must depend only on the first $m$ coin tosses. If $Y$ depends on tosses beyond those horizons, the reduction formulas do not apply.
* **Positivity of $(1+r)$:** For $\zeta_n$ in (3.2.7) to be well-defined, $(1+r)^n$ must be strictly positive for every $n$. This is not a new hypothesis of this section — it follows from the standing no-arbitrage condition $0<d<1+r<u$ inherited from Section 1.1.

## 5. Theorems and proof outline

**Theorem 3.2.1 (Martingale Property of $Z_n$):** Let $Z$ be a random variable in an $N$-period binomial model and define $Z_n=\mathbb{E}_n[Z]$ for $n=0,1,\dots,N$. Then $Z_n$ is a martingale under the actual measure $\mathbb{P}$.

*Proof outline:*

1. To verify the martingale property, show $\mathbb{E}_n[Z_{n+1}]=Z_n$ for every $n \in \{0,\dots,N-1\}$.
2. Substitute $Z_{n+1}=\mathbb{E}_{n+1}[Z]$: $\mathbb{E}_n[Z_{n+1}]=\mathbb{E}_n[\mathbb{E}_{n+1}[Z]]$.
3. Apply iterated conditioning (Theorem 2.3.2(iii)): $\mathbb{E}_n[\mathbb{E}_{n+1}[Z]]=\mathbb{E}_n[Z]$.
4. Recognize the result as the definition of $Z_n$, proving $Z_n=\mathbb{E}_n[Z_{n+1}]$.


**Remark 3.2.2 (Symmetric Martingale Property under $\tilde{\mathbb{P}}$):**

*Proof outline:*

1. If $Z'_n = \tilde{\mathbb{E}}_n[Z']$ is defined for any random variable $Z'$ under the risk-neutral measure $\tilde{\mathbb{P}}$, the identical iterated-conditioning argument applies under $\tilde{\mathbb{P}}$.
2. Therefore, risk-neutral conditional expectations of any terminal random variable form a martingale under $\tilde{\mathbb{P}}$.


**Example 3.2.3 (Radon-Nikodym Process in the Three-Period Model):** Recomputes the $Z_n$ process for the three-period model of Example 3.1.2 (Figure 3.2.1), where $p=2/3$, $q=1/3$, $\tilde{p}=\tilde{q}=1/2$, $r=1/4$.

*Proof outline:*

1. **Terminal values:** $Z_3(\omega)=Z(\omega)$ for all 8 paths, from (3.1.5).
2. **$Z_2$:** e.g. $Z_2(HH)=pZ_3(HHH)+qZ_3(HHT)=\frac{2}{3}\cdot\frac{27}{64}+\frac{1}{3}\cdot\frac{27}{32}=\frac{9}{16}$. Similarly $Z_2(HT)=Z_2(TH)=\frac{9}{8}$ and $Z_2(TT)=\frac{9}{4}$.
3. **$Z_1$:** $Z_1(H)=pZ_2(HH)+qZ_2(HT)=\frac{2}{3}\cdot\frac{9}{16}+\frac{1}{3}\cdot\frac{9}{8}=\frac{3}{4}$; $Z_1(T)=\frac{2}{3}\cdot\frac{9}{8}+\frac{1}{3}\cdot\frac{9}{4}=\frac{3}{2}$.
4. **$Z_0$:** $Z_0=pZ_1(H)+qZ_1(T)=\frac{2}{3}\cdot\frac{3}{4}+\frac{1}{3}\cdot\frac{3}{2}=1$, matching $\mathbb{E}Z=1$ from Theorem 3.1.1(ii).


**Lemma 3.2.5 (Expectation under Change of Measure over Short Horizons):** For $Y$ depending only on the first $n$ coin tosses, $\tilde{\mathbb{E}}[Y]=\mathbb{E}[Z_nY]$ (3.2.3).

*Proof outline:*

1. By Theorem 3.1.1(iii), $\tilde{\mathbb{E}}[Y]=\mathbb{E}[ZY]$.
2. Condition on time-$n$ information: $\mathbb{E}[ZY]=\mathbb{E}[\mathbb{E}_n[ZY]]$.
3. Since $Y$ is known at time $n$, apply "taking out what is known" (Theorem 2.3.2(ii)): $\mathbb{E}[\mathbb{E}_n[ZY]]=\mathbb{E}[Y\mathbb{E}_n[Z]]$.
4. Substitute $\mathbb{E}_n[Z]=Z_n$: $\mathbb{E}[Y\mathbb{E}_n[Z]]=\mathbb{E}[YZ_n]$.


**Lemma 3.2.6 (Conditional Change of Measure):** For $n\le m$ and $Y$ depending only on the first $m$ coin tosses, $\tilde{\mathbb{E}}_n[Y]=\frac{1}{Z_n}\mathbb{E}_n[Z_mY]$ (3.2.5).

*Proof outline:*

1. Write $\tilde{\mathbb{E}}_n[Y](\omega_1\dots\omega_n)$ as a sum over the future tosses $\omega_{n+1}\dots\omega_m$ weighted by $\tilde{p}^{\#H}\tilde{q}^{\#T}$.
2. Multiply and divide inside the sum by the actual transition probabilities $p^{\#H}q^{\#T}$.
3. Rewrite the resulting ratio $(\tilde{p}/p)^{\#H}(\tilde{q}/q)^{\#T}$ (over tosses $n{+}1$ to $m$) as $Z_m(\omega_1\dots\omega_m)/Z_n(\omega_1\dots\omega_n)$, consistent with (3.2.4).
4. Factor out $Z_n(\omega_1\dots\omega_n)$, known at time $n$.
5. Recognize the remaining sum as $\mathbb{E}_n[Z_mY]$, yielding $\tilde{\mathbb{E}}_n[Y]=\frac{1}{Z_n}\mathbb{E}_n[Z_mY]$.


**Theorem 3.2.7 (Risk-Neutral Pricing via State Price Densities):** For a derivative payoff $V_N$ depending on the first $N$ coin tosses, and $n=0,1,\dots,N$, the price at time $n$ is given by the equality chain (3.2.6), with $\zeta_n$ defined by (3.2.7).

*Proof outline:*

1. The first equality in (3.2.6) is the risk-neutral pricing formula (2.4.11) of Chapter 2.
2. The second equality follows from applying Lemma 3.2.6 with $m=N$ and $Y=V_N/(1+r)^{N-n}$.
3. Regroup the discount factors and $Z_N/Z_n$ terms.
4. The third equality is simply the definition of $\zeta_n=Z_n/(1+r)^n$ and $\zeta_N=Z_N/(1+r)^N$.

## 6. Exercises in this section (and required examples)

* **Exercise 3.3 (p. 84):** Using the stock price model of Figure 3.1.1 and the actual probabilities $p=2/3$, $q=1/3$, define the estimates of $S_3$ at various times by $M_n=\mathbb{E}_n[S_3]$, $n=0,1,2,3$. Fill in the values of $M_n$ in a tree like that of Figure 3.1.1. Verify that $M_n$, $n=0,1,2,3$, is a martingale under the actual measure $\mathbb{P}$.
* **Exercise 3.4 (p. 84) (parts (iii)-(iv) only):** This problem refers to the model of Example 3.1.2, whose Radon-Nikodym process $Z_n$ appears in Figure 3.2.1. (Parts (i)-(ii), computing $\zeta_3(\omega)$ and pricing the Asian option of Exercise 1.8 via (3.1.10), are covered in the Section 3.1 card — see 09_change_of_measure.md.)
  (iii) Compute also the state price densities $\zeta_2(HT)=\zeta_2(TH)$ explicitly.
  (iv) Use the risk-neutral pricing formula (3.2.6) in the form $V_2(HT)=\frac{1}{\zeta_2(HT)}\mathbb{E}_2[\zeta_3V_3](HT)$, $V_2(TH)=\frac{1}{\zeta_2(TH)}\mathbb{E}_2[\zeta_3V_3](TH)$ to compute $V_2(HT)$ and $V_2(TH)$. You should get $V_2(HT)=v_2(4,16)$ and $V_2(TH)=v_2(4,10)$, where $v_2(s,y)$ was computed in part (ii) of Exercise 1.8 of Chapter 1. Note that $V_2(HT)\neq V_2(TH)$.

## 7. Cross-references

* **Theorem 2.3.2 (Chapter 2, p. 34):** Iterated conditioning (iii) and taking out what is known (ii) are the core justifications for Theorem 3.2.1, Lemma 3.2.5, and Lemma 3.2.6.
* **Example 3.1.2 (Chapter 3, p. 62):** Supplies the joint probabilities, risk-neutral probabilities, and parameters ($p=2/3,q=1/3,\tilde{p}=\tilde{q}=1/2,r=1/4$) used in Example 3.2.3 and Exercise 3.4.
* **Exercise 1.8 (Chapter 1, p. 22):** Defines the three-period Asian call option whose intermediate and terminal pricing is verified via state price densities in Exercise 3.4.
* **Chapter 6 (Interest-Rate-Dependent Assets):** *(Unverified — not yet audited against the Chapter 6 pages of the PDF.)* NotebookLM reports that $Z_n$ is generalized there to models with random interest rates via an $m$-forward measure construction (cited as Section 6.4, Eq. 6.4.3, p. 160). Treat these specific numbers as unconfirmed until Chapter 6 is audited.