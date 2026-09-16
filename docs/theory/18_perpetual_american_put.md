## 1. Concept and Context

* **Perpetual Derivative Security** [Section 5.4, p. 129]:
  * A "perpetual" derivative security has no expiration date ($N = \infty$). While not typically traded directly in this form, it serves as a fundamental mathematical concept and a bridge between discrete-time American option pricing/hedging (Chapter 4) and continuous-time optimal stopping for American derivatives (Volume II, Chapter 8) [Section 5.4, p. 129].
  * Because the contract has no expiration date, both the option pricing function $v(s)$ and the optimal exercise policy depend solely on the current stock price $s = S_n$, and are completely independent of time $n$ [Section 5.4, p. 129].

* **Specific Model Parameters in Shreve's Example** [Section 5.4, p. 129]:
  * Binomial model parameters: Up factor $u = 2$, down factor $d = 1/2$, and interest rate $r = 1/4$.
  * Risk-neutral probabilities (Eq. 1.1.8): $\tilde{p} = \frac{1+r-d}{u-d} = \frac{5/4 - 1/2}{2 - 1/2} = \frac{1}{2}$ and $\tilde{q} = \frac{u-1-r}{u-d} = \frac{1}{2}$.
  * Stock price process: $S_n = S_0 \cdot 2^{M_n}$, where $M_n$ is a symmetric random walk under $\tilde{\mathbb{P}}$ [Section 5.4, p. 129, Eq. (5.4.1)].
  * Derivative instrument: Perpetual American put option with strike price $K = 4$. Immediate exercise at time $n$ pays $(4 - S_n)^+$ [Section 5.4, p. 129].

---

## 2. Formal Definitions

* **First Passage Exercise Policies ($\tau_{-m}$)** [Section 5.4, p. 130]:
  * For a positive integer $m$, the exercise policy $\tau_{-m}$ is the stopping time representing the first time the random walk $M_n$ falls to $-m$ (or equivalently, the first time the stock price $S_n$ falls to $4 \cdot 2^{-m}$) [Section 5.4, p. 130].
* **Option Value Function $v(s)$ / $v(2^j)$** [Section 5.4, pp. 131–132]:
  * For stock prices on the lattice $s = 2^j$ (where $j \in \mathbb{Z}$), $v(2^j)$ represents the time-independent value of the perpetual American option when $S_n = 2^j$ [Section 5.4, p. 131].
* **Perpetual Call Analogue** [Section 5.4, p. 136; Exercise 5.8, p. 141]:
  * A perpetual American call with strike $K > 0$ and intrinsic value $g(s) = s - K$, whose pricing function is shown in Exercise 5.8 to be $v(s) = s$ with no optimal exercise time [Section 5.4, p. 136; Exercise 5.8, p. 141].

* **Three Defining Properties of $v(S_n)$ (Analogous to Theorem 4.4.2)** [Section 5.4, pp. 132–133]:
  * **Property (i) (Dominance of Intrinsic Value)**: $v(S_n) \ge (4 - S_n)^+$ for all $n \ge 0$ [p. 132].
  * **Property (ii) (Discounted Supermartingale)**: The discounted process $\left(\frac{4}{5}\right)^n v(S_n)$ is a supermartingale under $\tilde{\mathbb{P}}$ [p. 132].
  * **Property (iii) (Minimality)**: If $Y_n$ is another process satisfying $Y_n \ge (4 - S_n)^+$ for all $n$ and $\left(\frac{4}{5}\right)^n Y_n$ is a supermartingale under $\tilde{\mathbb{P}}$, then $v(S_n) \le Y_n$ for all $n$ [pp. 133–134].

* **Lattice Recast of Properties (i)'–(iv)'** [Section 5.4, p. 135]:
  * **Property (i)'**: $v(s) \ge (4 - s)^+$ for all $s = 2^j$ [p. 135].
  * **Property (ii)'**: $v(s) \ge \frac{4}{5} \left[ \frac{1}{2} v(2s) + \frac{1}{2} v\left(\frac{s}{2}\right) \right]$ for all $s = 2^j$ [p. 135].
  * **Property (iii)'**: $v(s)$ is the smallest function satisfying (i)' and (ii)' [p. 135].
  * **Property (iv)'**: For every $s = 2^j$, equality holds in either (i)' or (ii)' [p. 135].

---

