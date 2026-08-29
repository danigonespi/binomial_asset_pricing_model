## 1. Concept and context

The Markov property in discrete-time finance asserts that the conditional expectation of any future function of a stochastic process depends only on its current state, rendering its historical path irrelevant for forecasting. In Section 2.5 (pp. 45–52), Shreve formalizes this property to transition derivative pricing from path-dependent random variables to deterministic functions of state variables. This framework reduces the exponential complexity of backward pricing algorithms on binomial trees (which grows as $O(2^N)$) to a polynomial scale (growing as $O(N^2)$) by eliminating the need to store historical trajectory details.

## 2. Formal definitions

Below are the mathematical objects introduced in this section, using the exact notation of the book:

* **One-Dimensional Markov Process (Definition 2.5.1, p. 45):** Let $X_0, X_1, \dots, X_N$ be an adapted process on a binomial asset-pricing model. If, for every $n$ between $0$ and $N-1$ and for every function $f(x)$, there is another function $g(x)$ (depending on $n$ and $f$) such that:

$$\mathbb{E}_n[f(X_{n+1})] = g(X_n)$$

we say that $X_0, X_1, \dots, X_N$ is a Markov process.

* **Running Maximum Process (Example 2.5.4, p. 48):** The adapted process $M_0, M_1, \dots, M_N$ representing the maximum stock price achieved up to date $n$, defined as:

$$M_n = \max_{0 \le k \le n} S_k$$

* **$K$-Dimensional Markov Process (Definition 2.5.5, p. 49):** Let $\{(X_n^1, \dots, X_n^K); n = 0, 1, \dots, N\}$ be a $K$-dimensional adapted process (i.e., $K$ one-dimensional adapted processes). If, for every $n$ between $0$ and $N-1$ and for every function $f(x_1, \dots, x_K)$, there is another function $g(x_1, \dots, x_K)$ (depending on $n$ and $f$) such that:

$$\mathbb{E}_n[f(X_{n+1}^1, \dots, X_{n+1}^K)] = g(X_n^1, \dots, X_n^K)$$

we say that $\{(X_n^1, \dots, X_n^K); n = 0, 1, \dots, N\}$ is a $K$-dimensional Markov process.

* **State-Variable Pricing Functions (Theorem 2.5.8, p. 52):** Deterministic functions $v_n(x)$ such that $V_n = v_n(X_n)$, where $X_n$ is the underlying Markov process and $V_n$ is the option price at time $n$.

## 3. Key equations

$$\mathbb{E}_n[f(X_{n+1})] = g(X_n) \quad \text{(2.5.1)}$$

$$v_n(s) = \frac{1}{1+r} \left[\tilde{p}v_{n+1}(us)+\tilde{q}v_{n+1}(ds)\right], \quad n = N-1, N-2 , \dots,0 \quad \text{(2.5.2)}$$

$$g(x_1, \dots, x_K) = \mathbb{E} f(x_1, \dots, x_K, Y_1, \dots, Y_L) \quad \text{(2.5.3)}$$

$$\mathbb{E}_n [ f(X_1, \dots, X_K, Y_1, \dots, Y_L) ] = g(X_1, \dots, X_K) \quad \text{(2.5.4)}$$

$$\mathbb{E}_n[f(X_{n+1}^1, \dots, X_{n+1}^K)] = g(X_n^1, \dots, X_n^K) \quad \text{(2.5.5)}$$

$$\mathbb{E}_n[h(X_m)] = g(X_n) \quad \text{(2.5.6)}$$

$$\mathbb{E}_n[h(X_m^1, \dots, X_m^K)] = g(X_n^1, \dots, X_n^K) \quad \text{(2.5.7)}$$

$$v_n(s, m) = \frac{1}{1+r} \mathbb{E}_n \left[ v_{n+1}\left(s \frac{S_{n+1}}{S_n}, m \vee \left(s \frac{S_{n+1}}{S_n}\right)\right) \right] \quad \text{(2.5.8)}$$

