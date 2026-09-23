## 1. Concept and context

A perpetual derivative security has no expiration date. It is not a traded
instrument but a mathematical bridge between the discrete-time American
pricing and hedging of Chapter 4 and the continuous-time optimal-stopping
analysis of Chapter 8 of Volume II. Because there is no expiration, both
the value $v(s)$ and the optimal exercise policy of a perpetual derivative
depend only on the current stock price, never on time (Section 5.4, p.
129). Shreve works out a specific example: a binomial model with $u=2$,
$d=1/2$, $r=1/4$ (so $\tilde p=\tilde q=1/2$ by Eq. 1.1.8 of Chapter 1) and
a perpetual American put struck at $K=4$.

## 2. Formal definitions

* **$S_n=S_0\cdot2^{M_n}$**: the stock price process of the example, where
  $M_n$ is the symmetric random walk under $\tilde{\mathbb P}$ (Eq. 5.4.1).
* **$\tau_{-m}$**: the exercise policy of exercising the first time the
  random walk falls to level $-m$, i.e. the first time the stock price
  falls to $4\cdot2^{-m}$ (p. 130).
* **$v(2^j)$ / $v(s)$**: the time-independent value of the perpetual
  American put when the stock price is on the lattice $s=2^j$, $j\in\mathbb Z$
  (p. 131).
* Three properties analogous to Theorem 4.4.2 of Chapter 4, verified for
  $v(S_n)$: (i) dominance, $v(S_n)\ge(4-S_n)^+$; (ii) the discounted
  process $(4/5)^nv(S_n)$ is a supermartingale under $\tilde{\mathbb P}$;
  (iii) minimality — if $Y_n\ge(4-S_n)^+$ for all $n$ and $(4/5)^nY_n$ is a
  supermartingale, then $v(S_n)\le Y_n$ (pp. 132–134).
* Their lattice restatement: (i)' $v(s)\ge(4-s)^+$; (ii)'
  $v(s)\ge\frac45\left[\frac12v(2s)+\frac12v(s/2)\right]$; (iii)' $v(s)$ is
  the smallest function satisfying (i)' and (ii)'; (iv)' for every
  $s=2^j$, equality holds in either (i)' or (ii)' (p. 135).
* **Perpetual American call**: the analogous contract with intrinsic value
  $g(s)=s-K$; Exercise 5.8 shows its value is $v(s)=s$, with no optimal
  exercise time (p. 136; Exercise 5.8, p. 141).

## 3. Key equations

$$S_n = S_0\cdot2^{M_n} \quad \text{(5.4.1)}$$

$$V^{(\tau_{-m})} = \tilde{\mathbb E}\left[\left(\frac{1}{1+r}\right)^{\tau_{-m}}(K-S_{\tau_{-m}})\right] = 4(1-2^{-m})\,\tilde{\mathbb E}\left[\left(\frac45\right)^{\tau_{-m}}\right] \quad \text{(5.4.2)}$$

$$V^{(\tau_{-m})} = 4(1-2^{-m})\left(\frac12\right)^m, \quad m=1,2,\dots \quad \text{(5.4.3)}$$

$$v(2^j) = 4-2^j, \quad j=1,0,-1,-2,\dots \quad \text{(5.4.4)}$$

$$v(2^j) = \tilde{\mathbb E}\left[\left(\frac45\right)^{\tau_{-(j-1)}}(4-S_{\tau_{-(j-1)}})\right] = 2\left(\frac12\right)^{j-1} = \frac{4}{2^j}, \quad j=2,3,4,\dots \quad \text{(5.4.5)}$$

$$v(2^j) = \begin{cases} 4-2^j, & \text{if } j\le1, \\ \dfrac{4}{2^j}, & \text{if } j\ge1 \end{cases} \quad \text{(5.4.6)}$$

$$\tilde{\mathbb E}_n\left[\left(\frac45\right)^{n+1}v(S_{n+1})\right] = \left(\frac45\right)^n v(S_n) \quad \text{(5.4.7)}$$

$$v(S_n) = \tilde{\mathbb E}_n\left[\left(\frac45\right)^{\tau-n}(4-S_\tau)\right] = \tilde{\mathbb E}_n\left[\left(\frac45\right)^{\tau-n}(4-S_\tau)^+\right] \quad \text{(5.4.8)}$$

