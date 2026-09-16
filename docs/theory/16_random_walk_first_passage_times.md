## 1. Concept and context

Section 5.1 introduces the symmetric random walk $M_n$, the discrete-time
version of Brownian motion (introduced in Chapter 3 of Volume II). Section
5.2 studies the first passage time $\tau_m$, the first time the walk reaches
a fixed nonzero level $m$: whether the walk eventually reaches $m$ at all,
how long this takes in expectation, and the exact probability distribution
of the hitting time. A central paradox of this section is that for a
symmetric random walk, $\tau_m$ is finite almost surely, yet its expectation
is infinite (Section 5.2, pp. 120–126).

## 2. Formal definitions

* **$X_j$**: outcome of the $j$-th coin toss, $X_j=1$ if $\omega_j=H$ and
  $X_j=-1$ if $\omega_j=T$ (Eq. 5.1.1).
* **$M_n$**: the random walk itself, $M_0=0$ and $M_n=\sum_{j=1}^n X_j$
  (Eq. 5.1.2). It is symmetric when $p=q=1/2$ and asymmetric otherwise; both
  cases share the same set of possible paths and differ only in the
  probabilities assigned to them. The symmetric random walk is both a
  martingale and a Markov process (Section 5.1, p. 120).
* **$\tau_m$**: the first passage time to level $m$, $\tau_m=\min\{n:M_n=m\}$,
  taken to be $\infty$ if the walk never reaches $m$; it is a stopping time
  (Eq. 5.2.1, p. 120).
* **$S_n$**: the exponential martingale process used to study $\tau_m$, for a
  fixed parameter $\sigma$: $S_n=e^{\sigma M_n}\left(\frac{2}{e^\sigma+e^{-\sigma}}\right)^n$
  (Lemma 5.2.1, Eq. 5.2.2).
* **$\varphi_{\tau_m}(u)$**: the moment-generating function of $\tau_m$,
  $\varphi_{\tau_m}(u)=\mathbb{E}e^{u\tau_m}$; it is interesting only for
  $u<0$, where the substitution $\alpha=e^u\in(0,1)$ gives
  $\varphi_{\tau_m}(u)=\mathbb{E}\alpha^{\tau_m}$ (p. 123).
* **$f(x)$**: the auxiliary function $f(x)=1-\sqrt{1-x}$, whose Taylor
  expansion at $0$ is used to extract the exact distribution of $\tau_1$
  (p. 125).

## 3. Key equations

$$X_j = \begin{cases} 1, & \text{if } \omega_j = H, \\ -1, & \text{if } \omega_j = T, \end{cases} \quad \text{(5.1.1)}$$

$$M_0 = 0, \quad M_n = \sum_{j=1}^n X_j, \quad n=1,2,\dots \quad \text{(5.1.2)}$$

$$\tau_m = \min\{n; M_n = m\} \quad \text{(5.2.1)}$$

$$S_n = e^{\sigma M_n}\left(\frac{2}{e^\sigma+e^{-\sigma}}\right)^n \quad \text{(5.2.2)}$$

$$1 = S_0 = \mathbb{E}S_{n\wedge\tau_m} = \mathbb{E}\left[e^{\sigma M_{n\wedge\tau_m}}\left(\frac{2}{e^\sigma+e^{-\sigma}}\right)^{n\wedge\tau_m}\right] \text{ for all } n\ge 0 \quad \text{(5.2.3)}$$

$$0 < \frac{2}{e^\sigma+e^{-\sigma}} < 1 \text{ for all } \sigma>0 \quad \text{(5.2.4)}$$

$$\lim_{n\to\infty}\left(\frac{2}{e^\sigma+e^{-\sigma}}\right)^{n\wedge\tau_m} = \begin{cases} \left(\frac{2}{e^\sigma+e^{-\sigma}}\right)^{\tau_m}, & \text{if } \tau_m<\infty, \\ 0, & \text{if } \tau_m=\infty, \end{cases} \quad \text{(5.2.5)}$$

$$0 \le e^{\sigma M_{n\wedge\tau_m}} \le e^{\sigma m} \quad \text{(5.2.6)}$$

