#Import von Quartalsendstände
#Berechnung der Änderungen
#Durchschnitt der Rendite


import pandas as pd
import matplotlib.pyplot as plt

import numpy as np
#stock_data.csv muss importiert werden
path='stock_data.csv'
stock_data = pd.read_csv(path)
#print(stock_data)
selected = list(stock_data.columns[1:])
quarterly_returns = stock_data[selected].pct_change()
#rint(quarterly_returns)
expected_returns_avg = quarterly_returns.mean()









try:
  print(expected_returns_avg)
except:
  print('Calculate the average quarterly expected returns and save it to expected_returns_avg.')