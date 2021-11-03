#mit Funktion Portfolios mit random Portfolios zusammenstellen

import pandas as pd
import matplotlib.pyplot as plt
from rf import return_portfolios

import numpy as np
import random

returns_quarterly = pd.read_csv('stock_data.csv')
expected_returns = returns_quarterly.mean()
cov_quarterly = returns_quarterly.cov()

random_portfolios = return_portfolios(expected_returns,cov_quarterly)
print(random_portfolios.head().round(4))
