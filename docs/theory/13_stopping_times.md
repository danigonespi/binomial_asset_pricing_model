## 1. Concept and context

The time at which an American option should be exercised is generally random: it depends on the price movements of the underlying asset. In the two-period American put of Example 4.2.1 ($S_0=4$, $u=2$, $d=1/2$, $r=1/4$, strike $5$), if the first toss is $T$ the option is deep in the money and should be exercised immediately at $n=1$; if the first toss is $H$ the option is out of the money and the owner should wait for the second toss (p. 96). This exercise decision is captured by the rule $\tau(HH)=\infty$, $\tau(HT)=2$, $\tau(TH)=1$, $\tau(TT)=1$ (4.3.1) — a decision at each node based only on the tosses observed so far. Contrast this with the rule $\rho(HH)=0$, $\rho(HT)=0$, $\rho(TH)=1$, $\rho(TT)=2$ (4.3.2), which a clairvoyant owner with foreknowledge of the coin tosses would use to always exercise exactly when the option is in the money. Because deciding whether to exercise at time $0$ under $\rho$ requires already knowing the outcome of the first toss, $\rho$ requires "insider information" and is not implementable — it is not a valid stopping time (p. 97).

## 2. Formal definitions

* **$\tau$**: a stopping time — an exercise rule that decides to stop based only on information available at the time of the decision.
* **Definition 4.3.1**: in an $N$-period binomial model, a stopping time is a random variable $\tau$ taking values $0,1,\dots,N$ or $\infty$, satisfying: if $\tau(\omega_1\dots\omega_n\omega_{n+1}\dots\omega_N)=n$, then $\tau(\omega_1\dots\omega_n\omega_{n+1}'\dots\omega_N')=n$ for all $\omega_{n+1}'\dots\omega_N'$ — i.e., whether stopping occurs at time $n$ depends only on the first $n$ tosses, never on what comes after.
* **$n\wedge\tau$**: shorthand for $\min(n,\tau)$, the time index used to construct a stopped process.
* **$Y_{n\wedge\tau}$ (stopped process)**: given a process $Y_n$ and a stopping time $\tau$, the process whose value at time $n$ is $Y_{n\wedge\tau}$ — it continues evolving with $Y_n$ up to time $\tau$, and freezes at the value $Y_\tau$ for all times after $\tau$.

## 3. Key equations

$$\tau(HH)=\infty,\ \ \tau(HT)=2,\ \ \tau(TH)=1,\ \ \tau(TT)=1 \quad \text{(4.3.1)}$$

$$\rho(HH)=0,\ \ \rho(HT)=0,\ \ \rho(TH)=1,\ \ \rho(TT)=2 \quad \text{(4.3.2)}$$

*Unnumbered:* the notation $n\wedge\tau=\min(n,\tau)$, and every explicit numeric value of the stopped processes worked out in Example 4.2.1 continued (Section 6 below), are given without an equation number.

## 4. Assumptions and domain of validity

* A stopping time takes values in $\{0,1,\dots,N,\infty\}$; the value $\infty$ means the option is allowed to expire without ever being exercised (p. 97).
* **Non-anticipating condition:** the event $\{\tau=n\}$ must be completely determined by the first $n$ coin tosses. A rule that looks ahead — like $\rho$ — violates this and is not a stopping time.

## 5. Theorems and proof outline

**Theorem 4.3.2 (Optional sampling — Part I):** a martingale stopped at a stopping time is a martingale; a supermartingale (or submartingale) stopped at a stopping time is a supermartingale (or submartingale, respectively).

*Proof outline:* the book gives no formal proof here — it justifies the theorem entirely through the worked illustrations of Example 4.2.1 continued (Section 6), showing a martingale before and after stopping at $\tau$, and a supermartingale before and after stopping at $\tau$, then contrasting both against stopping the same processes at the non-stopping-time $\rho$, which destroys the martingale property by introducing a downward bias.

**Theorem 4.3.3 (Optional sampling — Part II):** let $X_n$, $n=0,1,\dots,N$, be a submartingale and $\tau$ a stopping time. Then $\mathbb{E}X_{n\wedge\tau}\le\mathbb{E}X_n$. If $X_n$ is a supermartingale, then $\mathbb{E}X_{n\wedge\tau}\ge\mathbb{E}X_n$; if $X_n$ is a martingale, then $\mathbb{E}X_{n\wedge\tau}=\mathbb{E}X_n$.

*Proof outline:* no formal proof is given. The book adds an explicit remark that the expectation here is computed under whichever probability measure makes $X_n$ a sub/super/martingale; in particular, if $X_n$ is a submartingale under the risk-neutral probabilities of the binomial model, the conclusion becomes $\tilde{\mathbb{E}}X_{n\wedge\tau}\le\tilde{\mathbb{E}}X_n$.

