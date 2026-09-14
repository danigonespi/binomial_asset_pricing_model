## 1. Concept and context

European options can be exercised only at the expiration date $N$; American options let the owner exercise at any time $n$ with $0 \le n \le N$; Bermudan options sit in between, permitting early exercise but only on a contractually specified finite subset of dates (p. 89). Because the American holder has strictly more freedom, an American option is worth at least as much as its European counterpart — the extra value is the early exercise premium. This premium is zero for a call on a non-dividend-paying stock (American and European calls have the same price, proved later in Theorem 4.5.1) but can be substantial for puts (p. 89). Section 4.2 develops the pricing algorithm for the simplest case: the intrinsic value $g(S_n)$ depends only on the current stock price $S_n$, not on the path $\omega_1\dots\omega_n$ that produced it (p. 90). Because the stock price is itself Markov, this lets the price at every time be written as a deterministic function $v_n(s)$ of the current price alone (Theorem 2.5.8 of Chapter 2), exactly as in the European case — only the recursion itself changes.

## 2. Formal definitions

* **$g(s)$**: intrinsic value / payoff function, giving the cash received on immediate exercise when the stock price is $s$.
* **$v_n(s)$**: deterministic pricing function at time $n$; the derivative security's price process is $V_n = v_n(S_n)$.
* **$X_n$**: value at time $n$ of the seller's replicating (hedging) portfolio.
* **$\Delta_n$**: number of shares held in the replicating portfolio from time $n$ to $n+1$.
* **$C_n$**: nonnegative consumption (cash withdrawn) by the hedger at time $n$.
* **$u,d,r$**: up factor, down factor, per-period interest rate.
* **$\tilde p,\tilde q$**: risk-neutral probabilities, $\tilde p=\frac{1+r-d}{u-d}$, $\tilde q=\frac{u-1-r}{u-d}$.

## 3. Key equations

$$v_N(s)=\max\{g(s),0\} \quad \text{(4.2.1)}$$

$$v_n(s)=\frac{1}{1+r}\big[\tilde p\,v_{n+1}(us)+\tilde q\,v_{n+1}(ds)\big], \quad n=N-1,\dots,0 \quad \text{(4.2.2)}$$

$$\Delta_n=\frac{v_{n+1}(uS_n)-v_{n+1}(dS_n)}{(u-d)S_n} \quad \text{(4.2.3)}$$

$$X_n \ge g(S_n), \quad n=0,1,\dots,N \quad \text{(4.2.4)}$$

$$v_N(s)=\max\{g(s),0\} \quad \text{(4.2.5)}$$

$$v_n(s)=\max\Big\{g(s),\ \frac{1}{1+r}\big[\tilde p\,v_{n+1}(us)+\tilde q\,v_{n+1}(ds)\big]\Big\}, \quad n=N-1,\dots,0 \quad \text{(4.2.6)}$$

$$\Delta_n=\frac{v_{n+1}(uS_n)-v_{n+1}(dS_n)}{(u-d)S_n} \quad \text{(4.2.7)}$$

$$C_n=v_n(S_n)-\frac{1}{1+r}\big[\tilde p\,v_{n+1}(uS_n)+\tilde q\,v_{n+1}(dS_n)\big] \quad \text{(4.2.8)}$$

$$X_{n+1}=\Delta_nS_{n+1}+(1+r)(X_n-C_n-\Delta_nS_n) \quad \text{(4.2.9)}$$

$$X_n(\omega_1\dots\omega_n)=v_n(S_n(\omega_1\dots\omega_n)) \quad \text{(4.2.10)}$$

*Unnumbered formulas:* the risk-neutral probabilities $\tilde p=\frac{1+r-d}{u-d}$, $\tilde q=\frac{u-1-r}{u-d}$ are restated right after (4.2.2); the relation $V_n=v_n(S_n)$ appears right after (4.2.6); and the consumption non-negativity fact $v_n(S_n)\ge\frac{1}{1+r}[\tilde p\,v_{n+1}(uS_n)+\tilde q\,v_{n+1}(dS_n)]$ is stated right after Theorem 4.2.2, following directly from (4.2.6).

Note that (4.2.1) and (4.2.5) — and likewise (4.2.3) and (4.2.7) — are *identical* formulas; the book assigns them separate numbers because (4.2.1)-(4.2.3) are introduced while reviewing the European algorithm, and (4.2.5)-(4.2.7) restate them as part of the American algorithm proper.

## 4. Assumptions and domain of validity

* **No-arbitrage condition:** $0<d<1+r<u$, guaranteeing $0<\tilde p,\tilde q<1$.
* **Path-independence:** $g(S_n)$ depends only on the current price $S_n$, not on $S_0,\dots,S_{n-1}$ — this is what lets the price collapse to a function $v_n(s)$ of a single state variable rather than the full path.
* **Non-negativity of consumption:** $C_n\ge0$ for all $n$, guaranteed by construction since $v_n(s)\ge\frac{1}{1+r}[\tilde p\,v_{n+1}(us)+\tilde q\,v_{n+1}(ds)]$ by (4.2.6).