$$\left(\frac45\right)^n Y_n = \left(\frac45\right)^{\tau\wedge n}Y_{\tau\wedge n} \;\ge\; \tilde{\mathbb E}_n\left[\left(\frac45\right)^{\tau\wedge k}Y_{\tau\wedge k}\right] \;\ge\; \tilde{\mathbb E}_n\left[\left(\frac45\right)^{\tau\wedge k}(4-S_{\tau\wedge k})^+\right] \quad \text{(5.4.9)}$$

$$Y_n \ge \tilde{\mathbb E}_n\left[\left(\frac45\right)^{\tau-n}(4-S_\tau)^+\right] \quad \text{(5.4.10)}$$

$$v(s) = \begin{cases} 4-s & \text{if } s\le2, \\ \dfrac4s & \text{if } s\ge4 \end{cases} \quad \text{(5.4.11)}$$

$$v(s) = \max\left\{(4-s)^+,\; \frac45\left[\frac12v(2s)+\frac12v\left(\frac s2\right)\right]\right\} \quad \text{(5.4.12)}$$

$$v(s) = \max\left\{4-s,\; \frac45\left[\frac12v(2s)+\frac12v\left(\frac s2\right)\right]\right\} \quad \text{(5.4.13)}$$

$$w(s) = \frac4s \quad \text{for all } s=2^j \quad \text{(5.4.14)}$$

$$\lim_{s\downarrow0}v(s)=4, \quad \lim_{s\to\infty}v(s)=0 \quad \text{(5.4.15)}$$

$$v(s) = \max\left\{g(s),\; \frac{1}{1+r}\big[\tilde p\,v(us)+\tilde q\,v(ds)\big]\right\} \quad \text{(5.4.16)}$$

$$\lim_{s\downarrow0}v(s)=K, \quad \lim_{s\to\infty}v(s)=0 \quad \text{(5.4.17)}$$

$$\lim_{s\downarrow0}v(s)=0, \quad \lim_{s\to\infty}\frac{v(s)}{s}=1 \quad \text{(5.4.18)}$$

*Unnumbered formulas worked out in the text:* the evaluation of Theorem
5.2.3 at $\alpha=4/5$,
$\frac{1-\sqrt{1-\alpha^2}}{\alpha}=\frac54\left(1-\sqrt{1-(4/5)^2}\right)=\frac12$
(p. 130); the resulting policy values $V^{(\tau_{-1})}=1$,
$V^{(\tau_{-2})}=3/4$, $V^{(\tau_{-3})}=7/16$ (p. 130); the strict
supermartingale computation in the exercise region $j\le0$,
$\tilde{\mathbb E}_n[(4/5)^{n+1}v(S_{n+1})]=(4/5)^n\left[\frac{16}5-2^j\right]<(4/5)^n(4-2^j)$
(p. 132); and the boundary computation at $S_n=2$ ($j=1$),
$\tilde{\mathbb E}_n[(4/5)^{n+1}v(S_{n+1})]=(4/5)^n\left[\frac25(1)+\frac25(3)\right]=(4/5)^n\frac85<(4/5)^n\cdot2$
(p. 133).

## 4. Assumptions and domain of validity

* Standing no-arbitrage condition $0<d<1+r<u$; in the example,
  $u=2,d=1/2,r=1/4$, giving $\tilde p=\tilde q=1/2$.
* Stock prices are restricted to the lattice $s=2^j$, $j\in\mathbb Z$: if
  $S_0$ is of this form, every subsequent price is too.
* Because the derivative has no expiration, $v(s)$ and the exercise
  boundary depend only on $s$, never on $n$.
* The Bellman equation (5.4.13) admits extraneous solutions besides the
  true value function — e.g. $w(s)=4/s$ for every $s=2^j$ (Eq. 5.4.14)
  also satisfies it. These are excluded by the boundary conditions
  (5.4.15) (in general, (5.4.17) for puts and (5.4.18) for calls) together
  with the minimality condition (iii)'.

## 5. Theorems and proof outline

This section verifies no separately numbered theorem; it checks that
$v(2^j)$ of (5.4.6) satisfies the three properties analogous to Theorem
4.4.2 of Chapter 4, then derives the Bellman equation from them.

*Verification of property (i) (dominance):*

1. For $j\le1$ and $S_n=2^j$, (5.4.6) gives $v(S_n)=4-S_n\ge(4-S_n)^+$
   immediately.
2. For $j\ge2$ and $S_n=2^j$, $v(S_n)=4/2^j\ge0=(4-S_n)^+$.

*Verification of property (ii) (discounted supermartingale):*

