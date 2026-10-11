## 1. Concept and context

Chapters 1–3 work with a constant up factor $u$, down factor $d$ and interest rate $r$. Three linked exercises, all titled *Stochastic volatility, random interest rate* — Exercise 1.9 (pp. 22–23), Exercise 2.9 (p. 57) and Exercise 3.5 (p. 85) — relax this assumption: the up factor, the down factor and the interest rate are allowed to depend on the time $n$ and on the first $n$ coin tosses. Exercise 1.9 sets up the general model and asks for its replication algorithm; Exercise 2.9 specializes it to a two-period instance (Figure 2.8.1) and asks for the risk-neutral measure and the corresponding pricing formula; Exercise 3.5 takes the same instance with an actual probability measure and prices the same option through the Radon-Nikodým derivative process, without the risk-neutral measure. The three exercises were deferred from the Chapter 1–3 cards by project decision and are grouped here because they anticipate Chapter 6: once the interest rate is random, the discount factor applied to a payoff at time $N$ is the path-dependent product $(1+r_0)(1+r_1)\cdots(1+r_{N-1})$, which Section 6.2 formalizes as the discount process $D_n$ (Eq. 6.2.2, p. 145).

## 2. Formal definitions

* **$u_n(\omega_1\omega_2\dots\omega_n)$, $d_n(\omega_1\omega_2\dots\omega_n)$**: the "up factor" and "down factor" at time $n\ge1$, allowed to depend on $n$ and on the first $n$ coin tosses. The initial up factor $u_0$ and down factor $d_0$ are not random (Exercise 1.9, p. 22).
* **$r_n(\omega_1\omega_2\dots\omega_n)$**: the interest rate at time $n\ge1$, allowed to depend on $n$ and on the first $n$ coin tosses; the initial interest rate $r_0$ is not random. One dollar invested in or borrowed from the money market at time zero grows to an investment or debt of $1+r_0$ at time one, and one dollar invested in or borrowed from the money market at time $n$ grows to an investment or debt of $1+r_n(\omega_1\omega_2\dots\omega_n)$ at time $n+1$ (pp. 22–23).
* **$S_n$**: the stock price, starting from $S_0$ and moving by the factor $u_n$ or $d_n$ that applies at the current node (equations in Section 3 below, p. 22).
* **$\tilde{\mathbb P}(HH),\tilde{\mathbb P}(HT),\tilde{\mathbb P}(TH),\tilde{\mathbb P}(TT)$**: in the two-period model of Exercise 2.9, the risk-neutral probabilities of the four paths, to be determined so that the time-zero value of an option paying $V_2$ at time two is given by the risk-neutral pricing formula with discount factor $(1+r_0)(1+r_1)$ (p. 57).
* **$\mathbb P$**: in Exercise 3.5, the actual probability measure on the same two-period model (p. 85).
* **$Z$**: the Radon-Nikodým derivative of $\tilde{\mathbb P}$ with respect to $\mathbb P$, $Z(\omega)=\tilde{\mathbb P}(\omega)/\mathbb P(\omega)$ (Eq. 3.1.1), evaluated in Exercise 3.5(i).
* **$Z_0,Z_1,Z_2$**: the Radon-Nikodým derivative process (Definition 3.2.4), which in Exercise 3.5(ii) satisfies $Z_2=Z$ and $Z_0=\mathbb EZ=1$ (p. 85).

## 3. Key equations

*(Note: The author does not assign equation numbers within these exercises. The formulas printed in the problem statements are presented with the exact notation.)*

*Exercise 1.9 — model dynamics (p. 22):*

$$S_1(\omega_1)=\begin{cases}u_0S_0 & \text{if } \omega_1=H,\\ d_0S_0 & \text{if } \omega_1=T,\end{cases}$$

