## 1. Concept and context

Under a risk-neutral probability measure, the discounted price of a non-dividend-paying stock has no systematic tendency to rise or fall, meaning its expected future value is equal to its current value. Martingales mathematically formalize this concept of a "fair game" in a multiperiod setting, allowing the linear pricing of derivatives by expressing intermediate values as conditional expectations of discounted terminal payoffs (Section 2.4, pp. 36–37). This framework establishes the first fundamental theorem of asset pricing by showing that the existence of a risk-neutral martingale measure is mathematically equivalent to the complete exclusion of arbitrage opportunities (Section 2.4, p. 41).

## 2. Formal definitions

Below are the mathematical objects introduced in this section, using the exact notation of the book:

* **Adapted Stochastic Process:** A sequence of random variables $M_0, M_1, \dots, M_N$, where each $M_n$ depends only on the first $n$ coin tosses, and $M_0$ is a constant (Definition 2.4.1, p. 36).
* **Martingale:** An adapted stochastic process satisfying (Definition 2.4.1(i), p. 36):

$$M_n = \mathbb{E}_n[M_{n+1}], \quad n = 0, 1, \dots, N-1$$

* **Submartingale:** An adapted stochastic process satisfying (Definition 2.4.1(ii), p. 36):

$$M_n \le \mathbb{E}_n[M_{n+1}], \quad n = 0, 1, \dots, N-1$$

* **Supermartingale:** An adapted stochastic process satisfying (Definition 2.4.1(iii), p. 37):

$$M_n \ge \mathbb{E}_n[M_{n+1}], \quad n = 0, 1, \dots, N-1$$

* **Portfolio Process (Adapted):** A sequence $\Delta_0, \Delta_1, \dots, \Delta_{N-1}$ of random variables, where $\Delta_n$ represents the number of stock shares held from time $n$ to $n+1$ and depends only on the first $n$ coin tosses (Definition 2.4.1, p. 36).
* **Wealth Process:** The sequence of random variables $X_0, X_1, \dots, X_N$ generated recursively from initial capital $X_0$ by (p. 40):

$$X_{n+1} = \Delta_n S_{n+1} + (1+r)(X_n - \Delta_n S_n)$$

* **Cash Flow Process:** A sequence of random variables $C_0, C_1, \dots, C_N$ such that each $C_n$ depends only on the first $n$ tosses $\omega_1\dots\omega_n$ (p. 42).
* **Value of Cash Flow Payments:** The price process $V_n$ representing the net present value at time $n$ of the future payments $C_n, \dots, C_N$ (p. 42).

## 3. Key equations

$$\frac{S_n}{(1+r)^n} = \mathbb{E}_n\left[ \frac{S_{n+1}}{(1+r)^{n+1}} \right] \quad \text{(2.4.1)}$$

$$M_n = \mathbb{E}_n[M_{n+1}], \quad n = 0, 1, \dots, N-1 \quad \text{(2.4.2)}$$

$$M_n = \mathbb{E}_n[M_m], \quad 0 \le n \le m \le N \quad \text{(2.4.3)}$$

$$M_0 = \mathbb{E}M_n, \quad n = 0, 1, \dots, N \quad \text{(2.4.4)}$$

$$\tilde{\mathbb{E}}_n\left[ \left(\frac{4}{5}\right)^{n+1} S_{n+1} \right] = \left(\frac{4}{5}\right)^nS_n \quad \text{(2.4.5)}$$

$$X_{n+1} = \Delta_n S_{n+1} + (1+r)(X_n - \Delta_n S_n) \quad \text{(2.4.6)}$$

$$\frac{X_n}{(1+r)^n} = \tilde{\mathbb{E}}_n\left[ \frac{X_{n+1}}{(1+r)^{n+1}} \right], \quad n = 0, 1, \dots, N-1 \quad \text{(2.4.7)}$$

$$\tilde{\mathbb{E}} \left[ \frac{X_n}{(1+r)^n} \right] = X_0, \quad n = 0, 1, \dots, N \quad \text{(2.4.8)}$$

