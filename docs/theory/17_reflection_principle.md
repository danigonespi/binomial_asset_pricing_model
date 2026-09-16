## 1. Concept and Context

* **Combinatoric Proof of First Passage Times** (Section 5.3, pp. 126–129):
  * Section 5.3 presents a second, purely combinatorics-based proof of Theorem 5.2.5 (the distribution of the first passage time $\tau_1$) using the **reflection principle** [p. 127].
  * Rather than relying on moment-generating functions and power series expansions as in Section 5.2, the reflection principle provides a geometric path-counting argument: every path that reaches a target level before a final time but ends below it corresponds bijectively to a "reflected" path that ends above the target level [pp. 127–128].
  * Shreve explicitly notes that this same geometric reflection technique serves as the foundational idea for analyzing Brownian motion and deriving analytical pricing formulas for exotic options (such as barrier and lookback options) in Chapter 7 of Volume II [p. 127].

---

## 2. Formal Definitions

* **Reflected Path** [p. 127]:
  * For a random walk path $M_0, M_1, \dots, M_{2j-1}$ that reaches level $1$ at some first passage time $\tau_1 \le 2j-1$, the **reflected path** is constructed by keeping the original path up to time $\tau_1$ and reflecting all subsequent steps about level $1$ (i.e., replacing every subsequent up-step with a down-step and every down-step with an up-step) [p. 127].

* **Maximum-to-Date Process ($M_n^*$)** [Exercise 5.5, p. 140]:
  * For a random walk $M_k$, the running maximum process up to time $n$ is defined by:
    $$M_n^* = \max_{1 \le k \le n} M_k \quad \text{(5.7.2)}$$

---

## 3. Key Equations

* **Author-Numbered Equations in Section 5.3**:
  * *Note*: Section 5.3 contains **no equations numbered by the author**; all formulas in this section are unnumbered combinatoric path-counting steps that culminate in re-deriving equation **(5.2.22)** from Section 5.2 [pp. 127–128].

* **Author-Numbered Equations in Exercises 5.5**:
  * **Equation (5.7.2)** — Running Maximum Process Definition:
    $$M_n^* = \max_{1 \le k \le n} M_k \quad \text{(5.7.2)}$$

* **Unnumbered Key Formulas in Section 5.3 & Exercise 5.5**:
  * Reflection Path Count Identity [p. 128]:
    $$\mathbb{P}\{\tau_1 \le 2j - 1\} = \mathbb{P}\{M_{2j-1} = 1\} + 2\mathbb{P}\{M_{2j-1} \ge 3\} = 1 - \mathbb{P}\{M_{2j-1} = -1\}$$
  * Re-derivation of (5.2.22) via Reflection [p. 128]:
    $$\mathbb{P}\{\tau_1 = 2j - 1\} = \frac{(2j - 2)!}{j!(j - 1)!} \left(\frac{1}{2}\right)^{2j-1}, \quad j = 1, 2, \dots$$
  * Symmetric Joint Distribution of Walk and Maximum [Exercise 5.5(i), p. 140]:
    $$\mathbb{P}\{M_n^* \ge m, M_n = b\} = \mathbb{P}\{M_n = 2m - b\} = \frac{n!}{\left(\frac{n-b}{2} + m\right)! \left(\frac{n+b}{2} - m\right)!} \left(\frac{1}{2}\right)^n$$
  * Asymmetric Joint Distribution of Walk and Maximum [Exercise 5.5(ii), p. 140]:
    $$\mathbb{P}\{M_n^* \ge m, M_n = b\} = \frac{n!}{\left(\frac{n-b}{2} + m\right)! \left(\frac{n+b}{2} - m\right)!} p^{\frac{n+2m-b}{2}} q^{\frac{n-(2m-b)}{2}}$$

---

## 4. Assumptions and Domain of Validity

