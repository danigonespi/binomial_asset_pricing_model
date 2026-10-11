## 1. Concept and context

Like a forward contract, a *futures contract* is designed to lock in a price for the purchase or sale of an asset before the time of the purchase or sale, but it addresses two shortcomings of forward contracts (Section 6.5, pp. 168–169). First, on any date before a given delivery date there can be demand for forward contracts with that delivery date, so efficient markets would need, for each delivery date, a multitude of forward contracts with different initiation dates; by contrast, the underlying process for futures contracts is a *futures price* tied to a delivery date but not to an initiation date, and all agents, whatever the date on which they enter, trade on the futures price for their desired delivery date. Second, although a forward contract has zero value at initiation, as the price of the underlying asset moves it takes on a value that may be positive or negative, and one party may become concerned about default by the other; futures contracts, through *marking to market*, require agents to settle daily so that no agent ever has a large obligation to another. Section 6.5 defines the futures price process by requiring the futures contract to have zero risk-neutral value at all times (Definition 6.5.1), shows that it is the risk-neutral conditional expectation of the asset price at delivery and therefore a martingale under $\tilde{\mathbb P}$ (Theorem 6.5.2), and compares futures and forward prices (Corollary 6.5.3, Remark 6.5.4), illustrating the comparison in the Black-Derman-Toy model (Example 6.5.5). The book notes that the distinction between forward contracts and futures was pointed out by Margrabe and by Black, and that no-arbitrage pricing of futures in a discrete-time model was developed by Cox, Ingersoll and Ross and by Jarrow and Oldfield (Section 6.7, p. 174).

## 2. Formal definitions