## 3. Key Equations

* **Equation (5.4.1)** — Stock Price Process in the Example:
  $$S_n = S_0 \cdot 2^{M_n} \quad \text{(5.4.1)}$$

* **Equation (5.4.2)** — Expected Discounted Payoff for Policy $\tau_{-m}$:
  $$V^{(\tau_{-m})} = \tilde{\mathbb{E}} \left[ \left(\frac{1}{1+r}\right)^{\tau_{-m}} (K - S_{\tau_{-m}}) \right] = 4(1 - 2^{-m}) \tilde{\mathbb{E}} \left[ \left(\frac{4}{5}\right)^{\tau_{-m}} \right] \quad \text{(5.4.2)}$$

* **Equation (5.4.3)** — Closed-Form Policy Value Function for $\tau_{-m}$:
  $$V^{(\tau_{-m})} = 4(1 - 2^{-m}) \left(\frac{1}{2}\right)^m, \quad m = 1, 2, \dots \quad \text{(5.4.3)}$$

* **Equation (5.4.4)** — Immediate Exercise Option Value ($j \le 1$):
  $$v(2^j) = 4 - 2^j, \quad j = 1, 0, -1, -2, \dots \quad \text{(5.4.4)}$$

* **Equation (5.4.5)** — Postponed Exercise Option Value ($j \ge 2$):
  $$v(2^j) = \tilde{\mathbb{E}} \left[ \left(\frac{4}{5}\right)^{\tau_{-(j-1)}} (4 - S_{\tau_{-(j-1)}}) \right] = 2 \cdot \left(\frac{1}{2}\right)^{j-1} = \frac{4}{2^j}, \quad j = 2, 3, 4, \dots \quad \text{(5.4.5)}$$

* **Equation (5.4.6)** — Piecewise Option Value Function:
  $$v(2^j) = \begin{cases} 4 - 2^j & \text{if } j \le 1, \\ \frac{4}{2^j} & \text{if } j \ge 1 \end{cases} \quad \text{(5.4.6)}$$

* **Equation (5.4.7)** — Martingale Verification in No-Exercise Region ($j \ge 2$):
  $$\tilde{\mathbb{E}}_n \left[ \left(\frac{4}{5}\right)^{n+1} v(S_{n+1}) \right] = \left(\frac{4}{5}\right)^n v(S_n) \quad \text{(5.4.7)}$$

* **Equation (5.4.8)** — Optimal Stopping Value Identity at time $n$:
  $$v(S_n) = \tilde{\mathbb{E}}_n \left[ \left(\frac{4}{5}\right)^{\tau - n} (4 - S_\tau) \right] = \tilde{\mathbb{E}}_n \left[ \left(\frac{4}{5}\right)^{\tau - n} (4 - S_\tau)^+ \right] \quad \text{(5.4.8)}$$

* **Equation (5.4.9)** — Optional Sampling Inequality for Supermartingale $Y_k$:
  $$\left(\frac{4}{5}\right)^n Y_n \ge \tilde{\mathbb{E}}_n \left[ \left(\frac{4}{5}\right)^{k \wedge \tau} Y_{k \wedge \tau} \right] \quad \text{(5.4.9)}$$

* **Equation (5.4.10)** — Minimality Upper Bound for $Y_n$:
  $$Y_n \ge \tilde{\mathbb{E}}_n \left[ \left(\frac{4}{5}\right)^{\tau - n} Y_\tau \right] \ge \tilde{\mathbb{E}}_n \left[ \left(\frac{4}{5}\right)^{\tau - n} (4 - S_\tau)^+ \right] \quad \text{(5.4.10)}$$

* **Equation (5.4.11)** — Piecewise Value Function in continuous variable $s$:
  $$v(s) = \begin{cases} 4 - s & \text{if } s \le 2, \\ \frac{4}{s} & \text{if } s \ge 4 \end{cases} \quad \text{(5.4.11)}$$

* **Equation (5.4.12)** — Unsimplified Lattice Bellman Equation:
  $$v(s) = \max \left\{ (4 - s)^+, \frac{4}{5} \left[ \frac{1}{2} v(2s) + \frac{1}{2} v\left(\frac{s}{2}\right) \right] \right\} \quad \text{(5.4.12)}$$