$$S_{n+1}(\omega_1\omega_2\dots\omega_n\omega_{n+1})=\begin{cases}u_n(\omega_1\omega_2\dots\omega_n)S_n(\omega_1\omega_2\dots\omega_n) & \text{if } \omega_{n+1}=H,\\ d_n(\omega_1\omega_2\dots\omega_n)S_n(\omega_1\omega_2\dots\omega_n) & \text{if } \omega_{n+1}=T,\end{cases} \quad n\ge1$$

*Exercise 1.9 — no-arbitrage conditions (p. 23):*

$$0<d_n(\omega_1\omega_2\dots\omega_n)<1+r_n(\omega_1\omega_2\dots\omega_n)<u_n(\omega_1\omega_2\dots\omega_n) \quad \text{for each } n \text{ and all } \omega_1\omega_2\dots\omega_n$$

$$0<d_0<1+r_0<u_0$$

*Exercise 2.9(i) — risk-neutral pricing formula with random interest rate (p. 57):*

$$V_0=\tilde{\mathbb E}\left[\frac{V_2}{(1+r_0)(1+r_1)}\right]$$

*Exercise 3.5 — actual measure (p. 85):*

$$\mathbb P(HH)=\frac49,\quad \mathbb P(HT)=\frac29,\quad \mathbb P(TH)=\frac29,\quad \mathbb P(TT)=\frac19$$

*Exercise 3.5(iii) — the version of the risk-neutral pricing formula (3.2.6) appropriate for this model, which does not use the risk-neutral measure (p. 85):*

$$V_1(H)=\frac{1+r_0}{Z_1(H)}\,\mathbb E_1\left[\frac{Z_2}{(1+r_0)(1+r_1)}V_2\right](H)=\frac{1}{Z_1(H)\big(1+r_1(H)\big)}\,\mathbb E_1[Z_2V_2](H)$$

$$V_1(T)=\frac{1+r_0}{Z_1(T)}\,\mathbb E_1\left[\frac{Z_2}{(1+r_0)(1+r_1)}V_2\right](T)=\frac{1}{Z_1(T)\big(1+r_1(T)\big)}\,\mathbb E_1[Z_2V_2](T)$$

$$V_0=\mathbb E\left[\frac{Z_2}{(1+r_0)(1+r_1)}V_2\right]$$

## 4. Assumptions and domain of validity

* **Node-wise no-arbitrage:** the condition $0<d<1+r<u$ of Eq. (1.1.2) is replaced by one condition per node, $0<d_n<1+r_n<u_n$ for every $n$ and every $\omega_1\dots\omega_n$, together with $0<d_0<1+r_0<u_0$ (p. 23). In particular $1+r_n>d_n>0$, so $r_n>-1$ at every node — the only assumption that Chapter 6 makes on its interest rate process (Eq. 6.2.1, p. 145).
* **Adaptedness:** $u_n$, $d_n$ and $r_n$ depend only on the first $n$ coin tosses, and $u_0,d_0,r_0$ are not random (p. 22). The rate $r_n$ that applies between times $n$ and $n+1$ is therefore known at time $n$, whereas the stock price at time $n+1$ is not; Section 6.2 makes the same point about its interest rate process (p. 145).
* **Path-dependent discounting:** because $r_1$ depends on the first toss, the discount factor $\frac{1}{(1+r_0)(1+r_1)}$ in Exercises 2.9 and 3.5 is a random variable that stays inside the expectation, instead of the constant $(1+r)^{-N}$ that can be taken outside it in Eqs. (2.4.11) and (3.2.6). In Exercise 3.5(iii) the factor $1+r_1$ can be taken out of $\mathbb E_1$ because $r_1$ is known at time one, which gives the second form of $V_1(H)$ and $V_1(T)$.
* **No recombination in the state $S_n$:** in Figure 2.8.1, $S_2(HT)=S_2(TH)=8$, but the two nodes are reached through different interest rates, $r_1(H)=1/4$ and $r_1(T)=1/2$. The stock price alone does not describe the state of the model, so the state reduction of Section 1.3, which relies on a recombining tree with constant parameters, does not apply to it directly.
* **Conditional expectations:** Definition 2.3.1 defines $\tilde{\mathbb E}_n$ for independent coin tosses with constant probabilities $\tilde p,\tilde q$. When $u_n,d_n,r_n$ vary from node to node, the risk-neutral measure need not have that product form; the book's general definition of conditional expectation for this situation is Definition 6.2.2 (p. 150), which satisfies all the properties of Theorem 2.3.2 (Remark 6.2.3). Under the actual measure of Exercise 3.5, $\mathbb P(HH)=\left(\frac23\right)^2$, $\mathbb P(HT)=\mathbb P(TH)=\frac23\cdot\frac13$ and $\mathbb P(TT)=\left(\frac13\right)^2$, so the tosses are independent with $p=2/3$ and $\mathbb E_1$ is the usual Definition 2.3.1.
* **Strictly positive probabilities:** $\mathbb P$ and $\tilde{\mathbb P}$ must assign strictly positive probability to every path so that $Z=\tilde{\mathbb P}/\mathbb P$ is defined and strictly positive (Theorem 3.1.1).