$$\frac{X_n}{(1+r)^n} = \mathbb{E}_n\left[ \frac{X_N}{(1+r)^N} \right] = \mathbb{E}_n\left[ \frac{V_N}{(1+r)^N} \right] \quad \text{(2.4.9)}$$

$$\frac{V_n}{(1+r)^n} = \tilde{\mathbb{E}}_n\left[ \frac{V_N}{(1+r)^N} \right] \quad \text{(2.4.10)}$$

$$V_n = \tilde{\mathbb{E}}_n\left[ \frac{V_N}{(1+r)^{N-n}} \right] \quad \text{(2.4.11)}$$

$$\frac{V_n}{(1+r)^n} = \tilde{\mathbb{E}}_n\left[ \frac{V_{n+1}}{(1+r)^{n+1}} \right], \quad n = 0, 1, \dots, N-1 \quad \text{(2.4.12)}$$

$$V_n = \tilde{\mathbb{E}}_n\left[ \sum_{k=n}^N \frac{C_k}{(1+r)^{k-n}} \right], \quad n = 0, 1, \dots, N \quad \text{(2.4.13)}$$

$$C_n(\omega_1 \dots \omega_n) = V_n(\omega_1 \dots \omega_n) - \frac{1}{1+r}\left[\tilde{p}V_{n+1}(\omega_1 \dots \omega_n H) + \tilde{q}V_{n+1}(\omega_1 \dots \omega_n T)\right] \quad \text{(2.4.14)}$$

$$\Delta_n(\omega_1 \dots \omega_n) = \frac{V_{n+1}(\omega_1 \dots \omega_n H) - V_{n+1}(\omega_1 \dots \omega_n T)}{S_{n+1}(\omega_1 \dots \omega_n H) - S_{n+1}(\omega_1 \dots \omega_n T)} \quad \text{(2.4.15)}$$

$$X_{n+1} = \Delta_n S_{n+1} + (1+r)(X_n - C_n - \Delta_n S_n) \quad \text{(2.4.16)}$$

$$X_n(\omega_1 \dots \omega_n) = V_n(\omega_1 \dots \omega_n) \quad \text{(2.4.17)}$$

$$V_n = C_n + \tilde{\mathbb{E}}_n\left[ \sum_{k=n+1}^N \frac{C_k}{(1+r)^{k-n}} \right], \quad n = 0, 1, \dots, N-1 \quad \text{(2.4.18)}$$

$$V_N = C_N \quad \text{(2.4.19)}$$

## 4. Assumptions and domain of validity

* **Strict Positivity:** The actual and risk-neutral measures must assign strictly positive probabilities to all $2^N$ paths (p. 26).
* **No-Arbitrage Parameters:** The parameters of the model must satisfy the no-arbitrage condition $0 < d < 1 + r < u$. If this is violated, risk-neutral probabilities $\tilde{p}$ and $\tilde{q}$ do not exist (p. 26).
* **No Dividends:** The stock is assumed to pay no dividends (Theorem 2.4.4, p. 38). (The dividend-paying case is treated separately in Exercise 2.10).
* **Self-Financing Wealth:** Corollary 2.4.6 requires that wealth is managed strictly according to (2.4.6), meaning no external capital is added or withdrawn from the portfolio during trading.

## 5. Theorems and proof outline

**Theorem 2.4.4 (Discounted Stock Price is a Martingale):** Under the risk-neutral measure, the discounted stock price $\left\lbrace \frac{S_n}{(1+r)^n} \right\rbrace_{n=0}^N$ is a martingale, meaning (2.4.1) holds.

*First Proof (Elementary Proof):*

