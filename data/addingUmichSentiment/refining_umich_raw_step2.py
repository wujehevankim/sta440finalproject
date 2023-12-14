import pandas as pd



file_path = 'umich_dates_refined.csv'
data = pd.read_csv(file_path) #ensure the first column is the header




#1. go through all rows, and create new columns called 'ActualMinusForecast' and 'UMichCSIOutcome'

#2. go through all rows, andmake data['ActualMinusForecast'] = data['Actual'] - data['Forecast']


#3. go through all rows, and make, if data['ActualMinusForecast'] is higher than 10, lower than -10, and else as 'Upbeat', 'Shock', and 'Baseline' respectively

data['ActualMinusForecast'] = data['Actual'] - data['Forecast']


data['UMichCSIOutcome'] = data['ActualMinusForecast'].apply(
    lambda x: 'Upbeat' if x > 5 else ('Shock' if x < -5 else 'Baseline')
)


new_file_path = 'umich_dates_refined_differences_added.csv'
data.to_csv(new_file_path, index=False)