## 6. Exercises in this section (and required examples)

* **Example 4.2.1 continued — stopped processes:** using the discounted stock price $M_n=(4/5)^nS_n$ from the model of Example 4.2.1 ($M_0=4$; $M_1(H)=6.40$, $M_1(T)=1.60$; $M_2(HH)=10.24$, $M_2(HT)=M_2(TH)=2.56$, $M_2(TT)=0.64$), which is a martingale under $\tilde p=\tilde q=1/2$: stopping it at the valid stopping time $\tau$ of (4.3.1) gives $M_{0\wedge\tau}=4$, $M_{1\wedge\tau}(H)=6.40$, $M_{1\wedge\tau}(T)=1.60$, $M_{2\wedge\tau}(HH)=10.24$, $M_{2\wedge\tau}(HT)=2.56$, $M_{2\wedge\tau}(TH)=M_{2\wedge\tau}(TT)=1.60$ (the last two frozen at $M_1(T)$ since $\tau=1$ there) — still a martingale at every node. Stopping the same process at the non-stopping-time $\rho$ of (4.3.2) instead gives $M_{1\wedge\rho}(H)=4$, $M_{2\wedge\rho}(HH)=M_{2\wedge\rho}(HT)=4$ (frozen at $M_0$ since $\rho=0$ on both), $M_{1\wedge\rho}(T)=1.60$, $M_{2\wedge\rho}(TH)=1.60$, $M_{2\wedge\rho}(TT)=0.64$ — this destroys the martingale property: $\tilde{\mathbb{E}}_1[M_{2\wedge\rho}](H)=\frac12(4)+\frac12(4)=4 < M_1(H)=6.40$, a downward bias caused by $\rho$ looking ahead and stopping right before an up-move.
  For the discounted American put price $Y_n=(4/5)^nv_n(S_n)$ of Figure 4.2.3 ($Y_0=1.36$; $Y_1(H)=0.32$, $Y_1(T)=2.40$; $Y_2(HH)=0$, $Y_2(HT)=Y_2(TH)=0.64$, $Y_2(TT)=2.56$), which is a supermartingale but not a martingale under $\tilde p=\tilde q=1/2$ — at the tail node, $\tilde{\mathbb{E}}_1[Y_2](T)=\frac12(0.64)+\frac12(2.56)=1.60 < Y_1(T)=2.40$, a strict inequality exactly at the node where early exercise is optimal — stopping it at $\tau$ gives $Y_{2\wedge\tau}(HH)=0$, $Y_{2\wedge\tau}(HT)=0.64$, $Y_{2\wedge\tau}(TH)=Y_{2\wedge\tau}(TT)=2.40$ (frozen at $Y_1(T)$), and now $\tilde{\mathbb{E}}_1[Y_{2\wedge\tau}](T)=\frac12(2.40)+\frac12(2.40)=2.40=Y_{1\wedge\tau}(T)$ — the stopped process is a martingale. The book notes this is a general fact: a discounted American price is always a supermartingale under the risk-neutral probabilities, but stopping it at the optimal exercise time turns it into a martingale.
* **Exercise 4.4:** the American put of Example 4.2.1 (strike $5$) is sold to a buyer with inside information who follows $\rho$, receiving the payoff $Y(HH)=1$, $Y(HT)=1$, $Y(TH)=3$, $Y(TT)=4$ (4.8.1). Its risk-neutral discounted expected value is $\tilde{\mathbb{E}}\big[(4/5)^\rho Y\big]=\frac14(1)+\frac14(1)+\frac14\cdot\frac45(3)+\frac14\cdot\frac{16}{25}(4)=1.74$ (4.8.2) — strictly more than the $1.36$ price computed in Example 4.2.1. The exercise asks whether the seller needs to charge the insider more than $1.36$ to hedge the resulting short position, and why.

## 7. Cross-references

* **Definition 2.4.1 (Chapter 2, pp. 36-37):** the definitions of martingale, supermartingale, and submartingale that stopping times act on here.
* **Theorem 4.2.2 and Example 4.2.1 (Section 4.2, pp. 91-95):** the non-path-dependent American put algorithm whose discounted price process $Y_n=(1+r)^{-n}v_n(S_n)$ is the supermartingale stopped in this section.
* **Theorem 4.4.5 (Section 4.4, p. 109):** the optimal exercise theorem, which shows the optimal exercise rule is precisely the stopping time $\tau^*=\min\{n:V_n=G_n\}$ — the general version of the specific $\tau$ used as the illustration here.