* **Equation (5.4.13)** — Simplified Bellman Equation for Put Example:
  $$v(s) = \max \left\{ 4 - s, \frac{4}{5} \left[ \frac{1}{2} v(2s) + \frac{1}{2} v\left(\frac{s}{2}\right) \right] \right\} \quad \text{(5.4.13)}$$

* **Equation (5.4.14)** — Extraneous Solution to Bellman Equation:
  $$w(s) = \frac{4}{s} \quad \text{for all } s = 2^j \quad \text{(5.4.14)}$$

* **Equation (5.4.15)** — Boundary Conditions for Put Example:
  $$\lim_{s \downarrow 0} v(s) = 4, \quad \lim_{s \to \infty} v(s) = 0 \quad \text{(5.4.15)}$$

* **Equation (5.4.16)** — General Bellman Equation for Perpetual American Derivatives:
  $$v(s) = \max \left\{ g(s), \frac{1}{1+r} [\tilde{p} v(us) + \tilde{q} v(ds)] \right\} \quad \text{(5.4.16)}$$

* **Equation (5.4.17)** — General Boundary Conditions for Perpetual American Put:
  $$\lim_{s \downarrow 0} v(s) = K, \quad \lim_{s \to \infty} v(s) = 0 \quad \text{(5.4.17)}$$

* **Equation (5.4.18)** — Boundary Conditions for Perpetual American Call (Exercise 5.8):
  $$\lim_{s \downarrow 0} v(s) = 0, \quad \lim_{s \to \infty} \frac{v(s)}{s} = 1 \quad \text{(5.4.18)}$$

* **Unnumbered Intermediate Equations**:
  * Moment-generating substitution value [p. 130]: $\frac{1 - \sqrt{1 - \alpha^2}}{\alpha} = \frac{5}{4} \left( 1 - \sqrt{1 - \left(\frac{4}{5}\right)^2} \right) = \frac{1}{2}$ (unnumbered).
  * Evaluated policy values [p. 130]: $V^{(\tau_{-1})} = 1, V^{(\tau_{-2})} = 3/4, V^{(\tau_{-3})} = 7/16$ (unnumbered).
  * Strict supermartingale verification for $j \le 0$ [p. 132]: $\tilde{\mathbb{E}}_n \left[ \left(\frac{4}{5}\right)^{n+1} v(S_{n+1}) \right] = \left(\frac{4}{5}\right)^n \left[ \frac{16}{5} - 2^j \right] < \left(\frac{4}{5}\right)^n (4 - 2^j)$ (unnumbered).
  * Boundary supermartingale verification for $S_n = 2$ ($j = 1$) [p. 133]: $\tilde{\mathbb{E}}_n \left[ \left(\frac{4}{5}\right)^{n+1} v(S_{n+1}) \right] = \left(\frac{4}{5}\right)^n \left[ \frac{2}{5}(1) + \frac{2}{5}(3) \right] = \left(\frac{4}{5}\right)^n \frac{8}{5} < \left(\frac{4}{5}\right)^n \cdot 2$ (unnumbered).

---

## 4. Assumptions and Domain of Validity

* **Standing No-Arbitrage Condition**:
  $$0 < d < 1 + r < u$$
  For the example in Section 5.4: $u = 2, d = 1/2, r = 1/4 \implies \tilde{p} = \tilde{q} = 1/2$ [p. 129].
* **Lattice Restriction**:
  Stock prices are restricted to the set of lattice points $s = S_0 \cdot 2^j = 2^j$ for integers $j \in \mathbb{Z}$ [p. 131].
* **Time Independence**:
  Because the derivative has no expiration date, the option price $v(s)$ and the optimal exercise boundary are time-invariant functions depending only on $s$ [p. 129].
* **Ruling Out Extraneous Bellman Solutions**:
  The Bellman equation (5.4.13) admits extraneous solutions (such as $w(s) = 4/s$ for all $s$). These are ruled out by applying the boundary conditions (5.4.15) (or (5.4.17) for puts, (5.4.18) for calls) and enforcing the minimality condition Property (iii)' [pp. 136, 138].

---

## 5. Theorems and Proof Outline

### **Verification of Perpetual American Put Properties** [pp. 132–134]

