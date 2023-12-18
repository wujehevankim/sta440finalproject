import pandas as pd



file_path = 'SPY_ready_for_analysis_triple_witch_NFP_CSI_FOMC_with_month_withUnemployment_finished_electionMonthsAdded.csv'
data = pd.read_csv(file_path) #ensure the first column is the header

unemploymentWeeksToAdd = pd.read_csv('unemployment_raw.csv')

data['UnemploymentActualMinusPreviousInPercent'] = 0.0


data['PrecedingWeekFridayDate'] = pd.to_datetime(data['PrecedingWeekFridayDate'])
unemploymentWeeksToAdd['Release Date'] = pd.to_datetime(unemploymentWeeksToAdd['Release Date'])


for index, row in unemploymentWeeksToAdd.iterrows():
    release_date = row['Release Date']
    if release_date in data['PrecedingWeekFridayDate'].values:
        data.loc[data['PrecedingWeekFridayDate'] == release_date, 'UnemploymentActualMinusPreviousInPercent'] = row['ActualMinusPreviousInPercent']





new_file_path = 'SPY_ready_for_analysis_triple_witch_NFP_CSI_FOMC_with_month_withUnemployment_finished_electionMonthsAdded_FINAL.csv'
data.to_csv(new_file_path, index=False)
