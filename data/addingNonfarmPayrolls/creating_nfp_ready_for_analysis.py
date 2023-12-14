import pandas as pd



file_path = 'nfp_refined.csv'
data = pd.read_csv(file_path) #ensure the first column is the header



#1. create new columns called ExpectionDefyingNFP
data['ExpectionDefyingNFP'] = None


#2. go through all rows, and calculate a value called actualVSForecastedInPercent = ( data['Actual']-data['Forecast']) / abs(data['Forecast']) ) * 100 only if data['Forecast'] != none. otherwise, leave it as "None"
data['actualVSForecastedInPercent'] = None
for index, row in data.iterrows():
    if pd.notnull(row['Forecast']) and row['Forecast'] != 0:
        data.at[index, 'actualVSForecastedInPercent'] = (row['Actual'] - row['Forecast']) / abs(row['Forecast']) * 100


#3. now go through each row, and if data['actualVSForecastedInPercent'] < -50, make data['ExpectionDefyingNFP'] as "Shock". if data['actualVSForecastedInPercent'] < +50, make data['ExpectionDefyingNFP'] as "Upbeat". all else, make data['ExpectionDefyingNFP'] as "Nonprovoking"
for index, row in data.iterrows():
    if pd.notnull(row['actualVSForecastedInPercent']):
        if row['actualVSForecastedInPercent'] < -50:
            data.at[index, 'ExpectionDefyingNFP'] = 'Shock'
        elif row['actualVSForecastedInPercent'] > 50:
            data.at[index, 'ExpectionDefyingNFP'] = 'Upbeat'
        else:
            data.at[index, 'ExpectionDefyingNFP'] = 'Nonprovoking'




new_file_path = 'nfp_refined_more.csv'
data.to_csv(new_file_path, index=False)
