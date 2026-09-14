## 1. Concept and context

Section 4.2 restricted the intrinsic value of an American derivative to functions $g(S_n)$ depending only on the current stock price. Section 4.4 removes that restriction: the intrinsic value $G_n$ may now depend on the entire path $\omega_1\dots\omega_n$ (p. 101). To price such a security we must consider, from the owner's perspective, every possible exercise decision she could make from time $n$ onward — a stopping time in the set $\mathcal S_n$ of all stopping times taking values in $\{n,n+1,\dots,N,\infty\}$. The price $V_n$ is defined as the largest risk-neutral discounted expected payoff achievable over all such stopping times.

## 2. Formal definitions

* **$\mathcal S_n$**: the set of all stopping times $\tau$ taking values in $\{n,n+1,\dots,N,\infty\}$; $\mathcal S_0$ contains every stopping time in the model, and a stopping time in $\mathcal S_N$ can only take the values $N$ or $\infty$.
* **Definition 4.4.1**: for each $n=0,1,\dots,N$, let $G_n$ be a random variable depending on the first $n$ coin tosses. An American derivative security with intrinsic value process $G_n$ is a contract that can be exercised at any time up to and including $N$, paying $G_n$ if exercised at time $n$. Its price process is given by the American risk-neutral pricing formula

$$V_n=\max_{\tau\in\mathcal S_n}\tilde{\mathbb E}_n\Big[\mathbb 1_{\{\tau\le N\}}\Big(\frac1{1+r}\Big)^{\tau-n}G_\tau\Big], \quad n=0,1,\dots,N \quad \text{(4.4.1)}$$

## 3. Key equations

$$V_N=\max_{\tau\in\mathcal S_N}\tilde{\mathbb E}_N\Big[\mathbb 1_{\{\tau\le N\}}\Big(\frac1{1+r}\Big)^{\tau-N}G_\tau\Big]=\max\{G_N,0\} \quad \text{(4.4.2)}$$

$$V_1(H)=\max_{\tau\in\mathcal S_1}\tilde{\mathbb E}_1\Big[\mathbb 1_{\{\tau\le2\}}\Big(\frac45\Big)^{\tau-1}G_\tau\Big](H) \quad \text{(4.4.3)}$$

$$V_1(T)=\max_{\tau\in\mathcal S_1}\tilde{\mathbb E}_1\Big[\mathbb 1_{\{\tau\le2\}}\Big(\frac45\Big)^{\tau-1}G_\tau\Big](T) \quad \text{(4.4.4)}$$

$$V_0=\max_{\tau\in\mathcal S_0}\tilde{\mathbb E}\Big[\mathbb 1_{\{\tau\le2\}}\Big(\frac45\Big)^\tau G_\tau\Big] \quad \text{(4.4.5)}$$

$$\tau(HH)=\infty,\ \tau(HT)=2,\ \tau(TH)=1,\ \tau(TT)=1 \quad \text{(4.4.6)}$$

$$V_0=\tfrac14(0)+\tfrac14\big(\tfrac45\big)^2G_2(HT)+\tfrac12\big(\tfrac45\big)G_1(T)=\tfrac14\cdot\tfrac{16}{25}\cdot1+\tfrac12\cdot\tfrac45\cdot3=1.36 \quad \text{(4.4.7)}$$

$$V_{n+1}=\tilde{\mathbb E}_{n+1}\Big[\mathbb 1_{\{\tau^*\le N\}}\Big(\frac1{1+r}\Big)^{\tau^*-(n+1)}G_{\tau^*}\Big], \quad \tau^*\in\mathcal S_{n+1}\text{ attaining the max} \quad \text{(4.4.8)}$$

$$V_n\ge\tilde{\mathbb E}_n\Big[\frac1{1+r}V_{n+1}\Big] \quad \text{(4.4.9)}$$

$$V_N(\omega_1\dots\omega_N)=\max\{G_N(\omega_1\dots\omega_N),0\} \quad \text{(4.4.10)}$$

$$V_n(\omega_1\dots\omega_n)=\max\Big\{G_n(\omega_1\dots\omega_n),\ \frac1{1+r}\big[\tilde pV_{n+1}(\dots H)+\tilde qV_{n+1}(\dots T)\big]\Big\}, \quad n=N-1,\dots,0 \quad \text{(4.4.11)}$$