* **Verification of Property (i) (Dominance)**:
  * For $j \le 1$ ($S_n \le 2$), $v(S_n) = 4 - S_n = (4 - S_n)^+$.
  * For $j \ge 2$ ($S_n \ge 4$), $v(S_n) = 4/S_n > 0 = (4 - S_n)^+$.
  * Hence $v(S_n) \ge (4 - S_n)^+$ for all $n \ge 0$ [p. 132].

* **Verification of Property (ii) (Discounted Supermartingale)**:
  1. *Exercise Region ($j \le 0$)*: Direct calculation shows $\tilde{\mathbb{E}}_n \left[ \left(\frac{4}{5}\right)^{n+1} v(S_{n+1}) \right] = \left(\frac{4}{5}\right)^n \left[ \frac{16}{5} - 2^j \right] < \left(\frac{4}{5}\right)^n v(S_n)$, so the discounted process is a strict supermartingale [p. 132].
  2. *No-Exercise Region ($j \ge 2$)*: Eq. (5.4.7) shows $\tilde{\mathbb{E}}_n \left[ \left(\frac{4}{5}\right)^{n+1} v(S_{n+1}) \right] = \left(\frac{4}{5}\right)^n \left[ \frac{4}{5 \cdot 2^j} + \frac{16}{5 \cdot 2^j} \right] = \left(\frac{4}{5}\right)^n \frac{4}{2^j} = \left(\frac{4}{5}\right)^n v(S_n)$, so the discounted process is a martingale [pp. 132–133].
  3. *Boundary ($j = 1$, $S_n = 2$)*: $\tilde{\mathbb{E}}_n \left[ \left(\frac{4}{5}\right)^{n+1} v(S_{n+1}) \right] = \left(\frac{4}{5}\right)^n \left[ \frac{2}{5} v(4) + \frac{2}{5} v(1) \right] = \left(\frac{4}{5}\right)^n \cdot \frac{8}{5} < \left(\frac{4}{5}\right)^n \cdot 2$, a strict supermartingale [p. 133].

* **Verification of Property (iii) (Minimality via Optional Sampling)**:
  1. Let $Y_n$ be any process satisfying $Y_n \ge (4 - S_n)^+$ and whose discounted process $(4/5)^n Y_n$ is a supermartingale [p. 133].
  2. Fix $n$. If $S_n \le 2$, $v(S_n) = 4 - S_n \le Y_n$ immediately by dominance [p. 133].
  3. If $S_n \ge 4$, let $\tau$ be the stopping time representing the first passage of stock price to level $2$ after time $n$.
  4. By Eq. (5.4.5) started at time $n$, $v(S_n) = \tilde{\mathbb{E}}_n \left[ \left(\frac{4}{5}\right)^{\tau - n} (4 - S_\tau) \right] = \tilde{\mathbb{E}}_n \left[ \left(\frac{4}{5}\right)^{\tau - n} (4 - S_\tau)^+ \right]$ [p. 134, Eq. (5.4.8)].
  5. By Optional Sampling (Theorem 4.3.2), $\left(\frac{4}{5}\right)^n Y_n \ge \tilde{\mathbb{E}}_n \left[ \left(\frac{4}{5}\right)^{k \wedge \tau} Y_{k \wedge \tau} \right]$ for all $k \ge n$ [p. 134, Eq. (5.4.9)].
  6. Taking $k \to \infty$ yields $Y_n \ge \tilde{\mathbb{E}}_n \left[ \left(\frac{4}{5}\right)^{\tau - n} Y_\tau \right] \ge \tilde{\mathbb{E}}_n \left[ \left(\frac{4}{5}\right)^{\tau - n} (4 - S_\tau)^+ \right] = v(S_n)$, proving $v(S_n) \le Y_n$ [p. 134, Eq. (5.4.10)].

* **Derivation of Bellman Equation**:
  * Properties (i)', (ii)', and (iv)' imply that $v(s)$ equals $(4 - s)^+$ when (i)' holds with equality ($s \le 2$) and equals $\frac{4}{5} \left[ \frac{1}{2} v(2s) + \frac{1}{2} v(s/2) \right]$ when (ii)' holds with equality ($s \ge 4$). Combining gives the Bellman equation (5.4.12) / (5.4.13) [pp. 135–136].

---

## 6. Exercises in this section