## 5. Theorems and proof outline

**Theorem 4.2.2 (Replication of path-independent American derivatives):** Consider an $N$-period binomial model with $0<d<1+r<u$. Given a payoff function $g(s)$, define $v_N,v_{N-1},\dots,v_0$ recursively backward by (4.2.5)-(4.2.6), and define $\Delta_n$ and $C_n$ by (4.2.7) and (4.2.8). Then $C_n\ge0$ for all $n$, and if $X_0=v_0(S_0)$ with $X_1,\dots,X_N$ generated forward by (4.2.9), then $X_n(\omega_1\dots\omega_n)=v_n(S_n(\omega_1\dots\omega_n))$ for all $n$ and all paths; in particular $X_n\ge g(S_n)$ for all $n$.

*Proof outline:* the book does not prove this theorem here. It states explicitly, right before the theorem, that it defers the proof to the more general Theorems 4.4.3 and 4.4.4 of Section 4.4, which establish the analogous algorithm and replication result for path-dependent (and therefore also path-independent) American derivatives.

## 6. Exercises in this section (and required examples)

* **Example 4.2.1 (two-period American put):** In the two-period model of Figure 4.2.1 with $S_0=4$, $u=2$, $d=1/2$, $r=1/4$ (so $\tilde p=\tilde q=1/2$), consider an American put struck at $5$, so $g(s)=5-s$. Terminal values: $v_2(16)=0$, $v_2(4)=1$, $v_2(1)=4$. At $n=1$: $v_1(8)=\max\{5-8,\ \frac45[\frac12(0)+\frac12(1)]\}=\max\{-3,0.40\}=0.40$; $v_1(2)=\max\{5-2,\ \frac45[\frac12(1)+\frac12(4)]\}=\max\{3,2.00\}=3$ — here early exercise is strictly optimal, since the continuation value ($2.00$) is below the intrinsic value ($3$). At $n=0$: $v_0(4)=\max\{5-4,\ \frac45[\frac12(0.40)+\frac12(3)]\}=\max\{1,1.36\}=1.36$. Replicating the portfolio: $\Delta_0=\frac{v_1(8)-v_1(2)}{8-2}=\frac{0.40-3}{6}\approx-0.43$. On the head branch, $X_1(H)=0.40$ and $\Delta_1(H)=\frac{v_2(16)-v_2(4)}{16-4}=-\frac1{12}$, which exactly replicates $X_2(HH)=0=v_2(16)$ and $X_2(HT)=1=v_2(4)$ with no consumption needed. On the tail branch, $X_1(T)=v_1(2)=3$, but the risk-neutral continuation value there is only $\frac45[\frac12(1)+\frac12(4)]=2$, so the hedger consumes $C_1(T)=3-2=1$ and continues hedging the remaining $2$ with $\Delta_1(T)=\frac{v_2(4)-v_2(1)}{4-1}=-1$. The book also notes that the resulting discounted American put price process (Figure 4.2.3) is a supermartingale but not a martingale under $\tilde p=\tilde q=1/2$ — the inequality is strict exactly at the tail node at time one, the node where early exercise turns out to be optimal.
* **Exercise 4.1:** In the three-period model of Figure 1.2.2 of Chapter 1 ($S_0=4$, $u=2$, $d=1/2$, $r=1/4$, so $\tilde p=\tilde q=1/2$):
  (i) find $V_0^P$, the price of the American put expiring at $N=3$ with $g_P(s)=(4-s)^+$;
  (ii) find $V_0^C$, the price of the American call expiring at $N=3$ with $g_C(s)=(s-4)^+$;
  (iii) find $V_0^S$, the price of the American straddle with $g_S(s)=g_P(s)+g_C(s)$;
  (iv) explain why $V_0^S < V_0^P+V_0^C$.
* **Exercise 4.2:** In Example 4.2.1 the time-zero value of the American put struck at $5$ was found to be $1.36$. Consider an agent who borrows $1.36$ at time zero and buys the put. Explain how, by trading in the stock and money market and exercising optimally, this agent can generate enough funds to repay the loan (which grows $25\%$ each period).

## 7. Cross-references

* **Theorem 1.2.2 (Chapter 1, p. 11):** the multiperiod European replication algorithm and wealth equation (1.2.14), which (4.2.9) generalizes by adding the nonnegative consumption process $C_n$.
* **Theorem 2.5.8 (Chapter 2, p. 52):** Markov pricing functions $V_n=v_n(X_n)$, the theoretical basis for representing the American price as a function $v_n(s)$ of the current stock price alone.
* **Theorems 4.4.3 and 4.4.4 (Section 4.4, pp. 106-107):** the general path-dependent American pricing algorithm and replication theorem, which this section's Theorem 4.2.2 is a special case of and whose proof supplies the one missing here.