## 5. Theorems and proof outline

Not covered in this section (being exercises, they do not introduce formal theorems or proofs of their own). They ask to carry three results of Chapters 1–3 over to the model with random $u_n$, $d_n$, $r_n$: the replication algorithm of Theorem 1.2.2 (Exercise 1.9(i)–(ii)), the risk-neutral pricing formula of Theorem 2.4.7 (Exercise 2.9(i)), and the formula (3.2.6) of Theorem 3.2.7, which Exercise 3.5(iii) rewrites in the "version appropriate for this model" printed in Section 3 above. The systematic version of these results for a random interest rate is Theorem 6.2.6 and Remark 6.2.8 of Chapter 6.

## 6. Exercises in this section

* **Exercise 1.9 (Stochastic volatility, random interest rate) (pp. 22–23):** Consider a binomial pricing model, but at each time $n\ge1$, the "up factor" $u_n(\omega_1\omega_2\dots\omega_n)$, the "down factor" $d_n(\omega_1\omega_2\dots\omega_n)$, and the interest rate $r_n(\omega_1\omega_2\dots\omega_n)$ are allowed to depend on $n$ and on the first $n$ coin tosses $\omega_1\omega_2\dots\omega_n$. The initial up factor $u_0$, the initial down factor $d_0$, and the initial interest rate $r_0$ are not random. The stock price evolves as in Section 3, the money market grows by $1+r_n$ between times $n$ and $n+1$, and the no-arbitrage conditions of Section 3 hold.
1. Let $N$ be a positive integer. In the model just described, provide an algorithm for determining the price at time zero for a derivative security that at time $N$ pays off a random amount $V_N$ depending on the result of the first $N$ coin tosses.
2. Provide a formula for the number of shares of stock that should be held at each time $n$ ($0\le n\le N-1$) by a portfolio that replicates the derivative security $V_N$.
3. Suppose the initial stock price is $S_0=80$, with each head the stock price increases by $10$, and with each tail the stock price decreases by $10$. In other words, $S_1(H)=90$, $S_1(T)=70$, $S_2(HH)=100$, etc. Assume the interest rate is always zero. Consider a European call with strike price $80$, expiring at time five. What is the price of this call at time zero?

