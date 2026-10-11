## 1. Concept and context

With zero-coupon bond prices $B_{n,m}$ defined by risk-neutral pricing (Section 6.2), Section 6.3 (pp. 154–160) prices the common derivative securities of the fixed income market: forward contracts on an asset, forward interest rates, interest rate swaps, and interest rate caps and floors. For forwards, forward rates and swaps the book determines the price by constructing a hedging portfolio for a short position — in each case a *static* hedge made of zero-coupon bonds, set up once and never rebalanced — and then checks that the result agrees with the risk-neutral pricing formula. Whenever such hedging portfolios can be constructed, risk-neutral pricing is justified. For caps and floors the section uses risk-neutral pricing directly; short position hedges for these instruments can usually be constructed, but the book does not work out the detailed assumptions that guarantee this, and Exercise 6.4 provides an example of such a construction (p. 157). The section closes with Example 6.3.9, which assigns values to the interest rates of the tree of Figure 6.2.1 and computes the bond prices and the price of a three-period cap.

## 2. Formal definitions

* **Asset price $S_n$**: the price at time $n$ of an asset in the binomial model for interest rates — possibly a stock, but more often a contract whose payoff depends on the interest rate. $S_n$ depends on the first $n$ coin tosses, and since $\tilde{\mathbb P}$ is a risk-neutral measure, the discounted asset price is a martingale under $\tilde{\mathbb P}$, Eq. (6.3.1) (p. 154).
* **Forward contract and $m$-forward price $\text{For}_{n,m}$**: a forward contract is an agreement to pay a specified delivery price $K$ at a delivery date $m$, where $0\le m\le N$, for the asset whose price at time $m$ is $S_m$. The $m$-forward price of this asset at time $n$, where $0\le n\le m$, is the value of $K$ that makes the forward contract have no-arbitrage price zero at time $n$ (Definition 6.3.1, p. 154).
* **Static hedge**: a hedge that calls for no trading between the time $n$ when it is set up and the time $m$ when the contract expires (Remark 6.3.3, p. 154).
* **Forward interest rate $F_{n,m}$**: for $0\le n\le m\le N-1$, the forward interest rate at time $n$ for investing at time $m$ is defined by (6.3.3) (Definition 6.3.4, p. 155). It is the rate that can be "locked in" at time $n$ for investing between times $m$ and $m+1$.
* **Interest rate swap**: for $1\le m\le N$, an $m$-period interest rate swap is a contract that makes payments $S_1,\dots,S_m$ at times $1,\dots,m$, where $S_n=K-R_{n-1}$; the fixed rate $K$ is constant. The *$m$-period swap rate* $SR_m$ is the value of $K$ that makes the time-zero no-arbitrage price of the swap equal to zero (Definition 6.3.6, p. 156). The long ("receive fixed") position receives the fixed payment $K$ and pays the variable rate $R_{n-1}$ on a principal of 1; it converts a fixed-rate loan into a variable-rate loan, and the short position does the reverse.
* **$\text{Swap}_m$**: the time-zero no-arbitrage price of the $m$-period swap (Theorem 6.3.7, p. 156).
* **Interest rate cap and floor**: for $1\le m\le N$, an $m$-period interest rate cap makes payments $C_n=(R_{n-1}-K)^+$ and an $m$-period interest rate floor makes payments $F_n=(K-R_{n-1})^+$ at times $n=1,\dots,m$. A contract that makes the payment $C_n$ (resp. $F_n$) at only one time $n$ is an interest rate *caplet* (resp. *floorlet*) (Definition 6.3.8, pp. 157–158). $\text{Cap}_m$ and $\text{Floor}_m$ denote their risk-neutral prices.

## 3. Key equations

$$D_nS_n=\tilde{\mathbb E}_n[D_{n+1}S_{n+1}],\quad n=0,1,\dots,N-1 \quad \text{(6.3.1)}$$