1. Exercise region ($j\le0$): direct computation gives
   $\tilde{\mathbb E}_n\left[(4/5)^{n+1}v(S_{n+1})\right]=(4/5)^n\left[\frac{16}5-2^j\right]<(4/5)^n(4-2^j)=(4/5)^nv(S_n)$
   — a strict supermartingale.
2. No-exercise region ($j\ge2$): (5.4.7) gives
   $\tilde{\mathbb E}_n\left[(4/5)^{n+1}v(S_{n+1})\right]=(4/5)^n\left[\frac{4}{5\cdot2^j}+\frac{16}{5\cdot2^j}\right]=(4/5)^n\frac{4}{2^j}=(4/5)^nv(S_n)$
   — a martingale.
3. Boundary ($j=1$, $S_n=2$):
   $\tilde{\mathbb E}_n\left[(4/5)^{n+1}v(S_{n+1})\right]=(4/5)^n\left[\frac25v(4)+\frac25v(1)\right]=(4/5)^n\frac85<(4/5)^n\cdot2=(4/5)^nv(S_n)$
   — again strict.

*Verification of property (iii) (minimality, via optional sampling):*

1. Let $Y_n$ satisfy $Y_n\ge(4-S_n)^+$ for all $n$, and suppose
   $(4/5)^nY_n$ is a supermartingale under $\tilde{\mathbb P}$.
2. Fix $n$. If $S_n\le2$, dominance already gives $v(S_n)=4-S_n\le Y_n$.
3. If $S_n=2^j$ for $j\ge2$, let $\tau$ be the first time after $n$ that
   the stock price falls to 2. Starting (5.4.5) at time $n$ instead of
   time 0 gives $v(S_n)=\tilde{\mathbb E}_n[(4/5)^{\tau-n}(4-S_\tau)]=\tilde{\mathbb E}_n[(4/5)^{\tau-n}(4-S_\tau)^+]$
   (Eq. 5.4.8), since $4-S_\tau=2>0$.
4. By the supermartingale property of $Y$, the Optional Sampling Theorem
   4.3.2 of Chapter 4, and $Y_n\ge(4-S_n)^+$, for every $k\ge n$:
   $(4/5)^nY_n=(4/5)^{\tau\wedge n}Y_{\tau\wedge n}\ge\tilde{\mathbb E}_n[(4/5)^{\tau\wedge k}Y_{\tau\wedge k}]\ge\tilde{\mathbb E}_n[(4/5)^{\tau\wedge k}(4-S_{\tau\wedge k})^+]$
   (Eq. 5.4.9).
5. Letting $k\to\infty$ and dividing by $(4/5)^n$ gives
   $Y_n\ge\tilde{\mathbb E}_n[(4/5)^{\tau-n}(4-S_\tau)^+]$ (Eq. 5.4.10).
6. Combining (5.4.8) and (5.4.10), $v(S_n)\le Y_n$.

*Derivation of the Bellman equation:*

1. The lattice properties (i)', (ii)', (iv)' say $v(s)=(4-s)^+$ where (i)'
   holds with equality ($s\le2$), and
   $v(s)=\frac45\left[\frac12v(2s)+\frac12v(s/2)\right]$ where (ii)' holds
   with equality ($s\ge4$); (iii)' rules out strict inequality holding in
   both simultaneously.
2. Combining both cases gives the Bellman equation (5.4.12), which
   simplifies to (5.4.13) once $(4-s)^+$ is replaced by $4-s$ — the two
   agree for every $s\le4$, and for $s>4$ only the continuation term can
   be the maximizer anyway.
3. The general perpetual Bellman equation for an arbitrary intrinsic value
   $g(s)$ is (5.4.16) — the same as Eq. (4.2.6) of Chapter 4, but without
   the time index, since the price no longer depends on $n$.

## 6. Exercises in this section

* **Exercise 5.6:** The value of the perpetual American put of Section 5.4
  is the limit as $n\to\infty$ of the value of an American put with the
  same strike 4 expiring at time $n$. With $S_0=4$ the perpetual value is
  1 (Eq. 5.4.6 with $j=2$). Show that the value of the finite-expiration
  American put with $S_0=4$ in the same model is 0.80 if it expires at
  time 1, 0.928 if it expires at time 3, and 0.96896 if it expires at time
  5.
