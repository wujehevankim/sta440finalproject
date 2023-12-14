import pandas as pd



file_path = 'SPY_ready_for_analysis_triple_witch.csv'
data = pd.read_csv(file_path) #ensure the first column is the header

nfp_data = pd.read_csv('nfp_refined_more.csv')

#1. create new column called "NFPResult" to data
data['NFPResult'] = 'noNFP' 


#2. go through every row in data, and for every row, if data['PrecedingWeekFridayDate'] in nfp_data['ReleaseDate'] column list, data['NFPResult'] == nfp_data['ExpectionDefyingNFP'] of the appropriate row of nfp_data where nfp_data['ReleaseDate'] = data['PrecedingWeekFridayDate']. ALL ELSE, data['NFPResult'] would be "noNFP"
for index, row in data.iterrows():
    # Check if 'PrecedingWeekFridayDate' exists in 'ReleaseDate' of nfp_data
    if row['PrecedingWeekFridayDate'] in nfp_data['ReleaseDate'].values:
        # Fetching the corresponding 'ExpectionDefyingNFP' value
        nfp_result = nfp_data[nfp_data['ReleaseDate'] == row['PrecedingWeekFridayDate']]['ExpectionDefyingNFP'].iloc[0]
        data.at[index, 'NFPResult'] = nfp_result
        
data['NFPResult'].fillna('noNFP', inplace=True)


new_file_path = 'nfp_almost_done_added.csv'
data.to_csv(new_file_path, index=False)