$$\text{For}_{n,m}=\frac{S_n}{B_{n,m}} \quad \text{(6.3.2)}$$

$$F_{n,m}=\frac{B_{n,m}}{B_{n,m+1}}-1=\frac{B_{n,m}-B_{n,m+1}}{B_{n,m+1}} \quad \text{(6.3.3)}$$

$$\text{Swap}_m=\sum_{n=1}^{m}B_{0,n}(K-F_{0,n-1})=K\sum_{n=1}^{m}B_{0,n}-(1-B_{0,m}) \quad \text{(6.3.4)}$$

$$SR_m=\frac{\sum_{n=1}^{m}B_{0,n}F_{0,n-1}}{\sum_{n=1}^{m}B_{0,n}}=\frac{1-B_{0,m}}{\sum_{n=1}^{m}B_{0,n}} \quad \text{(6.3.5)}$$

$$\text{Swap}_m=\sum_{n=1}^{m}\big[K\tilde{\mathbb E}D_n-(\tilde{\mathbb E}D_{n-1}-\tilde{\mathbb E}D_n)\big]=\tilde{\mathbb E}\sum_{n=1}^{m}D_n(K-R_{n-1}) \quad \text{(6.3.6)}$$

$$\text{Cap}_m=\tilde{\mathbb E}\sum_{n=1}^{m}D_n(R_{n-1}-K)^+ \quad \text{(6.3.7)}$$

$$\text{Floor}_m=\tilde{\mathbb E}\sum_{n=1}^{m}D_n(K-R_{n-1})^+ \quad \text{(6.3.8)}$$

$$\text{Swap}_m+\text{Cap}_m=\text{Floor}_m \quad \text{(6.3.9)}$$

$$\tilde{\mathbb E}\Big[D_1\Big(R_0-\frac13\Big)^+\Big]=0,\qquad \tilde{\mathbb E}\Big[D_2\Big(R_1-\frac13\Big)^+\Big]=\frac57\cdot\frac1{15}\cdot\frac14+\frac57\cdot\frac1{15}\cdot\frac14=\frac1{42},\qquad \tilde{\mathbb E}\Big[D_3\Big(R_2-\frac13\Big)^+\Big]=\frac37\cdot\frac23\cdot\frac13=\frac2{21} \quad \text{(6.3.10)}$$

*Unnumbered formulas in the text:*

The time-$n$ discounted price of the forward contract with payoff $S_m-K$ at time $m$, by the risk-neutral pricing formula (Remark 6.3.3, p. 155):

$$\tilde{\mathbb E}_n[D_m(S_m-K)]=\tilde{\mathbb E}_n[D_mS_m]-KD_n\tilde{\mathbb E}_n\left[\frac{D_m}{D_n}\right]=D_n(S_n-KB_{n,m})$$

The forward rate for investing at the current time (p. 155):

$$F_{m,m}=\frac{B_{m,m}}{B_{m,m+1}}-1=\frac{1}{\frac{1}{1+R_m}}-1=R_m$$

The no-arbitrage price at time $n$ of a contract that pays $R_m$ at time $m+1$ (Theorem 6.3.5, p. 155):

$$B_{n,m+1}F_{n,m}=B_{n,m}-B_{n,m+1}$$

The telescoping sum used in the proof of Theorem 6.3.7 (p. 157):

$$\sum_{n=1}^{m}B_{0,n}F_{0,n-1}=\sum_{n=1}^{m}(B_{0,n-1}-B_{0,n})=1-B_{0,m}$$

The payoff identity behind the cap-floor relation (p. 158):

$$K-R_{n-1}+(R_{n-1}-K)^+=(K-R_{n-1})^+$$

The time-zero price of the three-period cap of Example 6.3.9 (p. 160):

$$\text{Cap}_3=0+\frac1{42}+\frac2{21}=\frac5{42}$$

## 4. Assumptions and domain of validity