$$\lim_{n\to\infty} e^{\sigma M_{n\wedge\tau_m}} = e^{\sigma M_{\tau_m}} = e^{\sigma m} \text{ if } \tau_m<\infty \quad \text{(5.2.7)}$$

$$\lim_{n\to\infty} e^{\sigma M_{n\wedge\tau_m}}\left(\frac{2}{e^\sigma+e^{-\sigma}}\right)^{n\wedge\tau_m} = e^{\sigma m}\left(\frac{2}{e^\sigma+e^{-\sigma}}\right)^{\tau_m} \text{ if } \tau_m<\infty \quad \text{(5.2.8)}$$

$$\lim_{n\to\infty} e^{\sigma M_{n\wedge\tau_m}}\left(\frac{2}{e^\sigma+e^{-\sigma}}\right)^{n\wedge\tau_m} = 0 \text{ if } \tau_m=\infty \quad \text{(5.2.9)}$$

$$\lim_{n\to\infty} e^{\sigma M_{n\wedge\tau_m}}\left(\frac{2}{e^\sigma+e^{-\sigma}}\right)^{n\wedge\tau_m} = \mathbb{I}_{\{\tau_m<\infty\}}\, e^{\sigma m}\left(\frac{2}{e^\sigma+e^{-\sigma}}\right)^{\tau_m} \quad \text{(5.2.10)}$$

$$\mathbb{E}\left[\mathbb{I}_{\{\tau_m<\infty\}}\, e^{\sigma m}\left(\frac{2}{e^\sigma+e^{-\sigma}}\right)^{\tau_m}\right] = 1 \quad \text{(5.2.11)}$$

$$\mathbb{P}\{\tau_m<\infty\} = 1 \quad \text{(5.2.12)}$$

$$\mathbb{E}\alpha^{\tau_m} = \left(\frac{1-\sqrt{1-\alpha^2}}{\alpha}\right)^{|m|} \text{ for all } \alpha\in(0,1) \quad \text{(5.2.13)}$$

$$\mathbb{E}\left[e^{\sigma m}\left(\frac{2}{e^\sigma+e^{-\sigma}}\right)^{\tau_m}\right] = 1 \quad \text{(5.2.14)}$$

$$\alpha = \frac{2}{e^\sigma+e^{-\sigma}} \quad \text{(5.2.15)}$$

$$e^{-\sigma} = \frac{1-\sqrt{1-\alpha^2}}{\alpha} \quad \text{(5.2.16)}$$

$$\mathbb{E}\tau_m = \infty \quad \text{(5.2.17)}$$

$$\mathbb{E}\alpha^{\tau_1} = \frac{1-\sqrt{1-\alpha^2}}{\alpha} \text{ for all } \alpha\in(0,1) \quad \text{(5.2.18)}$$

$$\mathbb{E}\alpha^{\tau_1} = \sum_{j=1}^\infty \alpha^{2j-1}\,\mathbb{P}\{\tau_1=2j-1\} \quad \text{(5.2.19)}$$

$$f^{(j)}(0) = \left(\frac12\right)^{2j-1}\frac{(2j-2)!}{(j-1)!}, \quad j=1,2,3,\dots \quad \text{(5.2.20)}$$

$$\frac{1-\sqrt{1-\alpha^2}}{\alpha} = \frac{f(\alpha^2)}{\alpha} = \sum_{j=1}^\infty \left(\frac{\alpha}{2}\right)^{2j-1}\frac{(2j-2)!}{j!(j-1)!} \quad \text{(5.2.21)}$$

$$\mathbb{P}\{\tau_1=2j-1\} = \frac{(2j-2)!}{j!(j-1)!}\left(\frac12\right)^{2j-1}, \quad j=1,2,\dots \quad \text{(5.2.22)}$$

$$\mathbb{P}\{\tau_1=2j-1\} = \frac{(2j-2)!}{j!(j-1)!}\,p^j q^{j-1}, \quad j=1,2,\dots \quad \text{(5.2.23)}$$