* **Exercise 5.7 (Hedging a short position in the perpetual American
  put):** If the current stock price is $s$ and the hedging portfolio is
  worth $v(s)$, the hedge consumes
  $c(s)=v(s)-\frac45\left[\frac12v(2s)+v(s/2)\right]$ (Eq. 5.7.3 — printed
  exactly this way in the book, with the coefficient $\frac12$ appearing
  only on the first term; this is inconsistent with the symmetric
  continuation value of (5.4.12)/(5.4.13) and is almost certainly a
  typographical erratum, so use $\frac12v(2s)+\frac12v(s/2)$ when coding
  this) and then takes position
  $\delta(s)=\frac{v(2s)-v(s/2)}{2s-s/2}$ (Eq. 5.7.4) in the stock (see
  Theorem 4.2.2 of Chapter 4: $C_n=c(S_n)$, $\Delta_n=\delta(S_n)$).
  (i) Compute $c(s)$ for $s=2^j$ in the three cases $j\le0$, $j=1$,
  $j\ge2$. (ii) Compute $\delta(s)$ in the same three cases. (iii) Verify
  in each case that the hedge works, i.e. the portfolio's value at the
  next step equals $v$ of the next stock price regardless of whether it
  goes up or down.
* **Exercise 5.8 (Perpetual American call):** For a binomial model
  satisfying $0<d<1+r<u$, with $\tilde p,\tilde q$ as usual, consider the
  perpetual call with intrinsic value $g(s)=s-K$, $K>0$.
  (i) Let $v(s)=s$; show $v(S_n)\ge g(S_n)$ and that
  $(1/(1+r))^nv(S_n)$ is a supermartingale (in fact a martingale) — the
  analogues of properties (i) and (ii). (ii) Show that exercising at any
  fixed time $n$ gives discounted expected payoff $S_0-K/(1+r)^n$, and
  since this tends to $S_0$ as $n\to\infty$, the call's value must be at
  least $S_0$. (iii) Verify directly that $v(s)=s$ satisfies (5.4.16) and
  the boundary conditions (5.4.18). (iv) Show there is no optimal time to
  exercise the perpetual American call.
* **Exercise 5.9** (method due to Irene Villegas): a technique for solving
  (5.4.13) directly. (i) For large $s$ it is not optimal to exercise, so
  $v$ solves $v(s)=\frac25v(2s)+\frac25v(s/2)$ (Eq. 5.7.5); substituting
  $s^p$ gives a quadratic in $2^p$ with roots $2^p=2,1/2$, i.e. $p=1,-1$,
  so $v_1(s)=s$ and $v_2(s)=1/s$ solve (5.7.5). (ii) The general solution
  is $v(s)=As+B/s$ (Eq. 5.7.6); use the second boundary condition of
  (5.4.15) to show $A=0$. (iii) For small $s$, $v(s)=4-s$; show that
  $f_B(s)=\frac Bs-(4-s)$ has no zero for $s>0$ when $B>4$, but does when
  $B\le4$. (iv) For $B\le4$ with $s_B=2^j$ solving $f_B(s)=0$, suppose the
  owner exercises the first time the stock price is $s_B$ or smaller;
  then the discounted risk-neutral expected payoff is $v_B(S_0)$, where
  $v_B(s)=4-s$ for $s\le s_B$ and $v_B(s)=B/s$ for $s\ge s_B$ (Eq. 5.7.7).
  Which values of $B$ and $s_B$ give the owner the largest option value?
  (v) The derivative of $v_B$ is $v_B'(s)=-1$ for $s<s_B$ and
  $v_B'(s)=-B/s^2$ for $s>s_B$. Show that the best value of $B$ for the
  option owner is the one that makes this derivative continuous at
  $s=s_B$ (i.e. the two formulas agree there).

## 7. Cross-references

* **Theorem 5.2.3 (previous card, Section 5.2):** its moment-generating
  function $\mathbb E\alpha^{\tau_m}$ is used directly, at
  $\alpha=4/5=1/(1+r)$, to evaluate the expected discounted payoff of
  each policy $\tau_{-m}$ in (5.4.2)–(5.4.3).
* **Theorem 4.2.2 and Theorems 4.4.2/4.4.4 (Chapter 4):** supply the
  discrete-time template for the three properties (i)–(iii) verified
  here, and the consumption/hedging construction reused (with $s$ in
  place of $S_n$) in Exercise 5.7.
* **Theorem 4.3.2 (Chapter 4, Section 4.3):** the Optional Sampling
  Theorem, applied directly in the proof of property (iii) to obtain
  (5.4.9).
* **Chapter 8 of Volume II:** continuous-time optimal stopping for
  American derivatives; the discrete derivative-matching condition of
  Exercise 5.9(v) is the discrete-time analogue of the smooth pasting
  principle used there.