* **Risk-neutral measure:** $\tilde{\mathbb P}$ has been taken to be a risk-neutral measure, so every asset considered satisfies the martingale property (6.3.1) (p. 154). All the model assumptions of Section 6.2 remain in force: strictly positive path probabilities, (6.2.1), and $R_n$ depending only on the first $n$ tosses.
* **Tradable bonds:** Theorem 6.3.2 assumes that zero-coupon bonds of all maturities can be traded (p. 154); the hedges of Theorems 6.3.2 and 6.3.5 are built from them.
* **Index ranges:** forward prices are defined for $0\le n\le m\le N$; forward rates, Definition 6.3.4 and Theorem 6.3.5 for $0\le n\le m\le N-1$ (they involve the bond maturing at $m+1\le N$); swaps and caps/floors for $1\le m\le N$, with the payment at time $n$ determined by the rate $R_{n-1}$ set one period earlier.
* **Constant fixed rate:** in swaps, caps and floors the fixed rate (strike) $K$ is constant (p. 156).
* **Hedging versus risk-neutral pricing:** Theorems 6.3.2, 6.3.5 and 6.3.7 obtain prices by constructing hedging portfolios for short positions; whenever such hedges can be constructed, risk-neutral pricing is justified, and (6.3.6) is an example of this. The cap and floor prices (6.3.7)–(6.3.8) are defined by risk-neutral pricing without working out the assumptions that guarantee a hedge exists (p. 157); this is the limitation already noted in Remark 6.2.8.
* **Notation:** the book reuses symbols across sections. In this section $S_n$ denotes both the asset price of (6.3.1)–(6.3.2) and the swap payments of Definition 6.3.6; $C_n$ denotes the cap payments, whereas in Section 6.2 it denotes the coupons of a coupon-paying bond; and the floor payments $F_n$ (one index) are different from the forward rates $F_{n,m}$ (two indices).

## 5. Theorems and proof outline

**Theorem 6.3.2 (Forward price):** consider an asset with price process $S_0,S_1,\dots,S_N$ in the binomial interest rate model, and assume that zero-coupon bonds of all maturities can be traded. For $0\le n\le m\le N$, the $m$-forward price at time $n$ of the asset is (6.3.2) (p. 154).

*Proof outline:*
1. At time $n$ an agent sells the forward contract with delivery date $m$ and delivery price $K$, chosen so that the contract has price zero; selling it generates no income.
2. The agent immediately shorts $\frac{S_n}{B_{n,m}}$ zero-coupon bonds maturing at $m$ and uses the income $S_n$ to buy one share of the asset, then does no further trading.
3. At time $m$ the agent delivers the share and receives $K$; after covering the short bond position, the agent is left with $K-\frac{S_n}{B_{n,m}}$.
4. If this is positive the agent has found an arbitrage; if it is negative, taking the opposite positions (long the forward, long the $m$-maturity bond, short the asset) is an arbitrage. To preclude arbitrage, $K$ must be given by (6.3.2).

**Remark 6.3.3 (Static hedge and risk-neutral pricing):** the proof of Theorem 6.3.2 constructs a static hedge for a short position in the forward contract. Whenever there is a hedge, static or not, its discounted value is a martingale under the risk-neutral measure, so the risk-neutral pricing formula applies; using (6.3.1) and (6.2.4) it gives the time-$n$ discounted price $D_n(S_n-KB_{n,m})$ of the forward contract, which is zero exactly when $K$ is given by (6.3.2) (pp. 154–155).

**Forward interest rates (p. 155):** at time $n$ an agent shorts one $m$-maturity zero-coupon bond and uses the income to buy $\frac{B_{n,m}}{B_{n,m+1}}$ bonds maturing at $m+1$, at zero cost. At time $m$ the agent invests 1 to cover the short position, and at time $m+1$ receives $\frac{B_{n,m}}{B_{n,m+1}}$. Between $m$ and $m+1$ it is as if the agent had invested at the rate (6.3.3), locked in at time $n$. Since $F_{m,m}=R_m$, the rate that can be locked in at time $m$ for investing at time $m$ is $R_m$.