*Unnumbered formulas in the text:* the moment-generating function definition
$\varphi_{\tau_m}(u)=\mathbb{E}e^{u\tau_m}$ and the substitution $\alpha=e^u\in(0,1)$
for $u<0$ (p. 123); the quadratic equation in $e^{-\sigma}$,
$\alpha(e^{-\sigma})^2-2e^{-\sigma}+\alpha=0$, solved to obtain (5.2.16) (p. 123);
the derivative $\frac{d}{d\alpha}\mathbb{E}\alpha^{\tau_1}=\frac{1-\sqrt{1-\alpha^2}}{\alpha^2\sqrt{1-\alpha^2}}$
used in the proof of Corollary 5.2.4 (p. 124); and the first three explicit
probability values $\mathbb{P}\{\tau_1=1\}=1/2$, $\mathbb{P}\{\tau_1=3\}=(1/2)^3$,
$\mathbb{P}\{\tau_1=5\}=2\cdot(1/2)^5$ verifying (5.2.22) (p. 126).

## 4. Assumptions and domain of validity

* **Symmetric-only results:** Lemma 5.2.1, Theorem 5.2.2
  ($\mathbb{P}\{\tau_m<\infty\}=1$), Theorem 5.2.3 (the moment-generating
  function (5.2.13)), and Corollary 5.2.4 ($\mathbb{E}\tau_m=\infty$) all
  require the symmetric random walk ($p=q=1/2$).
* **Generalization to the asymmetric walk:** Theorem 5.2.5 extends the
  distribution of $\tau_1$ to an arbitrary up-step probability $p$ and
  down-step probability $q=1-p$ (Eq. 5.2.23). Exercises 5.2 and 5.3 extend
  the finiteness and expectation results themselves: with upward drift
  ($p>1/2$), $\mathbb{P}\{\tau_m<\infty\}=1$ and $\mathbb{E}\tau_m<\infty$;
  with downward drift ($p<1/2$), $\mathbb{P}\{\tau_m<\infty\}<1$ and
  $\mathbb{E}\tau_m=\infty$.
* **Domain restrictions:** $m$ must be a nonzero integer; $\sigma>0$ for the
  martingale $S_n$ of Eq. (5.2.2); $\alpha\in(0,1)$ throughout the
  moment-generating-function derivation; $\tau_1$ can only take odd values
  $2j-1$, $j=1,2,\dots$, since level 1 cannot be reached on an even step.

## 5. Theorems and proof outline

**Lemma 5.2.1:** Let $M_n$ be a symmetric random walk. Fix a number $\sigma$
and define $S_n=e^{\sigma M_n}\left(\frac{2}{e^\sigma+e^{-\sigma}}\right)^n$.
Then $S_n$, $n=0,1,2,\dots$ is a martingale.

*Proof outline:*

1. Write $S_{n+1}=S_n\left(\frac{2}{e^\sigma+e^{-\sigma}}\right)e^{\sigma X_{n+1}}$.
2. Take out what is known (Theorem 2.3.2(ii)) to factor $S_n$ outside the
   conditional expectation.
3. Use independence (Theorem 2.3.2(iv)), since $X_{n+1}$ depends only on the
   $(n+1)$-st toss.
4. Compute $\mathbb{E}e^{\sigma X_{n+1}}=\frac12e^\sigma+\frac12e^{-\sigma}$.
5. Multiply by $\frac{2}{e^\sigma+e^{-\sigma}}$ to obtain
   $\mathbb{E}_nS_{n+1}=S_n$.

**Theorem 5.2.2:** Let $m$ be an arbitrary nonzero integer. The symmetric
random walk reaches the level $m$ almost surely; i.e., $\tau_m$ is finite
almost surely.

*Proof outline:*

1. Because a martingale stopped at a stopping time is still a martingale
   (Theorem 4.3.2), $S_{n\wedge\tau_m}$ has constant expectation $1$ for
   every $n$ (Eq. 5.2.3).
2. For fixed $\sigma>0$, $\frac{2}{e^\sigma+e^{-\sigma}}<1$ (Eq. 5.2.4), so its
   $(n\wedge\tau_m)$-th power converges as $n\to\infty$ to itself raised to
   $\tau_m$ if $\tau_m<\infty$, and to $0$ if $\tau_m=\infty$ (Eq. 5.2.5).
