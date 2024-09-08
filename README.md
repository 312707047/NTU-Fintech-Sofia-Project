# Crypto Trading with DQN and Its Variants

## 🚀 Overview

This project implements Deep Q-Network (DQN) and its advanced variants for cryptocurrency trading. It leverages reinforcement learning techniques to optimize trading strategies in the volatile crypto market.

## ✨ Features

- 🧠 Implementation of DQN (Deep Q-Network) for crypto trading
- 🔀 Advanced DQN variants:
  - Dueling DQN
  - Double DQN
  - CER DQN
- 📊 Data visualization for trading performance and model analysis
- 🔢 Numerical analysis using pandas and numpy
- 📈 Financial charting with mplfinance

## 🛠️ Installation

Ensure you have Python 3.7+ installed.

### Dependencies

This project relies on the following key packages:

```
pandas==1.3.4
matplotlib==3.5.0
matplotlib-inline==0.1.3
numpy==1.21.4
mplfinance==0.12.7a17
opencv-python==4.5.4.58
```

## 🖥️ Usage

To run the main trading simulation:

```bash
python main.py
```

You can customize the run by directly modifying the `main.py`

## 📊 Models

### DQN (Deep Q-Network)
The base model for our reinforcement learning approach to crypto trading.

### Dueling DQN
Separates state-value and advantage functions for more efficient learning.

### Double DQN
Reduces overestimation bias by decoupling action selection and evaluation.

### CER DQN
Implements CER DQN for taking every new observation to update the agent.

## 📈 Visualization

This project uses `matplotlib` and `mplfinance` for creating insightful visualizations:

- Trading performance over time
- Price charts with buy/sell signals

## 📚 References

1. Wang, Z., et al. (2016). Dueling Network Architectures for Deep Reinforcement Learning. ICML.
2. Van Hasselt, H., Guez, A., & Silver, D. (2016). Deep Reinforcement Learning with Double Q-learning. AAAI.
