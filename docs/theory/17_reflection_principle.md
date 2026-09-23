## 1. Concept and context

Section 5.3 gives a second, purely combinatorial proof of Theorem 5.2.5 (the
distribution of the first passage time $\tau_1$, established via
moment-generating functions in the previous card). The reflection principle
provides a geometric path-counting argument instead: every path that reaches
level 1 by a given time but ends below it corresponds bijectively to a
"reflected" path that ends above level 1. The book notes that this same
reflection idea will be reused later in the study of Brownian motion
(Section 5.3, p. 127).

## 2. Formal definitions

* **Reflected path**: for a path $M_0,\dots,M_{2j-1}$ that reaches level 1
  at some first passage time $\tau_1\le2j-1$, the reflected path keeps the
  original path up to $\tau_1$ and flips every step afterward (an up-step
  becomes a down-step and vice versa) (p. 127).
* **$M_n^*$**: the maximum-to-date process of a random walk $M_k$,
  $M_n^*=\max_{1\le k\le n}M_k$, introduced in Exercise 5.5 (Eq. 5.7.2).

## 3. Key equations

Section 5.3 itself contains no equations numbered by the author — the whole
section is a prose-and-diagram combinatorial argument that re-derives
(5.2.22) from the previous card without assigning it a new number. The only
numbered equation belonging to this card comes from Exercise 5.5:

$$M_n^* = \max_{1\le k\le n} M_k \quad \text{(5.7.2)}$$

*Unnumbered formulas worked out in the text:* the path-partition identity

$$\mathbb{P}\{\tau_1\le2j-1\} = \mathbb{P}\{M_{2j-1}=1\} + 2\,\mathbb{P}\{M_{2j-1}\ge3\} = 1-\mathbb{P}\{M_{2j-1}=-1\}$$

the path count

$$\mathbb{P}\{M_{2j-1}=-1\} = \binom{2j-1}{j}\left(\frac12\right)^{2j-1} = \frac{(2j-1)!}{j!(j-1)!}\left(\frac12\right)^{2j-1}$$

and the resulting re-derivation of (5.2.22),

$$\mathbb{P}\{\tau_1=2j-1\} = \frac{(2j-2)!}{j!(j-1)!}\left(\frac12\right)^{2j-1} \quad (p.\ 128)$$

The formula asked for in Exercise 5.5(i) is

$$\mathbb{P}\{M_n^*\ge m,\, M_n=b\} = \mathbb{P}\{M_n=2m-b\} = \frac{n!}{\left(\frac{n-b}{2}+m\right)!\left(\frac{n+b}{2}-m\right)!}\left(\frac12\right)^n \quad (p.\ 140)$$

Part (ii) of that same exercise only asks for the asymmetric analogue of
this formula and does not supply one — it is an open question, not a
result given in the text.

## 4. Assumptions and domain of validity

* The direct path-reflection argument requires the symmetric random walk
  ($p=q=1/2$), where every path of a given length shares the same
  probability $(1/2)^n$, so counting paths is equivalent to computing
  probabilities.
* Exercise 5.5 restricts $n$ and $m$ to even positive integers and $b$ to
  an even integer with $b\le m$, and requires $m\le n$ and $2m-b\le n$ so
  that level $m$ and endpoint $b$ are jointly attainable in $n$ steps.

## 5. Theorems and proof outline

This section introduces no new numbered theorem — it gives a second,
combinatorial proof of Theorem 5.2.5 (stated in the previous card) for the
symmetric random walk.

*Proof outline:*

1. Fix $2j-1$ tosses. A path reaches level 1 by time $2j-1$ exactly when it
   falls into one of three cases at the final time: it ends at 1
   ($M_{2j-1}=1$), it ends strictly above 1 ($M_{2j-1}\ge3$), or it reaches
   1 at some point but ends strictly below 1 ($M_{2j-1}\le-1$).
2. Reflecting a path after its first passage time $\tau_1$ turns every path
   that reaches 1 and ends below 1 into a unique path ending above 1, and
   vice versa — a bijection between the two families.
3. This gives $\mathbb{P}\{\tau_1\le2j-1\}=\mathbb{P}\{M_{2j-1}=1\}+2\mathbb{P}\{M_{2j-1}\ge3\}$;
   using symmetry ($\mathbb{P}\{M_{2j-1}\ge3\}=\mathbb{P}\{M_{2j-1}\le-3\}$)
   and that all four probabilities sum to 1, this simplifies to
   $\mathbb{P}\{\tau_1\le2j-1\}=1-\mathbb{P}\{M_{2j-1}=-1\}$.
4. Reaching $M_{2j-1}=-1$ requires exactly $j-1$ up-steps and $j$
   down-steps out of $2j-1$ tosses, so
   $\mathbb{P}\{M_{2j-1}=-1\}=\binom{2j-1}{j}(1/2)^{2j-1}$.
5. Differencing, $\mathbb{P}\{\tau_1=2j-1\}=\mathbb{P}\{\tau_1\le2j-1\}-\mathbb{P}\{\tau_1\le2j-3\}=\mathbb{P}\{M_{2j-3}=-1\}-\mathbb{P}\{M_{2j-1}=-1\}$;
   substituting the binomial counts for $2j-3$ and $2j-1$ tosses and
   simplifying algebraically recovers (5.2.22).
6. The book illustrates this with three tosses ($j=2$): among the 8 paths,
   5 reach level 1 (HHH, HHT, HTH, HTT, THH). HTT reaches 1 at step 1 and
   ends at $-1$; reflecting its remaining steps (T,T $\to$ H,H) gives
   exactly HHH, the one path ending above 1 — confirming the bijection
   (Figure 5.3.1).

## 6. Exercises in this section

* **Exercise 5.4(ii):** Using the power series from the previous card,
  $\mathbb{E}\alpha^{\tau_2}=\sum_{k=1}^\infty\left(\frac{\alpha}{2}\right)^{2k}\frac{(2k)!}{(k+1)!k!}$,
  use the reflection principle to determine $\mathbb{P}\{\tau_2=2k\}$,
  $k=1,2,\dots$.
* **Exercise 5.5 (Joint distribution of random walk and maximum-to-date):**
  Let $M_n$ be a symmetric random walk and $M_n^*=\max_{1\le k\le n}M_k$
  (Eq. 5.7.2). Let $n$ and $m$ be even positive integers and $b$ an even
  integer with $b\le m$; assume $m\le n$ and $2m-b\le n$.
  (i) Use an argument based on reflected paths to show that
  $\mathbb{P}\{M_n^*\ge m, M_n=b\}=\mathbb{P}\{M_n=2m-b\}=\frac{n!}{\left(\frac{n-b}{2}+m\right)!\left(\frac{n+b}{2}-m\right)!}\left(\frac12\right)^n$.
  (ii) If the random walk is instead asymmetric, with probability $p$ for
  an up step and $q=1-p$ for a down step, $0<p<1$, what is
  $\mathbb{P}\{M_n^*\ge m, M_n=b\}$?

## 7. Cross-references

* **Section 5.2 (previous card):** gives the moment-generating-function
  proof of Theorem 5.2.5 (Eq. 5.2.22), which this section re-derives
  combinatorially.
* **Brownian motion (Volume II):** the book states explicitly that this
  same reflection idea will be reused in the study of Brownian motion,
  without citing a specific chapter at this point.