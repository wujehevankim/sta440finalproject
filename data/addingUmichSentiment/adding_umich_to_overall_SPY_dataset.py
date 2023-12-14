import pandas as pd



file_path = 'SPY_ready_for_analysis_triple_witch_NFP.csv'
data = pd.read_csv(file_path) #ensure the first column is the header

umich_data = pd.read_csv('umich_dates_refined_differences_added.csv')

#1. create new column called "umichResult" to data
data['CSIOutcome'] = 'noCSI' 
data['CSIActualMinusExpected'] = None


#2. go through every row in data, and for every row, if data['PrecedingWeekFridayDate'] in umich_data['ReleaseDate'] column list, data['umichResult'] == umich_data['UMichCSIOutcome'] of the appropriate row of umich_data where umich_data['ReleaseDate'] = data['PrecedingWeekFridayDate']. ALL ELSE, data['umichResult'] would be "noCSI"
for index, row in data.iterrows():
    # Check if 'PrecedingWeekFridayDate' exists in 'ReleaseDate' of nfp_data
    if row['PrecedingWeekFridayDate'] in umich_data['ReleaseDate'].values:
        # Fetching the corresponding 'ExpectionDefyingNFP' value
        umich_result = umich_data[umich_data['ReleaseDate'] == row['PrecedingWeekFridayDate']]['UMichCSIOutcome'].iloc[0]
        data.at[index, 'CSIOutcome'] = umich_result
        data.at[index, 'CSIActualMinusExpected'] = umich_data[umich_data['ReleaseDate'] == row['PrecedingWeekFridayDate']]['ActualMinusForecast'].iloc[0]
        
#data['NFPResult'].fillna('noNFP', inplace=True)

data['CSIDayOrNot'] = 0

for index, row in data.iterrows():
    if data.at[index, 'CSIOutcome'] != 'noCSI':
        data.at[index, 'CSIDayOrNot'] = 1


for index, row in data.iterrows():
    if data.at[index, 'CSIOutcome'] == 'noCSI':
        data.at[index, 'CSIOutcome'] = None



new_file_path = 'SPY_ready_for_analysis_triple_witch_NFP_CSI.csv'
data.to_csv(new_file_path, index=False)
