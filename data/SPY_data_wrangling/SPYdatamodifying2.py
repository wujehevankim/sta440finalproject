import pandas as pd


file_path = 'SPY_modified1.csv'  
data = pd.read_csv(file_path)


grouped = data.groupby('WeekOf')
filtered_data = grouped.head(1).append(grouped.tail(1))


filtered_data.reset_index(drop=True, inplace=True)


filtered_data['Date'] = pd.to_datetime(filtered_data['Date'])


filtered_data.sort_values(by='Date', inplace=True)


filtered_data.to_csv('SPY_modified2.csv', index=False)

