## 1. Concept and context

Chapter 6 develops a simple binomial model for interest rates and examines assets whose value depends on interest rates, called *fixed income* assets (Section 6.1, p. 143). The simplest one is the zero-coupon bond, which pays its face value at maturity; since there is a zero-coupon bond for every maturity, there is a yield for every maturity, and models that describe the random evolution of the whole yield curve are called *term structure of interest rates* models. Having so many tradable assets raises the specter of arbitrage, and a model that permits arbitrage gives nonsensical answers to pricing and hedging questions (pp. 143–144). The book avoids the problem by building the model directly under the risk-neutral measure: it first describes the evolution of the interest rate under $\tilde{\mathbb P}$ and then defines the prices of zero-coupon bonds and all other fixed income assets by the risk-neutral pricing formula. This construction guarantees that all discounted asset prices, and hence all discounted portfolio processes, are martingales — Theorem 6.2.6, the main result of Section 6.2 — and martingale discounted portfolio processes are inconsistent with arbitrage (p. 144). Models built this way, starting from the interest rate, are called *short-rate models*; models that start from the whole yield curve are *whole yield models*. Section 6.2 (pp. 144–154) sets up the interest rate process and the discount process, extends conditional expectation to coin tosses that are not independent (Definition 6.2.2), defines zero-coupon bond prices (Definition 6.2.4), proves that discounted wealth is a martingale and that the model is free of arbitrage, and prices coupon-paying bonds.

## 2. Formal definitions

* **$\Omega$, $\tilde{\mathbb P}$**: $\Omega$ is the set of $2^N$ possible outcomes $\omega_1\omega_2\dots\omega_N$ of $N$ coin tosses, and $\tilde{\mathbb P}$ is a probability measure on $\Omega$ under which every sequence $\omega_1\omega_2\dots\omega_N$ has strictly positive probability (p. 144).
* **Interest rate process $R_0,R_1,\dots,R_{N-1}$**: a sequence of random variables where $R_0$ is not random and, for $n=1,\dots,N-1$, $R_n$ depends only on the first $n$ coin tosses $\omega_1\dots\omega_n$. One dollar invested in the money market at time $n$ grows to $1+R_n$ dollars at time $n+1$; at time $n$ the rate for the period from $n$ to $n+1$ is already known (pp. 144–145).
* **Discount process $D_n$**: defined by (6.2.2). $D_n$ depends on only the first $n-1$ coin tosses, contrary to the usual situation in which the subscript indicates the number of coin tosses on which the random variable depends (p. 145).
* **Zero-coupon bond**: a bond that pays a specified amount, its *face value* or *par value*, at a specified time, its *maturity* (p. 143). With face value 1, $B_{n,m}$ denotes the price at time $n$ of the zero-coupon bond maturing at time $m$ (Definition 6.2.4, p. 150); a bond with face value $C$ is worth $CB_{n,m}$.
* **Yield $y_m$**: the number for which $\frac{1}{B_{0,m}}=(1+y_m)^m$ — the constant rate of interest that makes one dollar invested at time zero grow to the payoff $\frac{1}{B_{0,m}}$ of the bonds it buys (p. 145). The *yield curve* is the function from the maturity variable to the yield variable (p. 143).
* **Transition probabilities**: the conditional probabilities $\tilde{\mathbb P}\{\omega_{n+1}=\cdot\mid\omega_1,\dots,\omega_n\}$ of traversing the links of the interest rate tree (Example 6.2.1, p. 148).
* **Conditional expectation $\tilde{\mathbb E}_n[X]$**: the conditional expectation of a random variable $X$ based on the information at time $n$, for a measure $\tilde{\mathbb P}$ under which the coin tosses need not be independent (Definition 6.2.2, p. 150).
* **$\Delta_{n,m}$**: the number of $m$-maturity zero-coupon bonds held by an agent between times $n$ and $n+1$, with $n<m$ and depending only on the first $n$ coin tosses; **$X_n$** is the agent's wealth at time $n$, with nonrandom initial wealth $X_0$ (p. 151).
* **Coupon-paying bond**: a sequence of constant (nonrandom) quantities $C_0,C_1,\dots,C_m$, where $C_n$ ($0\le n\le m-1$) is the coupon paid at time $n$ (possibly zero) and $C_m$ is the payment at time $m$, including principal and any coupon due then. It can be regarded as a sum of $C_1$ zero-coupon bonds maturing at time 1, $C_2$ maturing at time 2, …, $C_m$ maturing at time $m$ (p. 153).