$$V_n(\omega_1\dots\omega_n)\ge\frac1{1+r}\big[\tilde pV_{n+1}(\dots H)+\tilde qV_{n+1}(\dots T)\big]=\tilde{\mathbb E}_n\Big[\frac1{1+r}V_{n+1}\Big](\omega_1\dots\omega_n) \quad \text{(4.4.12)}$$

$$V_n(\omega_1\dots\omega_n)\ge\max\Big\{G_n(\omega_1\dots\omega_n),\ \frac1{1+r}\big[\tilde pV_{n+1}(\dots H)+\tilde qV_{n+1}(\dots T)\big]\Big\} \quad \text{(4.4.13)}$$

$$\Delta_n(\omega_1\dots\omega_n)=\frac{V_{n+1}(\dots H)-V_{n+1}(\dots T)}{S_{n+1}(\dots H)-S_{n+1}(\dots T)} \quad \text{(4.4.14)}$$

$$C_n(\omega_1\dots\omega_n)=V_n(\omega_1\dots\omega_n)-\frac1{1+r}\big[\tilde pV_{n+1}(\dots H)+\tilde qV_{n+1}(\dots T)\big] \quad \text{(4.4.15)}$$

$$X_{n+1}=\Delta_nS_{n+1}+(1+r)(X_n-C_n-\Delta_nS_n) \quad \text{(4.4.16)}$$

$$X_n(\omega_1\dots\omega_n)=V_n(\omega_1\dots\omega_n) \quad \text{(4.4.17)}$$

$$X_{n+1}(\omega_1\dots\omega_nH)=V_{n+1}(\omega_1\dots\omega_nH) \quad \text{(4.4.18)}$$

$$X_{n+1}(\omega_1\dots\omega_nT)=V_{n+1}(\omega_1\dots\omega_nT) \quad \text{(4.4.19)}$$

$$V_n=\tilde{\mathbb E}_n\Big[\mathbb 1_{\{\tau^*\le N\}}\Big(\frac1{1+r}\Big)^{\tau^*-n}G_{\tau^*}\Big] \quad \text{(4.4.20)}$$

$$\tau^*=\min\{n:V_n=G_n\} \quad \text{(4.4.21)}$$

$$V_0=\tilde{\mathbb E}\Big[\mathbb 1_{\{\tau^*\le N\}}\Big(\frac1{1+r}\Big)^{\tau^*}G_{\tau^*}\Big] \quad \text{(4.4.22)}$$

$$\Big(\frac1{1+r}\Big)^{n\wedge\tau^*}V_{n\wedge\tau^*} \quad \text{(4.4.23)}$$

$$V_0=\tilde{\mathbb E}\Big[\Big(\frac1{1+r}\Big)^{N\wedge\tau^*}V_{N\wedge\tau^*}\Big]=\tilde{\mathbb E}\Big[\mathbb 1_{\{\tau^*\le N\}}\Big(\frac1{1+r}\Big)^{\tau^*}G_{\tau^*}\Big]+\tilde{\mathbb E}\Big[\mathbb 1_{\{\tau^*=\infty\}}\Big(\frac1{1+r}\Big)^NV_N\Big] \quad \text{(4.4.24)}$$

$$V_0=\tilde{\mathbb E}\Big[\mathbb 1_{\{\tau^*\le N\}}\Big(\frac1{1+r}\Big)^{\tau^*}G_{\tau^*}\Big] \quad \text{(4.4.25)}$$

*Unnumbered:* dividing both sides of (4.4.9) by $(1+r)^n$ gives the discounted supermartingale property $\big(\frac1{1+r}\big)^nV_n\ge\tilde{\mathbb E}_n\big[\big(\frac1{1+r}\big)^{n+1}V_{n+1}\big]$ right after (4.4.9), with no number of its own. The cash flows $C_k=\mathbb 1_{\{\tau^*=k\}}G_k$ used in (4.4.20) are likewise unnumbered.

## 4. Assumptions and domain of validity

* **No-arbitrage condition:** $0<d<1+r<u$, as always, giving $0<\tilde p,\tilde q<1$.
* **Adaptedness of $G_n$:** each $G_n$ depends only on the first $n$ coin tosses.
* **Stopping-time restriction:** the maximization in (4.4.1) ranges only over genuine stopping times in $\mathcal S_n$; look-ahead rules are excluded.

## 5. Theorems and proof outline

