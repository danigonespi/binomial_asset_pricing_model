## 1. Concept and context

We saw in Example 4.2.1 that early exercise of an American put can be strictly optimal. For an American call on a non-dividend-paying stock, by contrast, there is no advantage to early exercise at all — the early exercise premium is exactly zero, a consequence of Jensen's inequality for conditional expectations (p. 111). Intuitively: exercising a call early at $S_n-K$ surrenders the option's remaining time value and forces the holder to pay $K$ sooner than necessary, forfeiting interest on it until $N$; holding the option also insures against $S$ falling below $K$ later. For a put, the logic reverses — the holder *receives* $K$ upon exercise, so exercising early lets her start earning interest on that $K$ immediately, an effect that can dominate the convexity effect when the stock price is low enough (as it did at $n=1$, $S_1=2$, in Example 4.2.1).

## 2. Formal definitions

* **$g$**: a convex function on $[0,\infty)$ satisfying $g(0)=0$ (Figure 4.5.1). The book's own example is $g(s)=(s-K)^+$, the payoff of a call struck at $K$ — already nonnegative and satisfying $g(0)=0$ directly.
* **$g_+(s)=\max\{g(s),0\}$**: an auxiliary function introduced in the proof (not separately numbered). It is needed because the theorem's hypothesis only requires $g(0)=0$, which does not by itself guarantee $g\ge0$ everywhere for a general such $g$ — $g_+$ is the nonnegative floor of $g$, and inherits convexity from $g$.
* **$\hat V_0$**: the American derivative security's time-zero price (Definition 4.4.1).
* **$V_0^E$**: the corresponding European derivative security's time-zero price (Theorem 2.4.7 of Chapter 2).

## 3. Key equations

$$g(\lambda s_1+(1-\lambda)s_2)\le\lambda g(s_1)+(1-\lambda)g(s_2), \quad s_1,s_2\ge0,\ \lambda\in[0,1] \quad \text{(4.5.1)}$$

$$\hat V_0=\max_{\tau\in\mathcal S_0}\tilde{\mathbb E}\Big[\mathbb 1_{\{\tau\le N\}}\Big(\frac1{1+r}\Big)^\tau g(S_\tau)\Big] \quad \text{(4.5.2)}$$

$$V_0^E=\tilde{\mathbb E}\Big[\Big(\frac1{1+r}\Big)^N\max\{g(S_N),0\}\Big] \quad \text{(4.5.3)}$$

$$g_+(\lambda s)\le\lambda g_+(s), \quad \lambda\in[0,1],\ s\ge0 \quad \text{(4.5.4)}$$

$$g_+\Big(\tilde{\mathbb E}_n\Big[\frac{S_{n+1}}{1+r}\Big]\Big)\le\tilde{\mathbb E}_n\Big[g_+\Big(\frac{S_{n+1}}{1+r}\Big)\Big] \quad \text{(4.5.5)}$$

$$g_+\Big(\frac{S_{n+1}}{1+r}\Big)\le\frac1{1+r}g_+(S_{n+1}) \quad \text{(4.5.6)}$$

$$\tilde{\mathbb E}\Big[\Big(\frac1{1+r}\Big)^{N\wedge\tau}g_+(S_{N\wedge\tau})\Big]\le\tilde{\mathbb E}\Big[\Big(\frac1{1+r}\Big)^Ng_+(S_N)\Big]=V_0^E, \quad \tau\in\mathcal S_0 \quad \text{(4.5.7)}$$

*Unnumbered:* the definition $g_+(s)=\max\{g(s),0\}$; the intermediate combined bound $g_+(S_n)\le\tilde{\mathbb E}_n\big[g_+(S_{n+1}/(1+r))\big]\le\frac1{1+r}\tilde{\mathbb E}_n[g_+(S_{n+1})]$ obtained by chaining (4.5.5) and (4.5.6), whose $(1+r)^n$-multiplied form gives the discounted submartingale property; and the final chain of inequalities, splitting on $\tau\le N$ vs. $\tau=\infty$, that reduces (4.5.7) to $\tilde{\mathbb E}[\mathbb 1_{\{\tau\le N\}}(1+r)^{-\tau}g(S_\tau)]\le V_0^E$.

## 4. Assumptions and domain of validity