## 3. Key equations

$$R_n(\omega_1\dots\omega_n)>-1 \quad \text{for all } n \text{ and all } \omega_1,\dots,\omega_n \quad \text{(6.2.1)}$$

$$D_n=\frac{1}{(1+R_0)\cdots(1+R_{n-1})},\quad n=1,2,\dots,N;\qquad D_0=1 \quad \text{(6.2.2)}$$

$$B_{0,m}=\tilde{\mathbb E}[D_m] \quad \text{(6.2.3)}$$

$$B_{n,m}=\tilde{\mathbb E}_n\left[\frac{D_m}{D_n}\right],\quad 0\le n\le m\le N \quad \text{(6.2.4)}$$

$$D_nB_{n,m}=\tilde{\mathbb E}_n[D_m] \quad \text{(6.2.5)}$$

$$X_{n+1}=\Delta_{n,n+1}+\sum_{m=n+2}^{N}\Delta_{n,m}B_{n+1,m}+(1+R_n)\left(X_n-\sum_{m=n+1}^{N}\Delta_{n,m}B_{n,m}\right) \quad \text{(6.2.6)}$$

$$\tilde{\mathbb E}[D_nX_n]=X_0,\quad n=0,1,\dots,N \quad \text{(6.2.7)}$$

$$V_n=\frac{1}{D_n}\tilde{\mathbb E}_n[D_mV_m],\quad 0\le n\le m\le N \quad \text{(6.2.8)}$$

$$\sum_{k=n}^{m}C_kB_{n,k}=\tilde{\mathbb E}_n\left[\sum_{k=n}^{m}\frac{C_kD_k}{D_n}\right],\quad n=0,1,\dots,m \quad \text{(6.2.9)}$$

*Unnumbered formulas in the text:*

The time-zero value of a payment $X$ received at time $m$ (where $X$ depends only on $\omega_1\dots\omega_m$), given by the risk-neutral pricing formula as the risk-neutral expected discounted payment (p. 145):

$$\tilde{\mathbb E}[D_mX]$$

The yield of the $m$-maturity zero-coupon bond and its explicit solution (p. 145):

$$\frac{1}{B_{0,m}}=(1+y_m)^m,\qquad y_m=\left(\frac{1}{B_{0,m}}\right)^{\frac1m}-1$$

The conditional probabilities and the conditional expectation of Definition 6.2.2, for $1\le n\le N-1$ and a sequence $\overline\omega_1\dots\overline\omega_N$ (p. 150):

$$\tilde{\mathbb P}\{\omega_{n+1}=\overline\omega_{n+1},\dots,\omega_N=\overline\omega_N\mid\omega_1=\overline\omega_1,\dots,\omega_n=\overline\omega_n\}=\frac{\tilde{\mathbb P}\{\overline\omega_1\dots\overline\omega_n\overline\omega_{n+1}\dots\overline\omega_N\}}{\tilde{\mathbb P}\{\omega_1=\overline\omega_1,\dots,\omega_n=\overline\omega_n\}}$$

$$\tilde{\mathbb E}_n[X](\overline\omega_1\dots\overline\omega_n)=\sum_{\overline\omega_{n+1},\dots,\overline\omega_N}X(\overline\omega_1\dots\overline\omega_n\overline\omega_{n+1}\dots\overline\omega_N)\,\tilde{\mathbb P}\{\omega_{n+1}=\overline\omega_{n+1},\dots,\omega_N=\overline\omega_N\mid\omega_1=\overline\omega_1,\dots,\omega_n=\overline\omega_n\},\qquad \tilde{\mathbb E}_0[X]=\tilde{\mathbb E}X,\ \ \tilde{\mathbb E}_N[X]=X$$

The martingale property of the discounted bond price, for $0\le k\le n\le m$ (Remark 6.2.5, p. 151):

$$\tilde{\mathbb E}_k[D_nB_{n,m}]=\tilde{\mathbb E}_k\big[\tilde{\mathbb E}_n[D_m]\big]=\tilde{\mathbb E}_k[D_m]=D_kB_{k,m}$$

The bond maturing one period ahead (Remark 6.2.9, p. 153):