3. For $m>0$, $M_{n\wedge\tau_m}\le m$, so $e^{\sigma M_{n\wedge\tau_m}}$ is
   bounded (Eq. 5.2.6) and converges to $e^{\sigma m}$ when $\tau_m<\infty$
   (Eq. 5.2.7).
4. Combining both limits gives $\mathbb{I}_{\{\tau_m<\infty\}}e^{\sigma m}\left(\frac{2}{e^\sigma+e^{-\sigma}}\right)^{\tau_m}$
   as the limit of the integrand (Eq. 5.2.10); taking expectations under
   this limit (justified by Dominated Convergence) gives Eq. (5.2.11).
5. Letting $\sigma\downarrow0$ in (5.2.11) gives $\mathbb{E}\mathbb{I}_{\{\tau_m<\infty\}}=1$,
   i.e. $\mathbb{P}\{\tau_m<\infty\}=1$ (Eq. 5.2.12). By symmetry the same
   conclusion holds for $m<0$.

**Theorem 5.2.3:** Let $m$ be a nonzero integer. The first passage time
$\tau_m$ for the symmetric random walk satisfies Eq. (5.2.13) for all
$\alpha\in(0,1)$.

*Proof outline:*

1. By symmetry it suffices to prove the case $m>0$. Since
   $\mathbb{P}\{\tau_m<\infty\}=1$, Eq. (5.2.11) simplifies to Eq. (5.2.14),
   valid for all $\sigma>0$.
2. Given $\alpha\in(0,1)$, solve $\alpha=\frac{2}{e^\sigma+e^{-\sigma}}$
   (Eq. 5.2.15) for $\sigma>0$; this is a quadratic equation in $e^{-\sigma}$
   with roots $e^{-\sigma}=\frac{1\pm\sqrt{1-\alpha^2}}{\alpha}$.
3. The root corresponding to $\sigma>0$ (i.e. $e^{-\sigma}<1$) is the one
   with the minus sign, giving Eq. (5.2.16); one verifies this root is
   strictly between $0$ and $1$ for every $\alpha\in(0,1)$.
4. Substituting back into (5.2.14) and dividing through by the nonrandom
   factor $\left(\frac{\alpha}{1-\sqrt{1-\alpha^2}}\right)^m$ yields
   Eq. (5.2.13) for positive $m$.

**Corollary 5.2.4:** Under the conditions of Theorem 5.2.3, $\mathbb{E}\tau_m=\infty$.

*Proof outline:*

1. Differentiate both sides of (5.2.13) with $m=1$ with respect to $\alpha$
   to get $\mathbb{E}[\tau_1\alpha^{\tau_1-1}]=\frac{1-\sqrt{1-\alpha^2}}{\alpha^2\sqrt{1-\alpha^2}}$.
2. Let $\alpha\uparrow1$; the right-hand side diverges, so
   $\mathbb{E}\tau_1=\infty$ (justified by Monotone Convergence).
3. For $m\ge1$, $\tau_m\ge\tau_1$, so $\mathbb{E}\tau_m\ge\mathbb{E}\tau_1=\infty$.
   By symmetry the same holds for negative $m$.

**Theorem 5.2.5:** Let $\tau_1$ be the first passage time to level 1 of a
random walk with probability $p$ for an up step and $q=1-p$ for a down step.
Then Eq. (5.2.23) holds for $j=1,2,\dots$.

*Proof outline:*

1. For the symmetric walk, equating the power series (5.2.19) with the
   Taylor expansion (5.2.21) term-by-term gives the exact distribution
   (5.2.22).
2. Any path first reaching level 1 at step $2j-1$ has exactly $j$ up steps
   and $j-1$ down steps; the combinatorial factor $\frac{(2j-2)!}{j!(j-1)!}$
   in (5.2.22) counts these paths and is unaffected by the value of $p$.
3. Replacing the symmetric path probability $(1/2)^{2j-1}$ with the
   asymmetric path probability $p^jq^{j-1}$ while keeping the same
   combinatorial count gives Eq. (5.2.23).

## 6. Exercises in this section