**Theorem 6.3.5 (Price of a contract paying $R_m$):** let $0\le n\le m\le N-1$. The no-arbitrage price at time $n$ of a contract that pays $R_m$ at time $m+1$ is $B_{n,m+1}F_{n,m}=B_{n,m}-B_{n,m+1}$ (p. 155).

*Proof outline:*
1. At time $n$ an agent sells the contract for $B_{n,m}-B_{n,m+1}$, buys one $m$-maturity bond and shorts one $(m+1)$-maturity bond; the total set-up cost is zero.
2. At time $m$ the agent receives 1 from the $m$-maturity bond and invests it at the money market rate $R_m$.
3. At time $m+1$ the investment yields $1+R_m$: the agent pays 1 to cover the short bond and uses the remaining $R_m$ to pay off the contract. The short position is hedged with initial capital $B_{n,m}-B_{n,m+1}$, which is therefore the no-arbitrage price.

**Forward price of $R_m$ and locking in a rate (p. 156):** by Theorems 6.3.2 and 6.3.5, the forward price at time $n$ of the contract that delivers $R_m$ at time $m+1$ is $F_{n,m}$ (replace $m$ by $m+1$ in (6.3.2) and set $S_n=B_{n,m+1}F_{n,m}$). Shorting this forward contract at time $n$ costs nothing; investing 1 at time $m$ at the variable rate $R_m$ and settling the forward at $m+1$ leaves $1+F_{n,m}$, so the rate $F_{n,m}$ has been locked in.

**Theorem 6.3.7 (Swap price):** the time-zero no-arbitrage price of the $m$-period interest rate swap of Definition 6.3.6 is (6.3.4); in particular, the $m$-period swap rate is (6.3.5) (p. 156).

*Proof outline:*
1. The time-zero no-arbitrage price of the payment $K$ at time $n$ is $KB_{0,n}$, and by Theorem 6.3.5 the time-zero no-arbitrage price of the payment $R_{n-1}$ at time $n$ is $B_{0,n}F_{0,n-1}$; hence the time-zero price of $S_n$ is $B_{0,n}(K-F_{0,n-1})$, and summing gives the middle term of (6.3.4).
2. Since $B_{0,n}F_{0,n-1}=B_{0,n-1}-B_{0,n}$, the sum telescopes to $1-B_{0,m}$ (using $B_{0,0}=1$), which gives the right-hand side of (6.3.4).
3. Setting the swap price equal to zero and solving for $K$ gives (6.3.5).
4. Consistency with risk-neutral pricing (6.3.6): using (6.3.4), (6.3.3), (6.2.4) and (6.2.2), $B_{0,n}=\tilde{\mathbb E}D_n$ and $\tilde{\mathbb E}D_{n-1}=\tilde{\mathbb E}[D_n(1+R_{n-1})]$, so the swap price equals $\tilde{\mathbb E}\sum_{n=1}^mD_n(K-R_{n-1})$, the risk-neutral price of the swap (p. 157).

**Caps, floors and the swap-cap-floor relation (pp. 157–158):** the cap and floor prices are (6.3.7) and (6.3.8). A cap caps at $K$ the variable interest paid on a loan of 1 (it pays the difference whenever the interest owed exceeds $K$), and a floor guarantees at least $K$ on a variable-rate investment of 1. Since $K-R_{n-1}+(R_{n-1}-K)^+=(K-R_{n-1})^+$, at each time the payoff of a portfolio holding a swap and a cap is the payoff of a floor, which gives (6.3.9). In particular, if $K$ is set equal to the $m$-period swap rate, the cap and the floor have the same initial price.

## 6. Exercises in this section (and required examples)

