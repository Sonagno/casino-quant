from casino_quant.roulette import simulate_roulette

def test_shapes():
    res = simulate_roulette(100, bet="red", stake=1.0, seed=0)
    assert len(res.spins) == 100
    assert len(res.pnl) == 100

def test_var_positive():
    res = simulate_roulette(1000, bet="red", stake=1.0, seed=0)
    assert res.var_95 >= 0