### **Exercise 5.6** [p. 140]
> The value of the perpetual American put in Section 5.4 is the limit as $n \to \infty$ of the value of an American put with the same strike price 4 that expires at time $n$. When the initial stock price is $S_0 = 4$, the value of the perpetual American put is 1 (see (5.4.6) with $j = 2$). Show that the value of an American put in the same model when the initial stock price is $S_0 = 4$ is 0.80 if the put expires at time 1, 0.928 if the put expires at time 3, and 0.96896 if the put expires at time 5.

---

### **Exercise 5.7 (Hedging a short position in the perpetual American put)** [p. 140]
> Suppose you have sold the perpetual American put of Section 5.4 and are hedging the short position in this put. Suppose that at the current time the stock price is $s$ and the value of your hedging portfolio is $v(s)$. Your hedge is to first consume the amount
> $$c(s) = v(s) - \frac{4}{5} \left[ \frac{1}{2} v(2s) + \frac{1}{2} v\left(\frac{s}{2}\right) \right] \quad \text{(5.7.3)}$$
> and then take a position
> $$\delta(s) = \frac{v(2s) - v(s/2)}{2s - s/2} \quad \text{(5.7.4)}$$
> in the stock. (See Theorem 4.2.2 of Chapter 4. The processes $C_n$ and $\Delta_n$ in that theorem are obtained by replacing the dummy variable $s$ by the stock price $S_n$ in (5.7.3) and (5.7.4); i.e., $C_n = c(S_n)$ and $\Delta_n = \delta(S_n)$.) If you hedge this way, then regardless of whether the stock goes up or down on the next step, the value of your hedging portfolio should agree with the value of the perpetual American put.
> **(i)** Compute $c(s)$ when $s = 2^j$ for the three cases $j \le 0$, $j = 1$, and $j \ge 2$.
> **(ii)** Compute $\delta(s)$ when $s = 2^j$ for the three cases $j \le 0$, $j = 1$, and $j \ge 2$.
> **(iii)** Verify in each of the three cases $s = 2^j$ for $j \le 0$, $j = 1$, and $j \ge 2$ that the hedge works (i.e., regardless of whether the stock goes up or down, the value of your hedging portfolio at the next time is equal to the value of the perpetual American put at that time).

---

### **Exercise 5.8 (Perpetual American call)** [p. 141]
> Like the perpetual American put of Section 5.4, the perpetual American call has no expiration. Consider a binomial model with up factor $u$, down factor $d$, and interest rate $r$ that satisfies the no-arbitrage condition $0 < d < 1 + r < u$. The risk-neutral probabilities are
> $$\tilde{p} = \frac{1+r-d}{u-d}, \quad \tilde{q} = \frac{u-1-r}{u-d}$$
> The intrinsic value of the perpetual American call is $g(s) = s - K$, where $K > 0$ is the strike price. The purpose of this exercise is to show that the value of the call is always the price of the underlying stock, and there is no optimal exercise time.
> **(i)** Let $v(s) = s$. Show that $v(S_n)$ is always at least as large as the intrinsic value $g(S_n)$ of the call and $\left(\frac{1}{1+r}\right)^n v(S_n)$ is a supermartingale under the risk-neutral probabilities. In fact, $\left(\frac{1}{1+r}\right)^n v(S_n)$ is a martingale. These are the analogues of properties (i) and (ii) for the perpetual American put of Section 5.4.
> **(ii)** To show that $v(s) = s$ is not too large to be the value of the perpetual American call, we must find a good policy for the purchaser of the call. Show that if the purchaser of the call exercises at time $n$, regardless of the stock price at that time, then the discounted risk-neutral expectation of her payoff is $S_0 - \frac{K}{(1+r)^n}$. Because this is true for every $n$, and
> $$\lim_{n \to \infty} \left[ S_0 - \frac{K}{(1+r)^n} \right] = S_0,$$
> the value of the call at time zero must be at least $S_0$. (The same is true at all other times; the value of the call is at least as great as the current stock price.)
> **(iii)** In place of (i) and (ii) above, we could verify that $v(s) = s$ is the value of the perpetual American call by checking that this function satisfies the equation (5.4.16) and boundary conditions (5.4.18). Do this verification.
> **(iv)** Show that there is no optimal time to exercise the perpetual American call.

---