* **Example 6.3.9 (Bond prices and a three-period cap) (pp. 158–160):** the tree of Figure 6.2.1, with the same risk-neutral path probabilities, now carries the interest rates of Figure 6.3.1: $R_0=0$; $R_1(H)=\frac16$, $R_1(T)=\frac25$; $R_2(HH)=1$, $R_2(HT)=0$, $R_2(TH)=\frac14$, $R_2(TT)=\frac14$.
Table 6.1 (columns $\frac1{1+R_0}$, $\frac1{1+R_1}$, $\frac1{1+R_2}$, $D_1$, $D_2$, $D_3$, $\tilde{\mathbb P}\{A_{\omega_1\omega_2}\}$): $HH$: $1,\frac67,\frac12,1,\frac67,\frac37,\frac13$; $HT$: $1,\frac67,1,1,\frac67,\frac67,\frac16$; $TH$: $1,\frac57,\frac45,1,\frac57,\frac47,\frac14$; $TT$: $1,\frac57,\frac45,1,\frac57,\frac47,\frac14$.
Time-zero bond prices: $B_{0,1}=\tilde{\mathbb E}D_1=1$, $B_{0,2}=\tilde{\mathbb E}D_2=\frac67\cdot\frac13+\frac67\cdot\frac16+\frac57\cdot\frac14+\frac57\cdot\frac14=\frac{11}{14}$, $B_{0,3}=\tilde{\mathbb E}D_3=\frac37\cdot\frac13+\frac67\cdot\frac16+\frac47\cdot\frac14+\frac47\cdot\frac14=\frac47$.
Time-one bond prices: $B_{1,1}=1$, $B_{1,2}(H)=\frac67$, $B_{1,2}(T)=\frac57$, $B_{1,3}(H)=\frac47$, $B_{1,3}(T)=\frac47$, each computed as $\frac{1}{D_1}\tilde{\mathbb E}_1[D_m]$.
Time-two bond prices: $B_{2,2}=1$, $B_{2,3}(HH)=\frac{D_3(HH)}{D_2(HH)}=\frac12$, $B_{2,3}(HT)=1$, $B_{2,3}(TH)=\frac45$, $B_{2,3}(TT)=\frac45$.
Cap with $K=\frac13$; payoff table (columns $R_0$, $(R_0-\frac13)^+$, $R_1$, $(R_1-\frac13)^+$, $R_2$, $(R_2-\frac13)^+$): $HH$: $0,0,\frac16,0,1,\frac23$; $HT$: $0,0,\frac16,0,0,0$; $TH$: $0,0,\frac25,\frac1{15},\frac14,0$; $TT$: $0,0,\frac25,\frac1{15},\frac14,0$.
The time-one, time-two and time-three caplets are worth $0$, $\frac1{42}$ and $\frac2{21}$ at time zero (6.3.10), so $\text{Cap}_3=\frac5{42}$.
(The book prints the fourth row of the payoff table with the label "$HT$", repeating the label of the second row. Its values $R_1=\frac25$ and $R_2=\frac14$ are those of the path beginning $TT$, and $TT$ is the only pair missing from the table, so the label is almost certainly a typographical erratum for "$TT$". In addition, Figure 6.3.1 (p. 159) repeats the label $\frac13$ of Figure 6.2.1 on the link from $R_2(HT)$ to $HTH$, while the text of Example 6.2.1 gives $\frac12$; this card uses the text value — see the previous card. Both corrections are our reading, not ones stated in the book.)

* **Exercise 6.2 (p. 174):** Verify that the discounted value of the static hedging portfolio constructed in the proof of Theorem 6.3.2 is a martingale under $\tilde{\mathbb P}$.

* **Exercise 6.3 (p. 174):** Let $0\le n\le m\le N-1$ be given. According to the risk-neutral pricing formula, the contract that pays $R_m$ at time $m+1$ has time-$n$ price $\frac{1}{D_n}\tilde{\mathbb E}_n[D_{m+1}R_m]$. Use the properties of conditional expectations to show that this gives the same result as Theorem 6.3.5, i.e.,
$$\frac{1}{D_n}\tilde{\mathbb E}_n[D_{m+1}R_m]=B_{n,m}-B_{n,m+1}.$$