$$B_{n,n+1}=\tilde{\mathbb E}_n\left[\frac{D_{n+1}}{D_n}\right]=\frac{D_{n+1}}{D_n}=\frac{1}{1+R_n},\qquad \frac{1}{B_{n,n+1}}=1+R_n$$

The time-zero price of the coupon-paying bond, the $n=0$ case of (6.2.9) (p. 153):

$$\sum_{k=0}^{m}C_kB_{0,k}=\tilde{\mathbb E}\left[\sum_{k=0}^{m}D_kC_k\right]$$

## 4. Assumptions and domain of validity

* **Model built under the risk-neutral measure:** the interest rate evolution is specified directly under $\tilde{\mathbb P}$, and every asset price is then defined by the risk-neutral pricing formula. There is no actual measure and no underlying stock in this section; absence of arbitrage is a consequence of the construction (Theorem 6.2.6 and Remark 6.2.7), not an assumption checked on parameters such as $0<d<1+r<u$ (p. 144).
* **Strictly positive probabilities:** every sequence $\omega_1\dots\omega_N$ must have strictly positive probability under $\tilde{\mathbb P}$ (pp. 144 and 150), so that the denominators $\tilde{\mathbb P}\{\omega_1=\overline\omega_1,\dots,\omega_n=\overline\omega_n\}$ in Definition 6.2.2 are nonzero.
* **Interest rate condition (6.2.1):** it is natural to assume $R_n>0$, and this is the case to keep in mind, but the analysis requires only $R_n>-1$ for all $n$ and all $\omega_1\dots\omega_n$ — the only assumption the section makes (p. 145). It keeps every factor $1+R_n$ positive, so $D_n>0$. The statement that a zero-coupon bond is worth less than its face value before maturity holds provided the interest rate is always greater than zero (p. 143).
* **Adaptedness:** $R_0$ is not random and $R_n$ depends only on $\omega_1\dots\omega_n$; consequently $D_{n+1}$ depends only on the first $n$ tosses and is "known" at time $n$, which is used repeatedly in the proof of Theorem 6.2.6 and in Remark 6.2.9.
* **Non-independent coin tosses:** $\tilde{\mathbb P}$ need not make the tosses independent or identically distributed (Example 6.2.1), so Definition 2.3.1 does not apply; Definition 6.2.2 replaces it and satisfies all the properties of Theorem 2.3.2 (Remark 6.2.3, p. 150).
* **Admissible portfolios:** $\Delta_{n,m}$ is defined only for $n<m$ (the $m$-maturity bond does not exist after time $m$) and may depend only on the first $n$ coin tosses (p. 151). All coupons and other payouts of cash are reinvested in the portfolio (p. 144).
* **Scope of (6.2.8):** Theorem 6.2.6 only partially justifies the general risk-neutral pricing formula: if a portfolio hedging a short position in the derivative security can be constructed, the price must be (6.2.8), but Theorem 6.2.6 does not guarantee that such a hedging portfolio exists (Remark 6.2.8, p. 153).
* **Coupon-paying bonds:** the payments $C_0,\dots,C_m$ are constant (nonrandom); (6.2.9) is the price at time $n$ after the payments $C_0,\dots,C_{n-1}$ have been made but before $C_n$ has been made (p. 153).

## 5. Theorems and proof outline

**Remark 6.2.3 (Properties of conditional expectation):** conditional expectation as defined in Definition 6.2.2 is a generalization of Definition 2.3.1 that allows for nonindependent coin tosses, and it satisfies all the properties of Theorem 2.3.2. The proofs are straightforward modifications of those given in the appendix (p. 150); carrying them out is Exercise 6.1.

**Remark 6.2.5 (Discounted bond prices are martingales):** for each maturity $m$, the discounted bond price $D_nB_{n,m}$, $n=0,1,\dots,m$, is a martingale under $\tilde{\mathbb P}$ (p. 151).

*Proof outline:*
1. Because $D_n$ depends only on the first $n$ tosses, "taking out what is known" (Theorem 2.3.2(ii)) turns (6.2.4) into (6.2.5).
2. For $0\le k\le n\le m$, (6.2.5) and "iterated conditioning" (Theorem 2.3.2(iii)) give $\tilde{\mathbb E}_k[D_nB_{n,m}]=\tilde{\mathbb E}_k[\tilde{\mathbb E}_n[D_m]]=\tilde{\mathbb E}_k[D_m]=D_kB_{k,m}$, which is the martingale property. Definition 6.2.4 was chosen precisely so that discounted zero-coupon bond prices would be martingales.