* **Exercise 5.1:** For the symmetric random walk, $\tau_2-\tau_1$ is the
  number of steps needed to rise from level 1 to level 2, has the same
  distribution as $\tau_1$, and is independent of $\tau_1$. (i) Use this to
  explain why $\mathbb{E}\alpha^{\tau_2}=(\mathbb{E}\alpha^{\tau_1})^2$ for all
  $\alpha\in(0,1)$. (ii) Without using (5.2.13), explain why for any
  positive integer $m$, $\mathbb{E}\alpha^{\tau_m}=(\mathbb{E}\alpha^{\tau_1})^m$
  (Eq. 5.7.1). (iii) Would (5.7.1) still hold if the random walk is not
  symmetric? Explain why or why not.
* **Exercise 5.2 (First passage time for random walk with upward drift):**
  Consider the asymmetric random walk with $\frac12<p<1$, $q=1-p$, and let
  $\tau_1$ be the first time the walk reaches level 1 from 0 (or $\infty$ if
  it never does). (i) Define $f(\sigma)=pe^\sigma+qe^{-\sigma}$; show
  $f(\sigma)>1$ for all $\sigma>0$. (ii) Show that for $\sigma>0$,
  $S_n=e^{\sigma M_n}\left(\frac{1}{f(\sigma)}\right)^n$ is a martingale.
  (iii) Show that $e^{-\sigma}=\mathbb{E}\left[\mathbb{I}_{\{\tau_1<\infty\}}\left(\frac{1}{f(\sigma)}\right)^{\tau_1}\right]$
  for $\sigma>0$, and conclude $\mathbb{P}\{\tau_1<\infty\}=1$.
  (iv) Compute $\mathbb{E}\alpha^{\tau_1}$ for $\alpha\in(0,1)$.
  (v) Compute $\mathbb{E}\tau_1$.
* **Exercise 5.3 (First passage time for random walk with downward drift):**
  Modify Exercise 5.2 assuming $0<p<\frac12$, $\frac12<q<1$. (i) Find
  $\sigma_0>0$ such that $f(\sigma_0)=1$ and $f(\sigma)>1$ for all
  $\sigma>\sigma_0$. (ii) Determine $\mathbb{P}\{\tau_1<\infty\}$ (no longer
  equal to 1). (iii) Compute $\mathbb{E}\alpha^{\tau_1}$ for $\alpha\in(0,1)$.
  (iv) Compute $\mathbb{E}[\mathbb{I}_{\{\tau_1<\infty\}}\tau_1]$ (since
  $\mathbb{P}\{\tau_1=\infty\}>0$, $\mathbb{E}\tau_1=\infty$).
* **Exercise 5.4(i) (Distribution of $\tau_2$):** Let $\tau_2$ be the first
  time the symmetric random walk reaches level 2. By Theorem 5.2.3,
  $\mathbb{E}\alpha^{\tau_2}=\left(\frac{1-\sqrt{1-\alpha^2}}{\alpha}\right)^2$,
  which the power series (5.2.21) rewrites as
  $\sum_{k=1}^\infty\left(\frac{\alpha}{2}\right)^{2k}\frac{(2k)!}{(k+1)!k!}$.
  Use this power series to determine $\mathbb{P}\{\tau_2=2k\}$,
  $k=1,2,\dots$. (Part (ii) of this exercise, which uses the reflection
  principle of Section 5.3, is treated in the next theory card.)

## 7. Cross-references

* **Theorem 2.3.2 (Chapter 2, p. 34):** "Taking out what is known" (ii) and
  independence (iv) are used directly in the proof of Lemma 5.2.1.
* **Exercise 2.4(ii) (Chapter 2, p. 55):** Already introduces the
  exponential martingale process of Eq. (5.2.2).
* **Theorem 4.3.2 (Chapter 4, Section 4.3):** Optional sampling for a
  stopped martingale, used to obtain Eq. (5.2.3) at the start of the proof
  of Theorem 5.2.2.
* **Section 5.3 (Reflection Principle):** Gives a second, purely
  combinatorial proof of Theorem 5.2.5, and also solves part (ii) of
  Exercise 5.4.
* **Section 5.4 (Perpetual American Put):** Applies Theorem 5.2.3 directly,
  with $\alpha=\frac{1}{1+r}$, to evaluate the risk-neutral discounted
  payoff of each candidate exercise policy $\tau_{-m}$.