1. **Conditional sum structure:** Fix $n$ and $\omega_1 \dots \omega_n$. Write the conditional expectation of $\frac{S_{n+1}}{(1+r)^{n+1}}$ based on information at time $n$ using the risk-neutral probabilities $\tilde{p}$ and $\tilde{q}$.
2. **Substitute next-step prices:** Replace the next-period stock values with their up and down realizations: $S_{n+1}(\omega_1 \dots \omega_n H) = u S_n$ and $S_{n+1}(\omega_1 \dots \omega_n T) = d S_n$.
3. **Factorization:** Factor out the common term $S_n(\omega_1 \dots \omega_n)$ and the discounting terms from the summation, leaving $\tilde{p}u + \tilde{q}d$.
4. **Incorporate risk-neutral definitions:** Use the definition of the risk-neutral probabilities to simplify the term: $\tilde{p}u + \tilde{q}d = 1+r$.
5. **Algebraic cancellation:** Cancel $1+r$ in the numerator with one factor of $(1+r)^{n+1}$ in the denominator to obtain $\frac{S_n}{(1+r)^n}$, completing the proof.

*Second Proof (Deeper Proof, using Theorem 2.3.2):*

1. **Decompose the fraction:** Rewrite the target term inside the conditional expectation as $\frac{S_{n+1}}{(1+r)^{n+1}} = \frac{S_n}{(1+r)^n} \cdot \frac{1}{1+r} \cdot \frac{S_{n+1}}{S_n}$.
2. **Pull out known terms:** Since $\frac{S_n}{(1+r)^n}$ depends only on the first $n$ coin tosses, pull it outside the conditional expectation $\tilde{\mathbb{E}}_n$ using the "taking out what is known" property.
3. **Identify independent ratios:** This leaves the conditional expectation of $\frac{1}{1+r} \frac{S_{n+1}}{S_n}$. Note that the stock price ratio $\frac{S_{n+1}}{S_n}$ depends only on the $(n+1)$-st toss.
4. **Apply independence:** Because the $(n+1)$-st toss is independent of the first $n$ tosses, apply the independence property (Theorem 2.3.2(iv)) to replace $\tilde{\mathbb{E}}_n$ with the unconditional expectation $\tilde{\mathbb{E}}$.
5. **Evaluate expectation:** Calculate $\tilde{\mathbb{E}}\left[ \frac{S_{n+1}}{(1+r)S_n} \right] = \frac{1}{1+r} [\tilde{p}u + \tilde{q}d] = \frac{1+r}{1+r} = 1$.
6. **Multiply out:** Multiply this result by the pulled-out factor $\frac{S_n}{(1+r)^n}$ to recover the martingale identity.

**Theorem 2.4.5 (Discounted Wealth is a Martingale):** Let $\Delta_0, \Delta_1, \dots, \Delta_{N-1}$ be an adapted portfolio process, and let the wealth process $X_0, X_1, \dots, X_N$ be generated according to (2.4.6). Then $\frac{X_n}{(1+r)^n}$ is a martingale under the risk-neutral measure.

*Proof Outline:*

1. **Substitute wealth recursion:** Write the conditional expectation of the discounted wealth at $n+1$: $\tilde{\mathbb{E}}_n \left[ \frac{X_{n+1}}{(1+r)^{n+1}}\right] = \tilde{\mathbb{E}}_n \left[ \frac{\Delta_n S_{n+1} + (1+r)(X_n - \Delta_n S_n)}{(1+r)^{n+1}}\right]$.
2. **Linearity expansion:** Use the linearity of conditional expectations (Theorem 2.3.2(i)) to split the expectation into stock-related and cash-related fractions.
3. **Factor out known variables:** Since $\Delta_n$, $X_n$, and $S_n$ are known at time $n$, apply "taking out what is known" (Theorem 2.3.2(ii)) to factor them outside of $\tilde{\mathbb{E}}_n$.
4. **Incorporate stock martingale property:** Use the martingale property of the discounted stock price (Theorem 2.4.4) to replace $\tilde{\mathbb{E}}_n\left[ \frac{S_{n+1}}{(1+r)^{n+1}}\right]$ with $\frac{S_n}{(1+r)^n}$.
5. **Simplify algebraically:** This reduces the right-hand side of the wealth equation to $\Delta_n \frac{S_n}{(1+r)^n} + \frac{X_n - \Delta_n S_n}{(1+r)^n} = \frac{X_n}{(1+r)^n}$. This proves the martingale relation (2.4.7).