**Theorem 6.2.6 (Discounted wealth is a martingale):** regardless of how the portfolio random variables $\Delta_{n,m}$ are chosen (subject to the condition that $\Delta_{n,m}$ may depend only on the first $n$ coin tosses), the discounted wealth process $D_nX_n$ generated by (6.2.6) is a martingale under $\tilde{\mathbb P}$ (p. 151).

*Proof outline:*
1. Take $\tilde{\mathbb E}_n$ of (6.2.6). Since $\Delta_{n,m}$ depends only on the first $n$ tosses, "taking out what is known" (Theorem 2.3.2(ii)) leaves $\tilde{\mathbb E}_n[B_{n+1,m}]$ as the only conditional expectation to compute.
2. Since $D_{n+1}$ also depends only on the first $n$ tosses, $\tilde{\mathbb E}_n[B_{n+1,m}]=\frac{1}{D_{n+1}}\tilde{\mathbb E}_n[D_{n+1}B_{n+1,m}]$, and the martingale property of Remark 6.2.5 gives $\tilde{\mathbb E}_n[D_{n+1}B_{n+1,m}]=D_nB_{n,m}$. Together with $1+R_n=\frac{D_n}{D_{n+1}}$, this yields $\tilde{\mathbb E}_n[X_{n+1}]=\Delta_{n,n+1}+\frac{D_n}{D_{n+1}}X_n-\frac{D_n}{D_{n+1}}\Delta_{n,n+1}B_{n,n+1}$ (p. 152).
3. But $B_{n,n+1}=\tilde{\mathbb E}_n\left[\frac{D_{n+1}}{D_n}\right]=\frac{D_{n+1}}{D_n}$, because $\frac{D_{n+1}}{D_n}$ depends only on the first $n$ tosses. Substituting gives $\tilde{\mathbb E}_n[X_{n+1}]=\frac{D_n}{D_{n+1}}X_n$.
4. Using again that $D_{n+1}$ depends only on the first $n$ tosses, this is $\tilde{\mathbb E}_n[D_{n+1}X_{n+1}]=D_nX_n$, the martingale property for the discounted wealth process.

**Remark 6.2.7 (No arbitrage):** because the discounted wealth process is a martingale under $\tilde{\mathbb P}$, it has constant expectation (6.2.7). An arbitrage would be a portfolio process with $X_0=0$ and, at some future time $n$, $X_n\ge0$ for every outcome and $X_n>0$ for some outcomes; it would give $\tilde{\mathbb E}[D_nX_n]>0=X_0$, which (6.2.7) rules out. Hence, by using the risk-neutral pricing formula (6.2.4) to define zero-coupon bond prices, the model is free of arbitrage (p. 152).

**Remark 6.2.8 (General risk-neutral pricing formula):** for $0\le n\le m\le N$, the price at time $n$ of a derivative security paying $V_m$ at time $m$ (where $V_m$ depends on only the first $m$ coin tosses) is (6.2.8). Theorem 6.2.6 provides a partial justification: if a portfolio hedging a short position in the derivative security can be constructed, its value at time $n$ must be $V_n$ given by (6.2.8) (p. 153).

**Remark 6.2.9 (The money market is redundant):** investing 1 at time $n$ in the zero-coupon bond maturing at $n+1$ buys $\frac{1}{B_{n,n+1}}$ bonds paying $\frac{1}{B_{n,n+1}}=1+R_n$ at time $n+1$, the same payoff as investing 1 in the money market. It is convenient to keep a money market account in (6.2.6), but in this discrete-time model it is unnecessary to include it among the traded assets (p. 153).

**Coupon-paying bonds:** regarding the coupon-paying bond as a portfolio of $C_k$ zero-coupon bonds maturing at each time $k$ gives its time-zero price $\sum_{k=0}^mC_kB_{0,k}=\tilde{\mathbb E}\left[\sum_{k=0}^mD_kC_k\right]$ and its price (6.2.9) at time $n$. This generalizes formula (2.4.13) of Chapter 2 to nonconstant interest rates but constant payment quantities $C_0,C_1,\dots,C_m$ (pp. 153–154).

## 6. Exercises in this section (and required examples)