* **Exercise 2.9 (Stochastic volatility, random interest rate) (p. 57):** Consider a two-period stochastic volatility, random interest rate model of the type described in Exercise 1.9 of Chapter 1. The stock prices and interest rates are shown in Figure 2.8.1: $S_0=4$, $r_0=\frac14$; $S_1(H)=8$, $r_1(H)=\frac14$; $S_1(T)=2$, $r_1(T)=\frac12$; $S_2(HH)=12$, $S_2(HT)=8$, $S_2(TH)=8$, $S_2(TT)=2$.
1. Determine risk-neutral probabilities $\tilde{\mathbb P}(HH)$, $\tilde{\mathbb P}(HT)$, $\tilde{\mathbb P}(TH)$, $\tilde{\mathbb P}(TT)$ such that the time-zero value of an option that pays off $V_2$ at time two is given by the risk-neutral pricing formula $V_0=\tilde{\mathbb E}\left[\frac{V_2}{(1+r_0)(1+r_1)}\right]$.
2. Let $V_2=(S_2-7)^+$. Compute $V_0$, $V_1(H)$, and $V_1(T)$.
3. Suppose an agent sells the option in (ii) for $V_0$ at time zero. Compute the position $\Delta_0$ the agent should take in the stock at time zero so that at time one, regardless of whether the first coin toss results in head or tail, the value of the agent's portfolio is $V_1$.
4. Suppose in (iii) that the first coin toss results in head. What position $\Delta_1(H)$ should the agent now take in the stock to be sure that, regardless of whether the second coin toss results in head or tail, the value of the agent's portfolio at time two will be $(S_2-7)^+$?

* **Exercise 3.5 (Stochastic volatility, random interest rate) (p. 85):** Consider the model of Exercise 2.9 of Chapter 2. Assume that the actual probability measure is $\mathbb P(HH)=\frac49$, $\mathbb P(HT)=\frac29$, $\mathbb P(TH)=\frac29$, $\mathbb P(TT)=\frac19$. The risk-neutral measure was computed in Exercise 2.9 of Chapter 2.
1. Compute the Radon-Nikodým derivative $Z(HH)$, $Z(HT)$, $Z(TH)$, and $Z(TT)$ of $\tilde{\mathbb P}$ with respect to $\mathbb P$.
2. The Radon-Nikodým derivative process $Z_0,Z_1,Z_2$ satisfies $Z_2=Z$. Compute $Z_1(H)$, $Z_1(T)$, and $Z_0$. Note that $Z_0=\mathbb EZ=1$.
3. The version of the risk-neutral pricing formula (3.2.6) appropriate for this model, which does not use the risk-neutral measure, is the set of three formulas for $V_1(H)$, $V_1(T)$ and $V_0$ in Section 3 above. Use this formula to compute $V_1(H)$, $V_1(T)$, and $V_0$ when $V_2=(S_2-7)^+$. Compare the result with your answers in Exercise 2.9(ii) of Chapter 2. (The book prints "Exercise 2.6(ii)" here. Exercise 2.6 deals with discrete-time stochastic integrals and computes no option prices, while this exercise reuses the model and the payoff $(S_2-7)^+$ of Exercise 2.9(ii); the reference is almost certainly a typographical erratum for Exercise 2.9(ii). This correction is our reading, not one stated in the book.)

## 7. Cross-references

* **Theorem 1.2.2 (Chapter 1, p. 12):** the replication algorithm (1.2.15)–(1.2.17) for constant $u$, $d$, $r$, which Exercise 1.9(i)–(ii) asks to extend to node-dependent parameters.
* **Theorems 2.4.5 and 2.4.7 (Chapter 2, pp. 40–42):** the discounted wealth martingale and the risk-neutral pricing formula (2.4.11), whose constant discount factor $(1+r)^{-N}$ becomes $\frac{1}{(1+r_0)(1+r_1)}$ in Exercise 2.9(i).
* **Lemma 3.2.6 and Theorem 3.2.7 (Chapter 3, pp. 69–70):** the conditional change of measure (3.2.5) and the equality chain (3.2.6) that Exercise 3.5(iii) rewrites for this model.
* **Section 1.3 (Chapter 1):** the state reduction for recombining trees with constant parameters, which does not apply directly to the non-recombining state of Figure 2.8.1.
* **Section 6.2 (Chapter 6, pp. 144–154):** the interest rate process $R_n$ with condition (6.2.1), the discount process $D_n$ (6.2.2), the conditional expectation for non-independent coin tosses (Definition 6.2.2 and Remark 6.2.3), the martingale property of discounted wealth (Theorem 6.2.6) and the risk-neutral pricing formula with random discounting (6.2.8) are the systematic versions of the objects that appear in these three exercises.