* **Exercise 6.4 (pp. 174–175):** Using the data in Example 6.3.9, this exercise constructs a hedge for a short position in the caplet paying $(R_2-\frac13)^+$ at time three. From the second table in Example 6.3.9, the payoff at time three of this caplet is $V_3(HH)=\frac23$, $V_3(HT)=V_3(TH)=V_3(TT)=0$. Since this payoff depends on only the first two coin tosses, the price of the caplet at time two can be determined by discounting: $V_2(HH)=\frac{1}{1+R_2(HH)}V_3(HH)=\frac13$, $V_2(HT)=V_2(TH)=V_2(TT)=0$. Indeed, if one is hedging a short position in the caplet and has a portfolio valued at $\frac13$ at time two in the event $\omega_1=H,\omega_2=H$, then one can simply invest this $\frac13$ in the money market in order to have the $\frac23$ required to pay off the caplet at time three. In Example 6.3.9, the time-zero price of the caplet is determined to be $\frac2{21}$ (see (6.3.10)).
1. Determine $V_1(H)$ and $V_1(T)$, the price at time one of the caplet in the events $\omega_1=H$ and $\omega_1=T$, respectively.
2. Show how to begin with $\frac2{21}$ at time zero and invest in the money market and the maturity two bond in order to have a portfolio value $X_1$ at time one that agrees with $V_1$, regardless of the outcome of the first coin toss. Why do we invest in the maturity two bond rather than the maturity three bond to do this?
3. Show how to take the portfolio value $X_1$ at time one and invest in the money market and the maturity three bond in order to have a portfolio value $X_2$ at time two that agrees with $V_2$, regardless of the outcome of the first two coin tosses. Why do we invest in the maturity three bond rather than the maturity two bond to do this?

## 7. Cross-references

* **Definition 6.2.4 and Remark 6.2.5 (previous card, 20_binomial_interest_rate_model.md):** the bond prices $B_{n,m}$ in which every result of this section is expressed, and the martingale property (6.2.5) used in Remark 6.3.3; Remark 6.2.9 ($B_{m,m+1}=\frac1{1+R_m}$) gives $F_{m,m}=R_m$.
* **Theorem 6.2.6 and Remark 6.2.8 (previous card):** the martingale property of discounted portfolios that justifies risk-neutral pricing whenever a hedge exists, as used in Remark 6.3.3 and (6.3.6).
* **Example 6.2.1 and Figure 6.2.1 (previous card):** the tree and the risk-neutral probabilities reused in Example 6.3.9.
* **Exercise 2.11 (Chapter 2, p. 58):** the forward contract and the put-call parity $C_N=F_N+P_N$ with a constant rate, where $F_0=S_0-\frac{K}{(1+r)^N}$ and the forward price is $(1+r)^NS_0$; (6.3.2) is its generalization to random interest rates, since with a constant rate $B_{0,N}=\frac{1}{(1+r)^N}$. The relation (6.3.9), "swap + cap = floor", plays for interest rates the role that put-call parity plays for stock options (this comparison is our reading; the book does not draw it).
* **Section 6.4 (next card):** Example 6.4.3 recomputes the time-three caplet of Example 6.3.9 under the 3-forward measure and recovers the price $\frac2{21}$ of (6.3.10); (6.4.9) identifies forward prices (6.3.2) as expectations under the forward measure, and Exercise 6.5 shows that the forward rates $F_{n,m}$ are martingales under $\tilde{\mathbb P}^{m+1}$.
* **Section 6.5:** futures prices are compared with the forward prices (6.3.2) in Corollary 6.5.3, and Example 6.5.5 computes forward rates $F_{n,2}$ in the Black-Derman-Toy model.