* **Example 6.2.1 (Conditional expectation with nonindependent tosses) (pp. 145–150):** Assume $N=3$, so $\Omega=\{HHH,HHT,HTH,HTT,THH,THT,TTH,TTT\}$, and
$\tilde{\mathbb P}\{HHH\}=\frac29$, $\tilde{\mathbb P}\{HHT\}=\frac19$, $\tilde{\mathbb P}\{HTH\}=\frac1{12}$, $\tilde{\mathbb P}\{HTT\}=\frac1{12}$, $\tilde{\mathbb P}\{THH\}=\frac16$, $\tilde{\mathbb P}\{THT\}=\frac1{12}$, $\tilde{\mathbb P}\{TTH\}=\frac18$, $\tilde{\mathbb P}\{TTT\}=\frac18$.
With $A_{HH}=\{\omega_1=H,\omega_2=H\}$, etc., and $A_H=\{\omega_1=H\}$, $A_T=\{\omega_1=T\}$, the book computes $\tilde{\mathbb P}\{A_{HH}\}=\frac13$, $\tilde{\mathbb P}\{A_{HT}\}=\frac16$, $\tilde{\mathbb P}\{A_{TH}\}=\frac14$, $\tilde{\mathbb P}\{A_{TT}\}=\frac14$, $\tilde{\mathbb P}\{A_H\}=\tilde{\mathbb P}\{A_T\}=\frac12$.
Transition probabilities at time two: $\tilde{\mathbb P}\{\omega_3=H\mid\omega_1=H,\omega_2=H\}=\frac23$, $\tilde{\mathbb P}\{\omega_3=T\mid HH\}=\frac13$; $\tilde{\mathbb P}\{\omega_3=H\mid HT\}=\frac12$, $\tilde{\mathbb P}\{\omega_3=T\mid HT\}=\frac12$; $\tilde{\mathbb P}\{\omega_3=H\mid TH\}=\frac23$, $\tilde{\mathbb P}\{\omega_3=T\mid TH\}=\frac13$; $\tilde{\mathbb P}\{\omega_3=H\mid TT\}=\frac12$, $\tilde{\mathbb P}\{\omega_3=T\mid TT\}=\frac12$.
Transition probabilities at time one: $\tilde{\mathbb P}\{\omega_2=H\mid\omega_1=H\}=\frac23$, $\tilde{\mathbb P}\{\omega_2=T\mid\omega_1=H\}=\frac13$, $\tilde{\mathbb P}\{\omega_2=H\mid\omega_1=T\}=\frac12$, $\tilde{\mathbb P}\{\omega_2=T\mid\omega_1=T\}=\frac12$.
Two-step conditional probabilities, computed either along the links of Figure 6.2.1 or as ratios of path probabilities: given $\omega_1=H$, the pairs $(\omega_2,\omega_3)=HH,HT,TH,TT$ have probabilities $\frac49,\frac29,\frac16,\frac16$; given $\omega_1=T$, they have $\frac13,\frac16,\frac14,\frac14$.
Resulting conditional expectations of $X(\omega_1\omega_2\omega_3)$:
$\tilde{\mathbb E}_1[X](H)=\frac49X(HHH)+\frac29X(HHT)+\frac16X(HTH)+\frac16X(HTT)$, $\tilde{\mathbb E}_1[X](T)=\frac13X(THH)+\frac16X(THT)+\frac14X(TTH)+\frac14X(TTT)$;
$\tilde{\mathbb E}_2[X](HH)=\frac23X(HHH)+\frac13X(HHT)$, $\tilde{\mathbb E}_2[X](HT)=\frac12X(HTH)+\frac12X(HTT)$, $\tilde{\mathbb E}_2[X](TH)=\frac23X(THH)+\frac13X(THT)$, $\tilde{\mathbb E}_2[X](TT)=\frac12X(TTH)+\frac12X(TTT)$.
If $X$ depends only on the first two tosses: $\tilde{\mathbb E}_1[X](H)=\frac23X(HH)+\frac13X(HT)$, $\tilde{\mathbb E}_1[X](T)=\frac12X(TH)+\frac12X(TT)$, and $\tilde{\mathbb E}_2[X]=X$.
(Figure 6.2.1, p. 147, prints two values that disagree with the text: the link from $R_2(HT)$ to $HTH$ is labeled $\frac13$, and the path probability is labeled $\tilde{\mathbb P}\{THH\}=\frac18$. The text gives $\tilde{\mathbb P}\{\omega_3=H\mid\omega_1=H,\omega_2=T\}=\frac12$ (p. 146) and $\tilde{\mathbb P}\{THH\}=\frac16$ (p. 146); only the text values make the two links leaving $R_2(HT)$ sum to 1, make the eight path probabilities sum to 1, and agree with $\tilde{\mathbb P}\{A_{TH}\}\cdot\frac23=\frac14\cdot\frac23=\frac16$. The figure values are almost certainly typographical errata; this card uses the text values. This correction is our reading, not one stated in the book.)