* **Symmetry Requirement for Direct Path Reflection**:
  * The direct reflection principle argument relies strictly on a **symmetric random walk** ($p = q = 1/2$), where every path of length $n$ has equal probability $(1/2)^n$, making path counting directly proportional to probability [pp. 127–128].
  * For an **asymmetric random walk** ($p \ne q$), path reflection cannot be applied directly to probabilities because reflecting a path changes its number of up and down steps (and hence its probability $p^{\#\text{up}} q^{\#\text{down}}$). The asymmetric joint distribution is obtained by weighting the combinatorial path count by the specific path probability $p^{\frac{n+2m-b}{2}} q^{\frac{n-(2m-b)}{2}}$ [Exercise 5.5(ii), p. 140].

* **Domain Restrictions in Exercise 5.5**:
  * $n$ and $m$ are positive even integers [p. 140].
  * $b$ is an even integer such that $b \le m$ [p. 140].
  * Parity and reachability constraints: $m \le n$ and $2m - b \le n$ [p. 140].

---

## 5. Theorems and Proof Outline

Section 5.3 does not introduce a new numbered theorem; it provides a **combinatoric proof of Theorem 5.2.5** (re-deriving formula (5.2.22) for $p=q=1/2$) [pp. 127–128].

### **Proof Outline of Theorem 5.2.5 via the Reflection Principle** [pp. 127–128]:

1. **Path Partitioning**: Consider $2j - 1$ coin tosses. A path reaches level $1$ by time $2j - 1$ ($\tau_1 \le 2j - 1$) if and only if it falls into one of three mutually exclusive categories at final time $2j - 1$:
   * It ends exactly at level $1$ ($M_{2j-1} = 1$).
   * It ends strictly above level $1$ ($M_{2j-1} \ge 3$).
   * It reaches level $1$ at or before time $2j - 1$ but ends strictly below level $1$ ($M_{2j-1} \le -1$).
2. **Reflection Bijection**: For any path that reaches level $1$ at time $\tau_1 \le 2j - 1$ and ends below level $1$ at time $2j - 1$, reflecting the path after $\tau_1$ produces a unique path that ends strictly above level $1$ ($M_{2j-1} \ge 3$). This establishes a $1$-to-$1$ correspondence between paths that reach level $1$ and end below $1$, and paths that end above $1$.
3. **Probability Accounting**:
   $$\mathbb{P}\{\tau_1 \le 2j - 1\} = \mathbb{P}\{M_{2j-1} = 1\} + 2 \mathbb{P}\{M_{2j-1} \ge 3\}$$
   By symmetry of the random walk, $\mathbb{P}\{M_{2j-1} \ge 3\} = \mathbb{P}\{M_{2j-1} \le -3\}$. Since the sum of all path probabilities is $1$:
   $$1 = \mathbb{P}\{M_{2j-1} = 1\} + \mathbb{P}\{M_{2j-1} = -1\} + \mathbb{P}\{M_{2j-1} \ge 3\} + \mathbb{P}\{M_{2j-1} \le -3\}$$
   Substituting yields the simplified identity:
   $$\mathbb{P}\{\tau_1 \le 2j - 1\} = 1 - \mathbb{P}\{M_{2j-1} = -1\}$$
4. **Path Count Evaluation**: To have $M_{2j-1} = -1$, a path of length $2j-1$ must have $j-1$ up-steps and $j$ down-steps. There are $\binom{2j-1}{j} = \frac{(2j-1)!}{j!(j-1)!}$ such paths, each having probability $(1/2)^{2j-1}$:
   $$\mathbb{P}\{M_{2j-1} = -1\} = \frac{(2j-1)!}{j!(j-1)!} \left(\frac{1}{2}\right)^{2j-1}$$
5. **Differencing for Exact Step Probability**: The probability of reaching level $1$ *for the first time* at step $2j - 1$ is:
   $$\mathbb{P}\{\tau_1 = 2j - 1\} = \mathbb{P}\{\tau_1 \le 2j - 1\} - \mathbb{P}\{\tau_1 \le 2j - 3\} = \mathbb{P}\{M_{2j-3} = -1\} - \mathbb{P}\{M_{2j-1} = -1\}$$
   Simplifying $\frac{(2j-3)!}{(j-1)!(j-2)!} (1/2)^{2j-3} - \frac{(2j-1)!}{j!(j-1)!} (1/2)^{2j-1}$ yields:
   $$\mathbb{P}\{\tau_1 = 2j - 1\} = \frac{(2j - 2)!}{j!(j - 1)!} \left(\frac{1}{2}\right)^{2j-1} \quad \blacksquare$$
6. **Worked Illustration (Figure 5.3.1, 3 tosses, $j=2$)** [p. 128]:
   * Among 8 paths of length 3, 5 reach level 1 ($HHH, HHT, HTH, THH, HTT$).
   * $HHH$ ends at $3 > 1$; $HHT, HTH, THH$ end at $1$; $HTT$ reaches $1$ at step $1$ and ends at $-1$.
   * Reflecting $HTT$ after step $1$ yields $HHH$ (which ends at $3 > 1$), confirming the $1$-to-$1$ match.

---

## 6. Exercises in This Section

* **Exercise 5.4 (part (ii) ONLY)** [p. 140]:
  *(Note: Part (i) of Exercise 5.4 was covered in Card 14).*
  > **(ii)** Use the reflection principle to determine $\mathbb{P}\{\tau_2 = 2k\}, k = 1, 2, \dots$.

* **Exercise 5.5 (Complete)** [p. 140]:
  > **Exercise 5.5 (Joint distribution of random walk and maximum-to-date).**
  > Let $M_n$ be a symmetric random walk, and define its maximum-to-date process
  > $$M_n^* = \max_{1 \le k \le n} M_k \quad \text{(5.7.2)}$$
  > Let $n$ and $m$ be even positive integers, and let $b$ be an even integer less than or equal to $m$. Assume $m \le n$ and $2m - b \le n$.
  > **(i)** Use an argument based on reflected paths to show that
  > $$\mathbb{P}\{M_n^* \ge m, M_n = b\} = \mathbb{P}\{M_n = 2m - b\} = \frac{n!}{\left(\frac{n-b}{2} + m\right)! \left(\frac{n+b}{2} - m\right)!} \left(\frac{1}{2}\right)^n$$
  > **(ii)** If the random walk is asymmetric with probability $p$ for an up step and probability $q = 1 - p$ for a down step, where $0 < p < 1$, what is $\mathbb{P}\{M_n^* \ge m, M_n = b\}$?

---

## 7. Cross-References

* **Section 5.2 & Card 14**: Provides the moment-generating function proof of Theorem 5.2.5 (formula (5.2.22)), which Section 5.3 re-derives combinatorially.
* **Volume II, Chapter 7**: The reflection principle established here for discrete random walk paths is extended to Brownian motion to derive closed-form pricing formulas for continuous-time barrier and lookback exotic options.