* **Convexity and zero intercept:** $g$ convex on $[0,\infty)$ with $g(0)=0$.
* **Non-negative interest rate:** $r\ge0$ — needed for (4.5.4) to scale the right way; if $r<0$ then $(1+r)s<s$ and the inequality direction breaks.
* **Standing no-arbitrage condition:** $0<d<1+r<u$.
* **Why the argument does not apply to puts:** for a put, $g(s)=K-s$ has $g(0)=K\ne0$, so the theorem's hypothesis fails outright — puts are simply outside its scope. As an illustrative aside (not a counterexample within the theorem's domain), the book checks what happens to the proof's own inequalities if one substitutes the put's $g_+(s)=(K-s)^+$ anyway: the conditional Jensen step (4.5.5) still holds (since $(K-s)^+$ is itself convex), but the scaling step (4.5.6) fails — shrinking $s$ toward $0$ *increases* $(K-s)^+$, so $g_+(S_{n+1}/(1+r)) > \frac1{1+r}g_+(S_{n+1})$ rather than $\le$. This is exactly why the discounted intrinsic value of a put is not a submartingale, and why early exercise can be optimal for puts but never for calls.

## 5. Theorems and proof outline

**Theorem 4.5.1 (American call price = European call price):** consider an $N$-period binomial model with $0<d<1+r<u$ and $r\ge0$, and an American derivative security with convex payoff $g(s)$ satisfying $g(0)=0$. Then its time-zero price $\hat V_0$ (4.5.2) equals the time-zero price $V_0^E$ (4.5.3) of the corresponding European security paying $g(S_N)$ at expiration.

*Proof outline:*
1. Since $g$ may take negative values, introduce $g_+(s)=\max\{g(s),0\}$, which is nonnegative, satisfies $g_+(0)=0$, and — because $g$ satisfies (4.5.1) and $g(0)=0$ — is itself convex.
2. Setting $s_2=0$ in the convexity inequality for $g_+$ gives $g_+(\lambda s)\le\lambda g_+(s)$ for all $\lambda\in[0,1]$, $s\ge0$ (4.5.4).
3. Because $(1+r)^{-n}S_n$ is a martingale under the risk-neutral measure, $S_n=\tilde{\mathbb E}_n[S_{n+1}/(1+r)]$; the conditional Jensen's inequality of Theorem 2.3.2(v) of Chapter 2, applied to the convex $g_+$, gives (4.5.5).
4. Taking $\lambda=1/(1+r)$ in (4.5.4) gives (4.5.6).
5. Chaining (4.5.5) and (4.5.6) gives $g_+(S_n)\le\frac1{1+r}\tilde{\mathbb E}_n[g_+(S_{n+1})]$; multiplying by $(1+r)^n$ shows that the discounted intrinsic value process $(1+r)^{-n}g_+(S_n)$ is a submartingale under the risk-neutral measure.
6. Because this process is a submartingale, the Optional Sampling Theorem (4.3.3) gives (4.5.7) for every stopping time $\tau\in\mathcal S_0$.
7. Splitting on whether $\tau\le N$ or $\tau=\infty$ reduces (4.5.7) to $\tilde{\mathbb E}\big[\mathbb 1_{\{\tau\le N\}}(1+r)^{-\tau}g(S_\tau)\big]\le V_0^E$ for every such $\tau$; taking the maximum over $\tau\in\mathcal S_0$ gives $\hat V_0\le V_0^E$. Since choosing $\tau=N$ — exercising only on the paths where $g(S_N)>0$, and letting the option expire otherwise — is itself an admissible element of $\mathcal S_0$ and exactly reproduces the European payoff, $\hat V_0\ge V_0^E$ trivially. Together, $\hat V_0=V_0^E$.

## 6. Exercises in this section

No exercise in Section 4.8 maps specifically to this theorem. Exercise 4.1(ii) computes an American call's price via the general algorithm of Section 4.2, but it does not test the convexity/no-early-exercise argument of this section itself.

## 7. Cross-references

* **Theorem 2.3.2(v) (Chapter 2, p. 34):** the conditional Jensen's inequality used directly in step 3, (4.5.5).
* **Theorem 4.3.3 (Section 4.3, p. 100):** the Optional Sampling Theorem for submartingales, used directly in step 6, (4.5.7).
* **Theorem 2.4.7 (Chapter 2):** the European risk-neutral pricing formula underlying $V_0^E$, (4.5.3).
* **Example 4.2.1 (Section 4.2, pp. 91-95):** the American put whose early exercise at $n=1$, $S_1=2$, is the concrete counterexample showing why this theorem's conclusion does not extend to puts.