* **Exercise 6.1 (p. 174):** Prove Theorem 2.3.2 when conditional expectation is defined by Definition 6.2.2.

* **Exercise 6.7 (pp. 175–176):** Consider a binomial interest rate model in which the interest rate at time $n$ depends on only the number of heads in the first $n$ coin tosses. In other words, for each $n$ there is a function $r_n(k)$ such that $R_n(\omega_1\dots\omega_n)=r_n(\#H(\omega_1\dots\omega_n))$. Assume the risk-neutral probabilities are $\tilde p=\tilde q=\frac12$. The Ho-Lee model (Example 6.4.4) and the Black-Derman-Toy model (Example 6.5.5) satisfy these conditions. Consider a derivative security that pays 1 at time $n$ if and only if there are $k$ heads in the first $n$ tosses; i.e., the payoff is $V_n(k)=\mathbb 1_{\{\#H(\omega_1\dots\omega_n)=k\}}$. Define $\psi_0(0)=1$ and, for $n=1,2,\dots$, define $\psi_n(k)=\tilde{\mathbb E}[D_nV_n(k)]$, $k=0,1,\dots,n$, to be the price of this security at time zero. Show that the functions $\psi_n(k)$ can be computed by the recursion
$$\psi_{n+1}(0)=\frac{\psi_n(0)}{2(1+r_n(0))},$$
$$\psi_{n+1}(k)=\frac{\psi_n(k-1)}{2(1+r_n(k-1))}+\frac{\psi_n(k)}{2(1+r_n(k))},\quad k=1,\dots,n,$$
$$\psi_{n+1}(n+1)=\frac{\psi_n(n)}{2(1+r_n(n))}.$$

## 7. Cross-references

* **Definition 2.3.1 and Theorem 2.3.2 (Chapter 2, pp. 32–33):** the conditional expectation for independent coin tosses that Definition 6.2.2 generalizes, and the properties ("taking out what is known" (ii), "iterated conditioning" (iii)) used in Remark 6.2.5 and Theorem 6.2.6; their proofs are in the appendix *Proof of Fundamental Properties of Conditional Expectations* (p. 177), which Exercise 6.1 asks to adapt.
* **Theorems 2.4.5 and 2.4.7 (Chapter 2, pp. 40–42):** the discounted wealth martingale and the risk-neutral pricing formula (2.4.11) for a constant rate, generalized by Theorem 6.2.6 and (6.2.8) to a random interest rate.
* **Theorem 2.4.8 (Chapter 2, p. 42):** the cash flow valuation formula (2.4.13), which (6.2.9) generalizes to nonconstant interest rates with constant payments $C_0,\dots,C_m$.
* **Exercises 1.9, 2.9 and 3.5 (previous card, 19_stochastic_volatility_random_interest_rate.md):** a stock model in which the discount factor $\frac{1}{(1+r_0)(1+r_1)}$ is already random and path-dependent; the discount process (6.2.2), Definition 6.2.2 and (6.2.8) are the systematic versions of the objects that appear there.
* **Section 6.3 (next card):** Example 6.3.9 assigns values to the interest rates of the tree of Figure 6.2.1 and computes the bond prices $B_{n,m}$ of (6.2.4); the forward price (6.3.2), forward rates, swaps, caps and floors are all expressed through $B_{n,m}$.
* **Section 6.4:** the $m$-forward measure is defined with the Radon-Nikodým derivative $Z_{m,m}=\frac{D_m}{B_{0,m}}$, whose expectation is 1 by (6.2.3), and (6.2.5) gives $Z_{n,m}=\frac{D_nB_{n,m}}{B_{0,m}}$ (Eq. 6.4.6).
* **Examples 6.4.4 (Ho-Lee) and 6.5.5 (Black-Derman-Toy):** the two discrete-time short-rate models named in Section 6.1 (p. 144); both satisfy the assumptions of Exercise 6.7.