**Theorem 4.4.2 (three defining properties of $V_n$):** the price process of Definition 4.4.1 satisfies (i) $V_n\ge\max\{G_n,0\}$ for all $n$; (ii) the discounted process $\big(\frac1{1+r}\big)^nV_n$ is a supermartingale; (iii) if $Y_n$ is any other process satisfying (i) and (ii), then $Y_n\ge V_n$ for all $n$ — i.e. $V_n$ is the *smallest* process with these two properties.

*Proof outline:*
1. **(i):** taking $\tau=n\in\mathcal S_n$ in (4.4.1) gives $\tilde{\mathbb E}_n[\mathbb 1_{\{n\le N\}}G_n]=G_n$, so $V_n\ge G_n$; taking $\tau=\infty$ gives $0$, so $V_n\ge0$. Together, $V_n\ge\max\{G_n,0\}$.
2. **(ii):** for any $\tau\in\mathcal S_{n+1}\subset\mathcal S_n$, (4.4.1) gives $V_n\ge\tilde{\mathbb E}_n\big[\frac1{1+r}\tilde{\mathbb E}_{n+1}[\dots]\big]$; letting $\tau$ attain the maximum defining $V_{n+1}$ (4.4.8) and taking the supremum inside yields the one-step relation $V_n\ge\tilde{\mathbb E}_n\big[\frac1{1+r}V_{n+1}\big]$ (4.4.9). Dividing by $(1+r)^n$ gives the discounted supermartingale property.
3. **(iii):** let $Y_n$ satisfy (i) and (ii), and fix any $\tau\in\mathcal S_n$. Since $Y_k\ge\max\{G_k,0\}$, we have $\mathbb 1_{\{\tau\le N\}}G_\tau\le Y_{N\wedge\tau}$; combining this with the Optional Sampling Theorem (4.3.2) and the supermartingale property of $(1+r)^{-k}Y_k$ gives $\tilde{\mathbb E}_n\big[\mathbb 1_{\{\tau\le N\}}(1+r)^{-\tau}G_\tau\big]\le(1+r)^{-n}Y_n$. Multiplying by $(1+r)^n$ and maximizing over $\tau\in\mathcal S_n$ gives $V_n\le Y_n$.

**Theorem 4.4.3 (general American pricing algorithm):** $V_n$ can equivalently be computed by the backward recursion (4.4.10)-(4.4.11).

*Proof outline:* by backward induction, using (4.4.11) and the induction hypothesis $V_{n+1}\ge\max\{G_{n+1},0\}$, one shows $V_n\ge\max\{G_n,0\}$ — establishing property (i) of Theorem 4.4.2. Equation (4.4.11) directly gives the supermartingale inequality (4.4.12), establishing property (ii). For minimality, any process satisfying (i) and (ii) must satisfy (4.4.13) at every node, which is exactly what (4.4.11) defines as the smallest possible value — so the recursively defined $V_n$ coincides with the $V_n$ of Definition 4.4.1, which Theorem 4.4.2 already showed is unique with these two properties.

**Theorem 4.4.4 (replication of path-dependent American derivatives):** with $\Delta_n$ and $C_n$ given by (4.4.14)-(4.4.15), $C_n\ge0$ for all $n$ (a consequence of (4.4.12)), and if $X_0=V_0$ with $X_1,\dots,X_N$ generated forward by (4.4.16), then $X_n=V_n$ for all $n$ and all paths — in particular $X_n\ge G_n$.

*Proof outline:* $C_n\ge0$ follows directly from (4.4.12). The replication identity is proved by forward induction exactly as in Theorem 2.4.8 of Chapter 2: assuming $X_n=V_n$, substituting the wealth recursion (4.4.16), the definitions of $\Delta_n$ (4.4.14) and $C_n$ (4.4.15), and simplifying algebraically yields $X_{n+1}(H)=V_{n+1}(H)$ (4.4.18) and $X_{n+1}(T)=V_{n+1}(T)$ (4.4.19).

**Theorem 4.4.5 (optimal exercise):** the stopping time $\tau^*=\min\{n:V_n=G_n\}$ (4.4.21) maximizes the right-hand side of (4.4.1) at $n=0$, i.e. (4.4.22) holds.

