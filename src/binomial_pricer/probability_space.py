import itertools
from dataclasses import dataclass

@dataclass(frozen=True)
class CoinTossSpace:
    """
    Formalizes the finite probability space for the multiperiod binomial model.
    Encapsulates Omega and the probability measure P (Sections 2.1 and 2.2).
    """
    n_periods: int
    p: float

    def __post_init__(self) -> None:
        """
        Validates the domain of the probability measure constraints.
        Probability strictly bounded in (0, 1) per Section 2.3 domain of validity.
        """
        if not (0.0 < self.p < 1.0):
            raise ValueError(f"Probability p must be in (0, 1). Got {self.p}")

    @property
    def q(self) -> float:
        return 1.0 - self.p

    def get_omega(self) -> list[str]:
        """
        Sample space Omega - a nonempty finite set whose elements omega
        represent the possible outcomes. 
        Uses Eq. (2.1.1).
        """
        if self.n_periods == 0:
            return [""]
        return ["".join(seq) for seq in itertools.product("HT", repeat=self.n_periods)]

    def probability(self, omega: str) -> float:
        """
        Probability measure assigning to each path in Omega a probability.
        Uses Eq. (2.1.2) and Eq. (2.3.6) logic (p^#H * q^#T).
        """
        h_count = omega.count('H')
        t_count = omega.count('T')
        return (self.p ** h_count) * (self.q ** t_count)

    def event_probability(self, event: set[str]) -> float:
        """
        Probability of an event A (any subset of Omega).
        Uses Eq. (2.1.5).
        """
        return sum(self.probability(w) for w in event)

    def distribution(self, x: dict[str, float]) -> dict[float, float]:
        """
        Distribution of a random variable X: probabilities that X takes
        each of its possible values, denoted P{X=j}.
        (p. 28-29, conceptually described).
        """
        dist: dict[float, float] = {}
        for omega, value in x.items():
            prob = self.probability(omega)
            dist[value] = dist.get(value, 0.0) + prob
        return dist

    def conditional_expectation(self, x: dict[str, float], n: int) -> dict[str, float]:
        """
        Conditional expectation of X based on information at time n.
        Uses Definition 2.3.1 and Eq. (2.3.6).
        """
        if not x:
            return {}
            
        m = len(next(iter(x.keys())))
        if not (0 <= n <= m <= self.n_periods):
            raise ValueError(f"Time index n={n} must be <= m={m} <= N={self.n_periods}")

        result = {}
        prefixes = [""] if n == 0 else ["".join(seq) for seq in itertools.product("HT", repeat=n)]
        continuations = [""] if n == m else ["".join(seq) for seq in itertools.product("HT", repeat=m - n)]

        for prefix in prefixes:
            expected_val = 0.0
            for cont in continuations:
                prob = self.probability(cont)
                expected_val += prob * x[prefix + cont]
            result[prefix] = expected_val
            
        return result

    def expectation(self, x: dict[str, float]) -> float:
        """
        Expectation of X (unconditional expectation).
        Uses Definition 2.2.4 and Eq. (2.3.7).
        """
        return self.conditional_expectation(x, 0)[""]

    def variance(self, x: dict[str, float]) -> float:
        """
        Variance of X (p. 29-30).
        Var(X) = E[(X - EX)^2]
        """
        ex = self.expectation(x)
        var_x = {omega: (val - ex)**2 for omega, val in x.items()}
        return self.expectation(var_x)