import argparse
import numpy as np
import matplotlib.pyplot as plt
from casino_quant.roulette import simulate_roulette

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-spins", type=int, default=10000)
    parser.add_argument("--bet", type=str, default="red", choices=["red","black","even","odd","high","low"])
    parser.add_argument("--stake", type=float, default=1.0)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    res = simulate_roulette(args.n_spins, bet=args.bet, stake=args.stake, seed=args.seed)

    print(f"Total PnL: {res.total_pnl:.2f}")
    print(f"Mean per spin: {res.mean_pnl:.4f} | Std: {res.std_pnl:.4f}")
    print(f"VaR 95%: {res.var_95:.2f} | ES 95%: {res.es_95:.2f}")

    # Plot cumulative PnL
    cum = res.pnl.cumsum()
    plt.figure()
    plt.plot(cum)
    plt.title(f"Cumulative PnL — {args.n_spins} spins ({args.bet})")
    plt.xlabel("Spin")
    plt.ylabel("PnL (cumulative)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
