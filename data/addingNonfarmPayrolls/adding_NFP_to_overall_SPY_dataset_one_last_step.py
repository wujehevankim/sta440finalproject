import pandas as pd



file_path = 'nfp_almost_done_added.csv'
data = pd.read_csv(file_path) #ensure the first column is the header

#1. create new columns called NFPDayOrNot and NFPOutcome
data['NFPDayOrNot'] = 0
data['NFPOutcome'] = None


#2. go through each row of data. if data['NFPResult'] == 'noNFP', make data[NFPDayOrNot] as 0. otherwise, make data[NFPDayOrNot] as 1.
for index, row in data.iterrows():
    if row['NFPResult'] != 'noNFP':
        data.at[index, 'NFPDayOrNot'] = 1


#3. now, go through each row of data again. if data['NFPResult'] == 'Shock', 'Nonprovoking', or "Upbeat", make data[NFPOutcome] as 'Shock', 'Nonprovoking', or "Upbeat", respectively
for index, row in data.iterrows():
    if row['NFPResult'] in ['Shock', 'Nonprovoking', 'Upbeat']:
        data.at[index, 'NFPOutcome'] = row['NFPResult']



data.drop(columns=['NFPResult'], inplace=True)

new_file_path = 'SPY_ready_for_analysis_triple_witch_NFP.csv'
data.to_csv(new_file_path, index=False)