**Theorem 2.4.7 (Risk-Neutral Pricing Formula):** Let $V_N$ be the payoff at time $N$ of a derivative security. For $n$ between $0$ and $N$, the no-arbitrage price $V_n$ of the derivative is given by (2.4.11).

*Proof Outline:*

1. **Replication boundary condition:** Let $X_n$ be the wealth process of a replicating portfolio that satisfies $X_N = V_N$.
2. **Stochastic martingale pricing:** Because $\frac{X_n}{(1+r)^n}$ is a risk-neutral martingale (Theorem 2.4.5), apply the multi-step-ahead martingale property (Remark 2.4.2) to write $\frac{X_n}{(1+r)^n} = \tilde{\mathbb{E}}_n \left[ \frac{X_N}{(1+r)^N} \right]$.
3. **Evaluate at boundary:** Replace $X_N$ with the target payoff $V_N$ inside the expectation: $\frac{X_n}{(1+r)^n} = \tilde{\mathbb{E}}_n \left[ \frac{V_N}{(1+r)^N} \right]$.
4. **Define option price:** Apply the no-arbitrage principle (Definition 1.2.3) to set the option price $V_n = X_n$, which yields (2.4.10).
5. **Isolate $V_n$:** Multiply both sides by $(1+r)^n$ to isolate $V_n$ and obtain the risk-neutral pricing formula: $V_n = \tilde{\mathbb{E}}_n \left[ \frac{V_N}{(1+r)^{N-n}} \right]$.
6. **Verify martingale property:** Re-apply the martingale definition to the resulting discounted price process $\frac{V_n}{(1+r)^n}$ to verify (2.4.12).

**Theorem 2.4.8 (Cash Flow Valuation):** *(Reference Statement)* The price at time $n$ of a security making payments $C_n, \dots, C_N$ at times $n, \dots, N$ is given by (2.4.13), satisfies (2.4.14)–(2.4.19), and admits no arbitrage.

## 6. Exercises in this section

* **Exercise 2.3 (p. 55):** Show that a convex function of a martingale is a submartingale. In other words, let $M_0, M_1, \dots, M_N$ be a martingale and let $\varphi$ be a convex function. Show that $\varphi(M_0), \varphi(M_1), \dots, \varphi(M_N)$ is a submartingale.
* **Exercise 2.4 (p. 55):** Toss a coin repeatedly. Assume the probability of head on each toss is $1/2$, as is the probability of tail. Let $X_j = 1$ if the $j$th toss results in a head and $X_j = -1$ if the $j$th toss results in a tail. Define

$$M_n = \sum_{j=1}^n X_j, \quad n \ge 1.$$

This is called a symmetric random walk; with each head, it steps up one, and with each tail, it steps down one.

1. Using the properties of Theorem 2.3.2, show that $M_0, M_1, M_2, \dots$ is a martingale.
2. Let $\sigma$ be a positive constant and, for $n \ge 0$, define

$$S_n = e^{\sigma M_n} \left( \frac{2}{e^\sigma + e^{-\sigma}} \right)^n.$$

Show that $S_0, S_1, S_2, \dots$ is a martingale. Note that even though the symmetric random walk $M_n$ has no tendency to grow, the "geometric symmetric random walk" $e^{\sigma M_n}$ does have a tendency to grow.

* **Exercise 2.8 (p. 56):** Consider an $N$-period binomial model.
1. Let $M_0, M_1, \dots, M_N$ and $M'_0, M'_1, \dots, M'_N$ be martingales under the risk-neutral measure $\tilde{\mathbb{P}}$. Show that if $M_N = M'_N$ (for every possible outcome of the sequence of coin tosses), then $M_n = M'_n$ for every $n$ and every outcome.
2. Let $V_N$ be the payoff at time $N$ of some derivative security. This is a random variable that can depend on all $N$ coin tosses. Define recursively $V'_{N-1}, V'_{N-2}, \dots, V'_0$ by the backward recursion formula (1.2.16):



