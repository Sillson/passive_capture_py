from __future__ import print_function
from statsmodels.compat import lzip
import statsmodels
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.stats.api as sms
import matplotlib.pyplot as plt


def test_of_variance(csv,spp)
  
  # Load data
  dat = pd.read_csv(url)

  # Fit regression model
  results = smf.ols(df['count_date'],df[f"{spp}"]).fit()

  # Inspect the results
  print(results.summary())