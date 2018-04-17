import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fbprophet import Prophet

# Example
# exec(open('/Users/stuartillson/passive_capture_py/passive_prophet.py').read())
# csv = '/Users/stuartillson/passive_capture_py/bon_passage_data.csv'
# spp = 'chinook_adult'

def run_all_forecasts(spp, num_of_days=30):
  for csv in passage_csvs():
    run_forecast_and_save(csv, spp, num_of_days)

def run_forecast_and_save(csv, spp, num_of_days=30, display_count=False):
  df = create_dataframe(csv, spp, display_count)
  predict_passage_and_save(df['dataframe'],df['dam'],num_of_days)

def passage_csvs():
  files = [os.path.abspath(f"csv/passage_data/{x}") for x in os.listdir('csv/passage_data')]
  return files

def run_forecast(csv, spp, num_of_days=30, display_count=False):
  df = create_dataframe(csv, spp, display_count)
  predict_passage(df['dataframe'],num_of_days)

def create_dataframe(csv, spp, display_count=False):
  print('Formatting the dataframe')
  df = pd.read_csv(csv)

  # isolate the dam
  dam_name = df['dam'][0]

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
  if display_count:
    df['y'] = df[f"{spp}"]
  else:
    df['y'] = np.log(df[f"{spp}"])
    # replace all -inf 
    df['y'] = df['y'].replace([np.log(0)], 0)

  df = df.drop(['index', f"{spp}"], axis=1)

  return {'dataframe': df, 'dam': dam_name}

def predict_passage_and_save(df,dam,num_of_days):
  print('Forecasting the future')
  m = Prophet()
  m.fit(df);
  future = m.make_future_dataframe(periods=num_of_days)
  forecast = m.predict(future)
  grf = m.plot(forecast)
  grf.savefig(f"charts/{dam}_forecast.png")
  forecast.to_csv(f"csv/forecasts/{dam}_forecast.csv")

def predict_passage(df,num_of_days):
  print('Forecasting the future')
  m = Prophet()
  m.fit(df);
  future = m.make_future_dataframe(periods=num_of_days)
  forecast = m.predict(future)
  m.plot(forecast)
  plt.show()







