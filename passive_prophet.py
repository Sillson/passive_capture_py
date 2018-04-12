import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fbprophet import Prophet

# Example
# exec(open('/Users/stuartillson/passive_capture_py/passive_prophet.py').read())
# csv = '/Users/stuartillson/passive_capture_py/bon_passage_data.csv'
# spp = 'chinook_adult'

def run_forecast(csv, spp, num_of_days=30, return_count=False):
  df = create_dataframe(csv, spp)
  predict_passage(df,num_of_days)

def create_dataframe(csv, spp):
  print('Formatting the dataframe')
  df = pd.read_csv(csv)

  # select columns to remove to isolate a spp
  cols_to_remove = [col for col in df.columns if f"{spp}" not in col and 'count_date' not in col]
  df = df.drop(cols_to_remove, axis=1)
  
  # create date range to accommodate missing dates
  df['count_date'] = pd.to_datetime(df['count_date'])
  idx = pd.date_range(df['count_date'].iloc[0], df['count_date'].iloc[-1])
  df.set_index('count_date',drop=True,inplace=True)
  df = df.reindex(idx, fill_value=0).reset_index()

  # for prophet, format to use ds and y cols
  df['ds'] = df['index']

  # flag return values to be either counts, or the log of the counts
  if return_count:
    df['y'] = df[f"{spp}"]
  else:
    df['y'] = np.log(df[f"{spp}"])
    # replace all -inf 
    df['y'] = df['y'].replace([np.log(0)], 0)

  df = df.drop(['index', f"{spp}"], axis=1)

  return df

def predict_passage(df,num_of_days):
  print('Forecasting the future')
  m = Prophet()
  m.fit(df);
  future = m.make_future_dataframe(periods=num_of_days)
  forecast = m.predict(future)
  m.plot(forecast)
  plt.show()