* **$m$-futures price process $\text{Fut}_{n,m}$**: consider an asset with price process $S_0,S_1,\dots,S_N$ in the binomial interest rate model. For $0\le m\le N$, the $m$-futures price process $\text{Fut}_{n,m}$, $n=0,1,\dots,m$, is an adapted process with the following properties: (i) $\text{Fut}_{m,m}=S_m$; (ii) for each $n$, $0\le n\le m-1$, the risk-neutral value at time $n$ of the contract that receives the payments $\text{Fut}_{k+1,m}-\text{Fut}_{k,m}$ at time $k+1$ for all $k=n,\dots,m-1$ is zero, i.e., (6.5.1) holds (Definition 6.5.1, p. 169).
* **Long futures position**: an agent who at time $n$ takes a long position in a futures contract with delivery at a later time $m$ agrees to receive the payments $\text{Fut}_{k+1,m}-\text{Fut}_{k,m}$ at times $k+1$, for $k=n,\dots,m-1$, and then to take delivery of the asset at its market price $S_m$ at time $m$. Any of these payments can be negative, in which case the agent must pay money rather than receive it (pp. 169–170).
* **Short futures position**: an agent who holds a short position makes payments equal to $\text{Fut}_{k+1,m}-\text{Fut}_{k,m}$ and agrees to sell the asset at its market price $S_m$ at time $m$ (p. 170).
* **Margin account and margin call**: the vehicle for these transfers of money is the margin account set up by the broker for the agent. At the end of each day the broker either deposits money into or withdraws money from the margin account; if the balance becomes too low, the broker issues a margin call, requiring the agent either to deposit more money or to close the futures position (p. 170).
* **Closing a position**: because the value of the futures contract is zero at all times, an agent can "sell" a long contract (or close a short one) at any time at no cost; all payments to the agent then cease and the agent is no longer obligated to trade the asset at time $m$ (p. 170).
* **Black-Derman-Toy (BDT) model**: the interest rate at time $n$ is $R_n(\omega_1\dots\omega_n)=a_nb_n^{\#H(\omega_1\dots\omega_n)}$, where the constants $a_0,a_1,\dots$ and $b_1,b_2,\dots$ are used to calibrate the model, and the risk-neutral probabilities are taken to be $\tilde p=\tilde q=\frac12$ (Example 6.5.5, p. 172).

## 3. Key equations

$$\frac{1}{D_n}\tilde{\mathbb E}_n\left[\sum_{k=n}^{m-1}D_{k+1}(\text{Fut}_{k+1,m}-\text{Fut}_{k,m})\right]=0 \quad \text{(6.5.1)}$$

$$\text{Fut}_{n,m}=\tilde{\mathbb E}_n[S_m],\quad n=0,1,\dots,m \quad \text{(6.5.2)}$$

$$\tilde{\mathbb E}_n\Big[D_{k+1}\big(\tilde{\mathbb E}_{k+1}[S_m]-\tilde{\mathbb E}_k[S_m]\big)\Big]=0,\quad k=n,\dots,m-1 \quad \text{(6.5.3)}$$

$$\sum_{k=n}^{m-1}\tilde{\mathbb E}_n\big[D_{k+1}(\text{Fut}_{k+1,m}-\text{Fut}_{k,m})\big]=0\quad\text{for } n=0,1,\dots,m-1 \quad \text{(6.5.4)}$$

$$0=\sum_{k=n}^{m-1}\tilde{\mathbb E}_n\big[D_{k+1}(\text{Fut}_{k+1,m}-\text{Fut}_{k,m})\big]-\sum_{k=n+1}^{m-1}\tilde{\mathbb E}_{n+1}\big[D_{k+1}(\text{Fut}_{k+1,m}-\text{Fut}_{k,m})\big] \quad \text{(6.5.5)}$$

$$0=\sum_{k=n}^{m-1}\tilde{\mathbb E}_n\big[D_{k+1}(\text{Fut}_{k+1,m}-\text{Fut}_{k,m})\big]-\sum_{k=n+1}^{m-1}\tilde{\mathbb E}_n\big[D_{k+1}(\text{Fut}_{k+1,m}-\text{Fut}_{k,m})\big]=\tilde{\mathbb E}_n\big[D_{n+1}(\text{Fut}_{n+1,m}-\text{Fut}_{n,m})\big] \quad \text{(6.5.6)}$$

*Unnumbered formulas in the text:*

Total payments received by the long position between times $n$ and $m$, and the balance after purchasing the asset at its market price (p. 170):

$$\sum_{k=n}^{m-1}(\text{Fut}_{k+1,m}-\text{Fut}_{k,m})=\text{Fut}_{m,m}-\text{Fut}_{n,m}=S_m-\text{Fut}_{n,m},\qquad S_m-\text{Fut}_{n,m}-S_m=-\text{Fut}_{n,m}$$

The step from (6.5.6) to the martingale property, since $\text{Fut}_{n,m}$ and $D_{n+1}$ depend only on the first $n$ coin tosses (p. 171):

$$D_{n+1}\big(\tilde{\mathbb E}_n[\text{Fut}_{n+1,m}]-\text{Fut}_{n,m}\big)=0,\qquad \tilde{\mathbb E}_n[\text{Fut}_{n+1,m}]=\text{Fut}_{n,m},\quad n=0,1,\dots,m-1$$

The time-zero forward and futures prices compared in Corollary 6.5.3 (p. 172):

$$\text{For}_{0,m}=\frac{S_0}{B_{0,m}}=\frac{S_0}{\tilde{\mathbb E}D_m}=\frac{\tilde{\mathbb E}[D_mS_m]}{\tilde{\mathbb E}D_m},\qquad \text{Fut}_{0,m}=\tilde{\mathbb E}S_m$$

The forward interest rates and the interest rate futures of Example 6.5.5 (pp. 172–173):

$$F_{n,2}=\frac{B_{n,2}-B_{n,3}}{B_{n,3}},\qquad \text{Fut}_{n,3}=\tilde{\mathbb E}_n[R_2]$$

## 4. Assumptions and domain of validity

* **Model and asset:** the binomial interest rate model of Section 6.2 under the risk-neutral measure $\tilde{\mathbb P}$, with an asset whose price $S_n$ depends on the first $n$ coin tosses and whose discounted price is a $\tilde{\mathbb P}$-martingale (6.3.1). The delivery date satisfies $0\le m\le N$, and $\text{Fut}_{n,m}$ is required to be adapted (Definition 6.5.1).
* **Zero value at all times:** condition (6.5.1) is designed so that at initiation the value of the futures contract is zero, so it costs nothing to enter a long or a short position, apart from setting up a margin account. Since (6.5.1) is required for every $n$ between $0$ and $m-1$, the value of the futures contract is zero at all times (p. 170).
* **"Locking in" a price:** after the futures payments and the purchase of the asset at $S_m$, the long position is left with $-\text{Fut}_{n,m}$ and owns the asset; it has paid $\text{Fut}_{n,m}$ for the asset only *if one ignores the time value of money*, because the payments are received at different dates (p. 170).
* **Forward versus futures:** the time-zero forward and futures prices coincide if and only if $D_m$ and $S_m$ are uncorrelated under $\tilde{\mathbb P}$, in particular when the interest rate is not random (Corollary 6.5.3). When $D_m$ and $S_m$ are negatively correlated — an increase in the asset price tends to come with an increase in the interest rate — $\text{For}_{0,m}<\text{Fut}_{0,m}$ (Remark 6.5.4).
* **BDT example:** the risk-neutral probabilities are $\tilde p=\tilde q=\frac12$, so every path of the three-period model has probability $\frac18$; the model satisfies the assumptions of Exercise 6.7 (p. 176).
* **Notation:** the book writes $F_{k,m}$ once for $\text{Fut}_{k,m}$ ("receive the payments $\text{Fut}_{k+1,m}-F_{k,m}$", p. 169) and $F_{n,m}$ once for $\text{Fut}_{n,m}$ ("the agent has paid $F_{n,m}$ and acquired the asset", p. 170). In this chapter $F_{n,m}$ denotes the forward interest rate (6.3.3), so both are typographical slips for the futures price; this card writes $\text{Fut}$ throughout. This reading is ours, not a correction stated in the book.

## 5. Theorems and proof outline

**Theorem 6.5.2 (Futures price):** let $m$ be given with $0\le m\le N$. Then $\text{Fut}_{n,m}=\tilde{\mathbb E}_n[S_m]$, $n=0,1,\dots,m$ (6.5.2), is the unique process satisfying the conditions of Definition 6.5.1 (p. 170).

*Proof outline (existence):*
1. $\tilde{\mathbb E}_m[S_m]=S_m$, so the right-hand side of (6.5.2) satisfies Definition 6.5.1(i).
2. For Definition 6.5.1(ii) it suffices to show that each term of the sum in (6.5.1) has $\tilde{\mathbb E}_n$ conditional expectation zero, i.e., (6.5.3).
3. Because $D_{k+1}$ depends only on the first $k$ coin tosses, iterated conditioning gives $\tilde{\mathbb E}_n\big[D_{k+1}(\tilde{\mathbb E}_{k+1}[S_m]-\tilde{\mathbb E}_k[S_m])\big]=\tilde{\mathbb E}_n\big[D_{k+1}(\tilde{\mathbb E}_k[\tilde{\mathbb E}_{k+1}[S_m]]-\tilde{\mathbb E}_k[S_m])\big]=\tilde{\mathbb E}_n\big[D_{k+1}(\tilde{\mathbb E}_k[S_m]-\tilde{\mathbb E}_k[S_m])\big]=0$ (p. 171).

*Proof outline (uniqueness):*
1. From (6.5.1), any process satisfying Definition 6.5.1 satisfies (6.5.4).
2. For $n=0,1,\dots,m-2$, replacing $n$ by $n+1$ in (6.5.4) and subtracting gives (6.5.5).
3. Taking conditional expectations $\tilde{\mathbb E}_n$ in (6.5.5) and using iterated conditioning gives (6.5.6); setting $n=m-1$ in (6.5.4) shows that (6.5.6) also holds for $n=m-1$.
4. Both $\text{Fut}_{n,m}$ and $D_{n+1}$ depend only on the first $n$ coin tosses, so (6.5.6) reduces to $D_{n+1}(\tilde{\mathbb E}_n[\text{Fut}_{n+1,m}]-\text{Fut}_{n,m})=0$, which yields $\tilde{\mathbb E}_n[\text{Fut}_{n+1,m}]=\text{Fut}_{n,m}$: the martingale property under $\tilde{\mathbb P}$ for $\text{Fut}_{n,m}$, $n=0,1,\dots,m$.
5. Since $\text{Fut}_{m,m}=S_m$, the martingale property implies (6.5.2).

**Corollary 6.5.3 (Forward and futures prices):** let $m$ be given with $0\le m\le N$. Then $\text{For}_{0,m}=\text{Fut}_{0,m}$ if and only if $D_m$ and $S_m$ are uncorrelated under $\tilde{\mathbb P}$. In particular, this is the case if the interest rate is not random (p. 172).

*Proof outline:*
1. From Theorem 6.3.2, $\text{For}_{0,m}=\frac{S_0}{B_{0,m}}=\frac{S_0}{\tilde{\mathbb E}D_m}=\frac{\tilde{\mathbb E}[D_mS_m]}{\tilde{\mathbb E}D_m}$, and from Theorem 6.5.2, $\text{Fut}_{0,m}=\tilde{\mathbb E}S_m$.
2. These two formulas agree if and only if $\tilde{\mathbb E}[D_mS_m]=\tilde{\mathbb E}D_m\cdot\tilde{\mathbb E}S_m$, which is uncorrelatedness of $D_m$ and $S_m$.

**Remark 6.5.4 (Futures above forwards):** if $D_m$ and $S_m$ are negatively correlated, so that $\tilde{\mathbb E}[D_mS_m]<\tilde{\mathbb E}D_m\cdot\tilde{\mathbb E}S_m$, then $\text{For}_{0,m}<\text{Fut}_{0,m}$. This is the case when an increase in the asset price tends to be accompanied by an increase in the interest rate (a decrease in the discount factor). The long futures position benefits from this more than the long forward position, since it receives an immediate payment to invest at the higher interest rate, whereas the forward contract has no settlement until the delivery date $m$. Because the long futures position is more favorable, the initial futures price is higher: the person using futures to lock in a purchase price locks in a higher price than a person using a long forward position (p. 172).

## 6. Exercises in this section (and required examples)

* **Example 6.5.5 (Black-Derman-Toy model) (pp. 172–173):** with $a_n=\frac{0.05}{1.2^n}$ and $b_n=1.44$, the three-period BDT model of Figure 6.5.1 has $R_0=0.05$; $R_1(H)=0.06$, $R_1(T)=0.04167$; $R_2(HH)=0.072$, $R_2(HT)=0.05$, $R_2(TH)=0.05$, $R_2(TT)=0.03472$; every path has $\tilde{\mathbb P}$-probability $\frac18$.
Zero-coupon bond prices: $B_{0,2}=0.9064$, $B_{0,3}=0.8620$, $B_{1,2}(H)=0.9434$, $B_{1,2}(T)=0.9600$, $B_{1,3}(H)=0.8893$, $B_{1,3}(T)=0.9210$.
Forward interest rates $F_{n,2}=\frac{B_{n,2}-B_{n,3}}{B_{n,3}}$: $F_{0,2}=0.05147$, $F_{1,2}(H)=0.06089$, $F_{1,2}(T)=0.04231$. These are the forward prices for a contract that pays $R_2$ at time three; the second subscript 2 denotes the time the rate is set, not the time of payment.
Futures prices for the contract that pays $R_2$ at time three, $\text{Fut}_{n,3}=\tilde{\mathbb E}_n[R_2]$: $\text{Fut}_{0,3}=0.05168$, $\text{Fut}_{1,3}(H)=0.06100$, $\text{Fut}_{1,3}(T)=0.04236$.
The interest rate futures are slightly higher than the forward interest rates, for the reason discussed in Remark 6.5.4.
(The bond prices, $F_{1,2}(H)$, $F_{1,2}(T)$ and the three futures prices are reproduced exactly by recomputing the model. The printed $F_{0,2}=0.05147$ is not: (6.3.3) with the model's bond prices gives $F_{0,2}=0.05143$, the same value is obtained as $\frac{1}{B_{0,3}}\tilde{\mathbb E}[D_3R_2]$ and as $\tilde{\mathbb E}^3[F_{1,2}]$ (the martingale property of Exercise 6.5), and using the four-decimal bond prices printed above gives $0.05151$. The discrepancy does not affect the conclusion $F_{n,2}<\text{Fut}_{n,3}$. This recomputation is ours; the book does not comment on it.)

* **Exercise 6.6 (p. 175):** Let $S_m$ be the price at time $m$ of an asset in a binomial interest rate model. For $n=0,1,\dots,m$, the forward price is $\text{For}_{n,m}=\frac{S_n}{B_{n,m}}$ and the futures price is $\text{Fut}_{n,m}=\tilde{\mathbb E}_n[S_m]$.
1. Suppose that at each time $n$ an agent takes a long forward position and sells this contract at time $n+1$. Show that this generates cash flow $S_{n+1}-\frac{S_nB_{n+1,m}}{B_{n,m}}$ at time $n+1$.
2. Show that if the interest rate is a constant $r$ and at each time $n$ an agent takes a long position of $(1+r)^{m-n-1}$ forward contracts, selling these contracts at time $n+1$, then the resulting cash flow is the same as the difference in the futures price $\text{Fut}_{n+1,m}-\text{Fut}_{n,m}$.
(The book prints the futures price as $\text{Fut}_{n,m}=\tilde{\mathbb E}_n[S_n]$, which would simply equal $S_n$; by Theorem 6.5.2 (Eq. 6.5.2) the futures price is $\tilde{\mathbb E}_n[S_m]$, which is almost certainly what is intended. This correction is our reading, not one stated in the book.)

## 7. Cross-references

* **Theorem 6.3.2 and Definition 6.3.4 (21_fixed_income_derivatives.md):** the forward price $\text{For}_{n,m}=\frac{S_n}{B_{n,m}}$ (6.3.2) compared with the futures price in Corollary 6.5.3 and Exercise 6.6, and the forward interest rates (6.3.3) computed in Example 6.5.5.
* **Theorem 6.4.2 and Eq. (6.4.9) (22_forward_measures.md):** forward prices are martingales under the forward measure $\tilde{\mathbb P}^m$, whereas Theorem 6.5.2 shows that futures prices are martingales under the risk-neutral measure $\tilde{\mathbb P}$; Exercise 6.5 asks to verify $\tilde{\mathbb E}^3[F_{1,2}]=F_{0,2}$ in the Ho-Lee model.
* **Definition 6.2.2, Remark 6.2.3 and the discount process (6.2.2) (20_binomial_interest_rate_model.md):** the conditional expectations, iterated conditioning and the fact that $D_{k+1}$ depends only on the first $k$ tosses, used throughout the proof of Theorem 6.5.2; Exercise 6.7 lists the BDT model among the models it covers.
* **Exercise 2.11 (Chapter 2, p. 58; 07_martingales.md):** the forward contract with a constant interest rate, the case in which Corollary 6.5.3 gives $\text{For}_{0,m}=\text{Fut}_{0,m}$.
* **Section 6.6 (Summary, p. 173):** futures contracts, introduced in Section 6.5, are related to forward contracts in Corollary 6.5.3.
