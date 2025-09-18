# 🎲 Casino Quant — Simuler, mesurer le risque, pricer

Projet fun et formateur : on simule des jeux de hasard (roulette, blackjack, etc.) pour illustrer des notions de finance quantitative (espérance, variance, Value-at-Risk, Monte Carlo, pricing).

## 🚀 Installation rapide (Windows/Mac/Linux)

1. **Cloner** ce dépôt (ou copiez les fichiers dans votre dossier du dépôt).
2. **Créer un environnement Python** :
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate
   ```
3. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Démarrer (exemple roulette)
```bash
python examples/run_roulette.py --n-spins 10000 --bet red --stake 1
```

## 📚 Contenu
- `src/casino_quant/roulette.py` : simulateur de roulette + métriques de risque
- `examples/run_roulette.py` : script d'exemple avec tracés
- `notebooks/01_roulette_monte_carlo.ipynb` : notebook introductif
- `tests/test_roulette.py` : tests unitaires simples

## 🧪 Idées d'extensions
- Ajouter **Blackjack** (stratégie basique vs aléatoire)
- Construire un **portefeuille de jeux** et calculer **VaR/ES**
- **Pricing** d'une option exotique liée aux gains d'un jeu (Monte Carlo)
- Backtesting d'une stratégie de mise (Martingale) et analyse du risque

## 💼 Pourquoi c'est vendeur
- Python propre + simulation + stats
- Visualisations claires
- Lien explicite avec la finance de marché (risque et pricing)


