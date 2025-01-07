
---

## Contents Overview

### 1. `demos/`
Contains all individual demonstration projects. Each sub-folder is self-contained:

1. **historical_var_demo/**
   - `compute_var.py`: Shows how to calculate Value at Risk (VaR) via Historical Simulation, downloading data (if desired) and using historical returns.
   - `utils.py`: Helper functions (e.g., data loading, processing).
   - `README.md`: Explains how to run and interpret the VaR demo.

2. **sharpe_ratio_demo/**
   - `sharpe_ratio_demo.py`: Demonstrates how to compute the **annualized Sharpe Ratio**, including data fetching and risk-free rate adjustments.
   - `utils.py`: Helper functions for processing daily returns, date handling, etc.
   - `README.md`: Provides usage instructions for the Sharpe Ratio demo.

There is also a `README.md` directly under `demos/` which can include general notes about the structure of the demos folder.

### 2. `scripts/`
- This folder can host additional or utility scripts that are not part of a specific demo.
- For example, a script to **batch-run** multiple demos, fetch data in bulk, or test environment setups.

### 3. Top-Level `README.md` (This File)
Provides an overview of the entire project, usage instructions, and references to the subfolders.

---