$$v_n(s, m) = \frac{1}{1+r} [ \tilde{p} v_{n+1}(u s, m \vee (u s)) + \tilde{q} v_{n+1}(d s, m) ] \quad \text{(2.5.9)}$$

$$V_n = v_n(X_n), \quad n = 0, 1, \dots, N \quad \text{(2.5.10)}$$

## 4. Assumptions and domain of validity

* **Independence of Coin Tosses:** The underlying binomial model assumes coin tosses are independent and identically distributed. If the coin tosses are not independent, processes like the stock price $S_n$ are no longer Markov unless the state space is expanded to include history.
* **Support of Measures:** Every path in $\Omega$ must have strictly positive probability under the probability measure (p. 26).
* **The Running Maximum Counterexample (Example 2.5.4, p. 48):**
* *Why $M_n = \max_{0 \le k \le n} S_k$ alone is **not** Markov:*
* Consider the three-period model of Figure 2.3.1 with $S_0 = 4, u = 2, d = 0.5$, and probabilities $p = 2/3, q = 1/3$.
* Evaluate two distinct paths at time $n = 2$:
* **Path 1: $TH$**. The stock price sequence is $S_0 = 4, S_1(T) = 2, S_2(TH) = 4$.
* The maximum-to-date is $M_2(TH) = \max(4, 2, 4) = 4$.


* **Path 2: $TT$**. The stock price sequence is $S_0 = 4, S_1(T) = 2, S_2(TT) = 1$.
* The maximum-to-date is $M_2(TT) = \max(4, 2, 1) = 4$.


* Thus, we have $M_2(TH) = M_2(TT) = 4$.


* Compute the conditional expectation of $M_3$ at time $n = 2$ for both states:
* For state $TH$, the next stock price $S_3$ can be $S_3(THH) = 8$ or $S_3(THT) = 2$.
* If $H$ occurs, $M_3(THH) = \max(M_2(TH), 8) = 8$.
* If $T$ occurs, $M_3(THT) = \max(M_2(TH), 2) = 4$.
* Thus, $\mathbb{E}_2[M_3](TH) = p M_3(THH) + q M_3(THT) = \frac{2}{3}(8) + \frac{1}{3}(4) = \frac{20}{3} \approx 6.67$.


* For state $TT$, the next stock price $S_3$ can be $S_3(TTH) = 2$ or $S_3(TTT) = 0.50$.
* If $H$ occurs, $M_3(TTH) = \max(M_2(TT), 2) = 4$.
* If $T$ occurs, $M_3(TTT) = \max(M_2(TT), 0.50) = 4$.
* Thus, $\mathbb{E}_2[M_3](TT) = p M_3(TTH) + q M_3(TTT) = \frac{2}{3}(4) + \frac{1}{3}(4) = 4$.




* *Contradiction:* If $M_n$ were a Markov process, there would have to exist a function $g$ such that $\mathbb{E}_2[M_3] = g(M_2)$, forcing $\mathbb{E}_2[M_3](TH) = g(4) = \mathbb{E}_2[M_3](TT)$. Since $\frac{20}{3} \ne 4$, no such function $g$ can exist. Thus, $M_n$ is not Markov because it ignores the current stock price, which is critical for future maximum updates.



## 5. Theorems and proof outline

**Lemma 2.5.3 (Independence Lemma):** In the $N$-period binomial asset pricing model, let $n$ be an integer between $0$ and $N$. Suppose the random variables $X_1, \dots, X_K$ depend only on coin tosses $1$ through $n$ and the random variables $Y_1, \dots, Y_L$ depend only on coin tosses $n+1$ through $N$. Let $f(x_1, \dots, x_K, y_1, \dots, y_L)$ be a function of dummy variables, and define:

$$g(x_1, \dots, x_K) = \mathbb{E} f(x_1, \dots, x_K, Y_1, \dots, Y_L) \quad \text{(2.5.3)}$$

Then

$$\mathbb{E}_n [ f(X_1, \dots, X_K, Y_1, \dots, Y_L) ] = g(X_1, \dots, X_K) \quad \text{(2.5.4)}$$