$$V'_0, \frac{V'_1}{1+r}, \dots, \frac{V'_{N-1}}{(1+r)^{N-1}}, \frac{V_N}{(1+r)^N}$$

is a martingale under $\tilde{\mathbb{P}}$.

3. Using the risk-neutral pricing formula (2.4.11) of this chapter, define

$$V_n = \tilde{\mathbb{E}}_n \left[ \frac{V_N}{(1+r)^{N-n}} \right], \quad n = 0, 1, \dots, N-1.$$

Show that

$$V_0, \frac{V_1}{1+r}, \dots, \frac{V_{N-1}}{(1+r)^{N-1}}, \frac{V_N}{(1+r)^N}$$

is a martingale.

4. Conclude that $V_n = V'_n$ for every $n$ (i.e., the algorithm (1.2.16) of Theorem 1.2.2 of Chapter 1 gives the same derivative security prices as the risk-neutral pricing formula (2.4.11)).

* **Exercise 2.11 (p. 58):** Consider a stock that pays no dividend in an $N$-period binomial model. A European call has payoff $C_N = (S_N - K)^+$ at time $N$, priced via the risk-neutral pricing formula. A European put has payoff $P_N = (K - S_N)^+$. A forward contract has payoff $F_N = S_N - K$.
1. If at time zero you buy a forward contract and a put, and hold them until expiration, explain why the payoff you receive is the same as the payoff of a call; i.e., explain why $C_N = F_N + P_N$.
2. Using the risk-neutral pricing formulas for $C_n$, $P_n$, and $F_n$, and the linearity of conditional expectations, show that $C_n = F_n + P_n$ for every $n$.
3. Using the fact that the discounted stock price is a martingale under the risk-neutral measure, show that $F_0 = S_0 - \frac{K}{(1+r)^N}$.
4. Show that starting at time zero with $F_0$, buying one share of stock and borrowing as necessary, with no further trades, gives a portfolio valued at $F_N$ at time $N$ (static replication of the forward).
5. The forward price is the value of $K$ that makes the forward contract worth zero at time zero; here it is $(1+r)^N S_0$. Show that, at time zero, a call struck at the forward price has the same price as a put struck at the forward price.
6. If $K = (1+r)^N S_0$, do we have $C_n = P_n$ for every $n$?


* **Exercise 2.12 (p. 59):** Let $1 \le m \le N-1$ and $K > 0$ be given. A chooser option is a contract sold at time zero that confers on its owner the right to receive either a call or a put at time $m$, with a strike price of $K$. The owner can choose at time $m$ which one to receive.
1. Show that the payoff at time $m$ of a chooser option is $\max(C_m, P_m)$.
2. Using the risk-neutral pricing formula and the fact that the maximum of two martingales is a submartingale, explain why the chooser option price at time zero is at least as much as the call price at time zero.



## 7. Cross-references

* **Chapter 1 Foundations:** Theorem 2.4.7 (Risk-Neutral Pricing) and Exercise 2.8 directly rely on the multiperiod replication results of Theorem 1.2.2 and the backward recursion formula (1.2.16).
* **Theorem 2.3.2 (Properties of Conditional Expectations):** Martingales are formulated on Theorem 2.3.2, specifically using:
* **Linearity (i):** Essential for the proof of wealth pricing (Theorem 2.4.5) and Exercise 2.11(ii).
* **Taking out what is known (ii) & Independence (iv):** Used to compute the elementary and deeper proofs of Theorem 2.4.4.
* **Iterated Conditioning (iii):** Required to propagate the martingale property over multiple steps (Remark 2.4.2).


* **Section 3.2 Generalization:** The risk-neutral pricing framework is restated using state price densities and Radon-Nikodym derivative processes $Z_n$ in Theorem 3.2.7.
* **Chapter 4 Connections:** Discounted European option price martingales (Theorem 2.4.7) are contrasted against discounted American option prices, which are shown to be supermartingales under the risk-neutral measure.
* **Chapter 6 Term-Structure:** The cash flow valuation principles of Theorem 2.4.8 are utilized in Chapter 6 to value coupon-paying bonds, interest rate swaps, and swaps under stochastic interest rates.
* **Volatility / Random Interest Rates:** *Note*: Exercise 2.9 (which details stochastic volatility and random interest rates) is included in Section 2.4 of the book but is treated separately in this online version.