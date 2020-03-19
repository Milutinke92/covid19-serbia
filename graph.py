from datetime import datetime

import matplotlib.pylab as plt
import pandas as pd

df = pd.read_json("data.json")
df_new_cases = pd.read_json("data_new_cases.json")
df_cured_cases = pd.read_json("data_cure_cases.json")

df['time'] = df['time'].apply(lambda x: datetime.strptime(x, "%Y-%m-%d"))
df_new_cases['time'] = df_new_cases['time'].apply(lambda x: datetime.strptime(x, "%Y-%m-%d"))
df_cured_cases['time'] = df_cured_cases['time'].apply(lambda x: datetime.strptime(x, "%Y-%m-%d"))

width = 0.35  # the width of the bars: can also be len(x) sequence

fig, ax = plt.subplots()

ax.bar(df['time'].array, df['num_of_cases'].array, width, label='all cases')
ax.bar(df_new_cases['time'].array, df_new_cases['num_of_cases'].array, width, label='new cases')
ax.bar(df_cured_cases['time'].array, df_cured_cases['num_of_cases'].array, width, label='cured cases')

ax.xaxis_date()
ax.set_ylabel('Num Of Cases')
ax.set_title('COVID19 Serbia')
ax.legend()

plt.show()