*Proof Outline (for the simplified case $K=L=1$):*

1. **Fix historical path:** Let $\omega_1\dots\omega_n$ be a fixed, arbitrary sequence of the first $n$ tosses.
2. **Apply Conditional Expectation definition:** Write $\mathbb{E}_n[f(X, Y)](\omega_1\dots\omega_n)$ as a sum over the future coin tosses $\omega_{n+1}\dots\omega_N$ using (2.3.6):

$$ \mathbb{E}*n[f(X,Y)](\omega_1\dots\omega_n) = \sum*{\omega_{n+1}\dots\omega_N} f(X(\omega_1\dots\omega_n), Y(\omega_{n+1}\dots\omega_N)) p^{\\#H(\omega_{n+1}\dots\omega_N)} q^{\\#T(\omega_{n+1}\dots\omega_N)} $$

3. **Treat known variables as constants:** On the right-hand side of the sum, replace the random variable $X(\omega_1\dots\omega_n)$ with the constant value $x$ because it is fully determined by the first $n$ tosses.
4. **Rewrite as unconditional expectation:** Observe that the resulting sum matches exactly the definition of the unconditional expectation $\mathbb{E}[f(x, Y)]$:

$$ g(x) = \mathbb{E}[f(x, Y)] = \sum_{\omega_{n+1}\dots\omega_N} f(x, Y(\omega_{n+1}\dots\omega_N)) p^{\\#H(\omega_{n+1}\dots\omega_N)} q^{\\#T(\omega_{n+1}\dots\omega_N)} $$

5. **Reintroduce the random variable:** Substitute the dummy variable $x$ back with $X(\omega_1\dots\omega_n)$ to conclude that $\mathbb{E}_n[f(X, Y)](\omega_1\dots\omega_n) = g(X(\omega_1\dots\omega_n))$ $\blacksquare$.

**Theorem 2.5.8 (Pricing on Markov Processes):** Let $X_0, X_1, \dots, X_N$ be a Markov process under the risk-neutral probability measure $\tilde{\mathbb{P}}$ in the binomial model. Let $V_N(x)$ be a function of the dummy variable $x$, and consider a derivative security whose payoff at time $N$ is $V_N(X_N)$. Then, for each $n$ between $0$ and $N$, the price $V_n$ of this derivative security is some function $v_n$ of $X_n$, i.e., (2.5.10) holds.

*Proof Outline:*

1. **Terminal condition:** At the maturity date $n = N$, the price of the option is by definition the payoff $V_N = V_N(X_N)$. Thus, we set $v_N(x) = V_N(x)$, which verifies the base case of backward induction.
2. **Risk-neutral pricing relation:** Assume by induction that the pricing function holds for $n+1$, i.e., $V_{n+1} = v_{n+1}(X_{n+1})$. Write the one-step-ahead risk-neutral pricing formula (2.4.12):

$$V_n = \frac{1}{1+r} \tilde{\mathbb{E}}_n [ V_{n+1} ] = \frac{1}{1+r} \tilde{\mathbb{E}}_n [ v_{n+1}(X_{n+1}) ]$$

3. **Apply Markov definition:** Because $X_n$ is a Markov process under $\tilde{\mathbb{P}}$, Definition 2.5.1 guarantees that there exists a deterministic function $g(x)$ such that:

$$\tilde{\mathbb{E}}_n [ v_{n+1}(X_{n+1}) ] = g(X_n)$$

4. **Define recursive function:** Set the function $v_n(x)$ as $v_n(x) = \frac{1}{1+r} g(x)$. This function depends only on the known parameters of the model, $r$, $v_{n+1}$, and the transition probabilities.
5. **Conclude step:** Substitute this definition to obtain $V_n = v_n(X_n)$, completing the induction step and proving the theorem for all $0 \le n \le N$ $\blacksquare$.

## 6. Exercises in this section

* **Exercise 2.7 (p. 56):** In a binomial model, give an example of a stochastic process that is a martingale but is not Markov.
* **Exercise 2.13 (p. 59) (Asian option):** Consider an $N$-period binomial model. An Asian option has a payoff based on the average stock price, i.e.,

$$V_N = f\left(\frac{1}{N+1} \sum_{k=0}^N S_k\right)$$

where the function $f$ is determined by the contractual details of the option.

* **(i)** Define $Y_n = \sum_{k=0}^n S_k$ and use the Independence Lemma 2.5.3 to show that the two-dimensional process $(S_n, Y_n), n = 0, 1, \dots, N$ is Markov.
* **(ii)** According to Theorem 2.5.8, the price $V_n$ of the Asian option at time $n$ is some function $v_n$ of $S_n$ and $Y_n$; i.e.,

$$V_n = v_n\left(S_n, \sum_{k=0}^n S_k\right), \quad n = 0, 1, \dots, N.$$

Give a formula for $v_N(s, y)$, and provide an algorithm for computing $v_n(s, y)$ in terms of $v_{n+1}$.

* **Exercise 2.14 (p. 60) (Asian option continued):** Consider an $N$-period binomial model, and let $M$ be a fixed number between $0$ and $N-1$. Consider an Asian option whose payoff at time $N$ is

$$V_N = f\left(\frac{1}{N-M} \sum_{k=M+1}^N S_k\right)$$

where again the function $f$ is determined by the contractual details of the option.

* **(i)** Define

$$Y_n = \begin{cases} 0 & \text{if } 0 \le n \le M \\ \sum_{k=M+1}^n S_k & \text{if } M+1 \le n \le N \end{cases}$$

Show that the two-dimensional process $(S_n, Y_n), n = 0, 1, \dots, N$ is Markov (under the risk-neutral measure $\tilde{\mathbb{P}}$).

* **(ii)** According to Theorem 2.5.8, the price $V_n$ of the Asian option at time $n$ is some function $v_n$ of $S_n$ and $Y_n$, i.e., $V_n = v_n(S_n, Y_n)$ for $n = 0, 1, \dots, N$. Of course, when $n \le M$, $Y_n$ is not random and does not need to be included in this function. Thus, for such $n$ we should seek a function $v_n$ of $S_n$ alone and have

$$V_n = \begin{cases} v_n(S_n) & \text{if } 0 \le n \le M \\ v_n(S_n, Y_n) & \text{if } M+1 \le n \le N \end{cases}$$

Give a formula for $v_N(s, y)$, and provide an algorithm for computing $v_n$ in terms of $v_{n+1}$. Note that the algorithm is different for $n < M$ and $n > M$, and there is a separate transition formula for $v_M(s)$ in terms of $v_{M+1}(\cdot, \cdot)$.

## 7. Cross-references

* **Chapter 1 Precursor (Section 1.3, p. 15):** The computational lookback option pricing algorithm in Example 1.3.2 is cited as the primary precursor and concrete application of this formalization. It priced a payoff of $V_3 = M_3 - S_3$ using functions of $(S_n, M_n)$ without storing the history of coin tosses, which is shown in Example 2.5.6 to be a valid two-dimensional Markov process.
* **Section 2.3 (Conditional Expectations):** The Independence Lemma (Lemma 2.5.3) is presented as a generalization of the "taking out what is known" property (Theorem 2.3.2(ii), p. 34) and the Independence property (Theorem 2.3.2(iv), p. 34).
* **Risk-Neutral Pricing Connection:** The pricing algorithm (2.5.2) and (2.5.9) simplifies the general multiperiod pricing formula of Theorem 2.4.7 (p. 41) into a backward recursive equation on deterministic state functions.
* **Continuous-Time Development (Vol II, Chapter 5 & 6):** The discrete recursive algorithm (2.5.9) is identified as the precursor to partial differential equations (PDEs) in continuous time. The theoretical tool that bridges continuous-time risk-neutral expectations and these PDEs is explicitly cited as the **Feynman-Kac Theorem** (p. 52).