*Proof outline:* the stopped process $(1+r)^{-(n\wedge\tau^*)}V_{n\wedge\tau^*}$ (4.4.23) is a martingale under $\tilde{\mathbb P}$ — on paths where $\tau^*\ge n+1$ this follows from (4.4.11) since $V_n$ still equals its continuation value there; on paths where $\tau^*\le n$ the process is already frozen. Applying the martingale property between times $0$ and $N$ gives the split (4.4.24). On paths where $\tau^*=\infty$, $V_N>G_N$ forces $G_N<0$ and hence $V_N=0$ by (4.4.10), so that term vanishes, leaving (4.4.25) — which is exactly (4.4.22).

## 6. Exercises in this section (and required examples)

* **Example 4.2.1 continued:** re-deriving the two-period American put ($N=2$, $S_0=4$, $u=2$, $d=1/2$, $r=1/4$, strike $5$) directly from Definition 4.4.1 rather than the Section 4.2 recursion. Intrinsic values: $G_0=1$, $G_1(H)=-3$, $G_1(T)=3$, $G_2(HH)=-11$, $G_2(HT)=G_2(TH)=1$, $G_2(TT)=4$. $V_2=\max\{G_2,0\}$ gives $V_2(HH)=0$, $V_2(HT)=V_2(TH)=1$, $V_2(TT)=4$. By (4.4.3), $V_1(H)=0.40$, achieved by $\tau(HH)=\infty,\tau(HT)=2$ (never exercising on $HH$, exercising at $2$ on $HT$); by (4.4.4), $V_1(T)=3$, achieved by exercising immediately at $\tau(TH)=\tau(TT)=1$. By (4.4.5), $V_0=1.36$ (4.4.7), achieved by the stopping time (4.4.6) — matching $v_n(S_n)$ from Section 4.2 exactly, as it must.
* **Exercise 4.3 (path-dependent American security on the running average):** in the three-period model of Figure 1.2.2 ($S_0=4$, $u=2$, $d=1/2$, $r=1/4$), find the time-zero price and optimal exercise policy for the American security whose intrinsic value at each time $n$ is $\big(4-\frac1{n+1}\sum_{j=0}^nS_j\big)^+$ — a put on the running average price. The book gives no numeric answer here; solving it requires applying Theorem 4.4.3 over the two-dimensional state $(S_n,Y_n)$ with $Y_n=\sum_{j=0}^nS_j$, reusing the cumulative-sum technique of Exercise 1.8 of Chapter 1.
* **Exercise 4.5:** in (4.4.5), the maximum ranges over all stopping times in $\mathcal S_0$ — there are $26$ of them. List the $11$ that never exercise while out of the money, compute $\tilde{\mathbb E}\big[\mathbb 1_{\{\tau\le2\}}(4/5)^\tau G_\tau\big]$ for each, and verify the largest is the one in (4.4.6), giving $1.36$.
* **Exercise 4.6:** consider the class of securities priced by (4.8.3), which restricts the maximization to $\tau\in\{0,\dots,N\}$ (excluding $\infty$).
  (i) with $G_n=K-S_n$, show the optimal policy is to exercise at time zero and the value is $K-S_0$.
  (ii) explain why a portfolio holding this security plus a European call struck at $K$ is at least as valuable as an American put struck at $K$, and conclude the upper bound $V_0^{AP}\le V_0^{EC}+K-S_0$ (4.8.4).
  (iii) use put-call parity (Exercise 2.11, Chapter 2) to derive the lower bound $V_0^{EC}-S_0+\dfrac{K}{(1+r)^N}\le V_0^{AP}$ (4.8.5).
* **Exercise 4.7:** for the same class of securities as Exercise 4.6, with $G_n=S_n-K$ instead (a security letting its owner buy a share for $K$ at any time up to $N$, or at $N$ if not exercised earlier), determine the time-zero value and optimal exercise policy. The book gives no answer here; it is a problem for the reader.

## 7. Cross-references

* **Theorem 1.2.2 (Chapter 1, p. 11):** the replication algorithm generalized by Theorem 4.4.4.
* **Exercise 1.8 (Chapter 1, p. 22):** the running-sum state variable $Y_n$ reused in Exercise 4.3.
* **Theorem 2.4.8 (Chapter 2, p. 42):** cash flow valuation, the model for interpreting (4.4.20) and for the proof of Theorem 4.4.4.
* **Definition 4.3.1 and Theorem 4.3.2 (Section 4.3):** the stopping-time machinery this whole section is built on, used directly in the proofs of Theorems 4.4.2(iii) and 4.4.5.
* **Theorem 4.5.1 (Section 4.5):** the corollary showing early exercise is worthless for calls, a special case answering the spirit of Exercise 4.7.