### **Exercise 5.9** [pp. 141–142]
> (Provided by Irene Villegas.) Here is a method for solving equation (5.4.13) for the value of the perpetual American put in Section 5.4.
> **(i)** We first determine $v(s)$ for large values of $s$. When $s$ is large, it is not optimal to exercise the put, so the maximum in (5.4.13) will be given by the second term,
> $$\frac{4}{5} \left[ \frac{1}{2} v(2s) + \frac{1}{2} v\left(\frac{s}{2}\right) \right] = \frac{2}{5} v(2s) + \frac{2}{5} v\left(\frac{s}{2}\right).$$
> We thus seek solutions to the equation
> $$v(s) = \frac{2}{5} v(2s) + \frac{2}{5} v\left(\frac{s}{2}\right). \quad \text{(5.7.5)}$$
> All such solutions are of the form $s^p$ for some constant $p$ or linear combinations of functions of this form. Substitute $s^p$ into (5.7.5), obtain a quadratic equation for $2^p$, and solve to obtain $2^p = 2$ or $2^p = 1/2$. This leads to the values $p = 1$ and $p = -1$, i.e., $v_1(s) = s$ and $v_2(s) = 1/s$ are solutions to (5.7.5).
> **(ii)** The general solution to (5.7.5) is a linear combination of $v_1(s)$ and $v_2(s)$, i.e.,
> $$v(s) = As + \frac{B}{s}. \quad \text{(5.7.6)}$$
> For large values of $s$, the value of the perpetual American put must be given by (5.7.6). It remains to evaluate $A$ and $B$. Using the second boundary condition in (5.4.15), show that $A$ must be zero.
> **(iii)** We have thus established that for large values of $s$, $v(s) = B/s$ for some constant $B$ still to be determined. For small values of $s$, the value of the put is its intrinsic value $4 - s$. We must choose $B$ so these two functions coincide at some point, i.e., we must find a value for $B$ so that, for some $s > 0$,
> $$f_B(s) = \frac{B}{s} - (4 - s)$$
> equals zero. Show that, when $B > 4$, this function does not take the value 0 for any $s > 0$, but, when $B \le 4$, the equation $f_B(s) = 0$ has a solution.
> **(iv)** Let $B$ be less than or equal to 4, and let $s_B$ be a solution of the equation $f_B(s) = 0$. Suppose $s_B$ is a stock price that can be attained in the model (i.e., $s_B = 2^j$ for some integer $j$). Suppose further that the owner of the perpetual American put exercises the first time the stock price is $s_B$ or smaller. Then the discounted risk-neutral expected payoff of the put is $v_B(S_0)$, where $v_B(s)$ is given by the formula
> $$v_B(s) = \begin{cases} 4 - s & \text{if } s \le s_B, \\ \frac{B}{s} & \text{if } s \ge s_B. \end{cases} \quad \text{(5.7.7)}$$
> Show that among all values $B \le 4$ for which $s_B$ is a stock price that can be attained in the model, the value of $v_B(S_0)$ is maximized by $B = 4$.
> **(v)** In continuous time, one does not require $s_B$ to be on a lattice of stock prices; $s_B$ can be any positive number. Show that $f_B(s) = 0$ has a unique solution if and only if $B = 4$. Show that for $B = 4$, the solution is $s_4 = 2$. Show that for $B = 4$, the function $v_4(s)$ defined by (5.7.7) is differentiable at $s = 2$. (This is the smooth pasting condition for continuous-time optimal stopping problems; see Chapter 8 of Volume II.)

---

## 7. Cross-References

* **Theorem 5.2.3 (Section 5.2, p. 123)**: Moment-generating function of first passage time $\tau_m$, used directly to calculate expected discounted payoffs $V^{(\tau_{-m})}$ for exercise policies $\tau_{-m}$ in Eq. (5.4.2)–(5.4.3) [p. 130].
* **Theorem 4.2.2 & Theorem 4.4.2 / 4.4.4 (Chapter 4, pp. 95, 104, 106)**: Discrete-time foundation for the three defining properties of American option prices and self-financing consumption/hedging, referenced in Properties (i)–(iii) and Exercise 5.7 [pp. 132, 140].
* **Theorem 4.3.2 (Chapter 4, p. 99)**: Optional Sampling Theorem for stopped supermartingales, used directly in the proof of Property (iii) minimality [p. 134].
* **Volume II, Chapter 8**: Continuous-time optimal stopping, American option pricing PDEs, and smooth pasting conditions, which extend Section 5.4 and Exercise 5.9(v) to continuous time [pp. 129, 138, 142].