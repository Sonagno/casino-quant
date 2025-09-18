"""
Roulette Monte Carlo simulator + simple risk metrics.
European roulette: numbers 0-36 (single zero). Even-money bets: red/black, even/odd, high/low.
"""
from __future__ import annotations
import numpy as np
from dataclasses import dataclass
from typing import Literal, Tuple

EvenMoneyBet = Literal["red", "black", "even", "odd", "high", "low"]

# European roulette: red numbers list
RED_NUMBERS = {
    1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36
}

@dataclass
class RouletteResult:
    spins: np.ndarray           # landed numbers
    pnl: np.ndarray             # profit and loss per spin
    total_pnl: float            # sum of pnl
    mean_pnl: float             # average per spin
    std_pnl: float              # std per spin
    var_95: float               # Value-at-Risk at 95% (loss is positive, returned as positive number)
    es_95: float                # Expected Shortfall at 95%

def spin_wheel(n: int, rng: np.random.Generator | None = None) -> np.ndarray:
    rng = np.random.default_rng() if rng is None else rng
    # 37 pockets: 0..36
    return rng.integers(0, 37, size=n)

def is_win(number: int, bet: EvenMoneyBet) -> bool:
    if bet == "red":
        return number in RED_NUMBERS
    if bet == "black":
        return number != 0 and number not in RED_NUMBERS
    if bet == "even":
        return number != 0 and number % 2 == 0
    if bet == "odd":
        return number % 2 == 1
    if bet == "high":
        return number >= 19
    if bet == "low":
        return 1 <= number <= 18
    raise ValueError(f"Unknown bet: {bet}")

def simulate_roulette(n_spins: int, bet: EvenMoneyBet = "red", stake: float = 1.0, seed: int | None = None) -> RouletteResult:
    rng = np.random.default_rng(seed)
    spins = spin_wheel(n_spins, rng)
    wins = np.fromiter((is_win(x, bet) for x in spins), dtype=bool, count=n_spins)
    # Even-money bets pay +stake when win, lose stake when lose
    pnl = np.where(wins, stake, -stake).astype(float)

    total = float(pnl.sum())
    mean = float(pnl.mean())
    std = float(pnl.std(ddof=1)) if n_spins > 1 else 0.0

    # VaR/ES 95% on losses (positive number). Convert pnl to losses: L = -pnl
    losses = -pnl
    if n_spins >= 20:
        var_95 = float(np.quantile(losses, 0.95))
        es_95 = float(losses[losses >= var_95].mean())
    else:
        # small-sample fallback
        var_95 = float(np.sort(losses)[int(0.95 * (n_spins - 1))])
        es_95 = float(losses.mean())
    return RouletteResult(spins=spins, pnl=pnl, total_pnl=total, mean_pnl=mean, std_pnl=std, var_95=var_95, es_95=es_95)
