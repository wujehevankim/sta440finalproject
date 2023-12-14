import pandas as pd



file_path = 'SPY_ready_for_analysis_triple_witch_NFP_CSI.csv'
data = pd.read_csv(file_path) #ensure the first column is the header

fomc_data = pd.read_csv('fomc_raw.csv')



data['PrecedingWeekFridayDate'] = pd.to_datetime(data['PrecedingWeekFridayDate'])
fomc_data['ReleaseDate'] = pd.to_datetime(fomc_data['ReleaseDate'])



def is_fomc_week(date, fomc_dates):
    # Check if the date, one day before, or two days before, is in FOMC dates
    return any(date + pd.Timedelta(days=offset) in fomc_dates for offset in [0, -1, -2])

fomc_dates_set = set(fomc_data['ReleaseDate'])



data['wasItFOMCWeek'] = data['PrecedingWeekFridayDate'].apply(lambda date: int(is_fomc_week(date, fomc_dates_set)))



#2. create a new column in data called 'FOMCMeetingDate' go through each row, and if data['wasItFOMCWeek'] == 1, make data['FOMCMeetingDate']the appropriate fomc_data['ReleaseDate'] that is one, two, or three days prior to data['PrecedingWeekFridayDate']
def find_fomc_meeting_date(date, fomc_dates):
    if any(date + pd.Timedelta(days=offset) in fomc_dates for offset in [0, -1, -2]):
        # Find the FOMC date that is one, two, or three days prior
        for offset in [0, -1, -2]:
            potential_date = date + pd.Timedelta(days=offset)
            if potential_date in fomc_dates:
                return potential_date
    return pd.NaT  # Return NaT (Not a Time) if no matching date is found

# Apply the function to create the 'FOMCMeetingDate' column
data['FOMCMeetingDate'] = data['PrecedingWeekFridayDate'].apply(lambda date: find_fomc_meeting_date(date, fomc_dates_set))



#3. create two columms called 'FOMCAction' and 'FOMCActualVSExpected'. go through each row of data, and if data['FOMCMeetingDate'] is not none, find the row that matches fomc_data['ReleaseDate']. then, make data['FOMCAction'] as fomc_data['FOMCAction'] and make data['FOMCActualVSExpected'] as fomc_data['FOMCActualVSExpected']
def get_fomc_data(date, fomc_df):
    if pd.notna(date):
        fomc_row = fomc_df[fomc_df['ReleaseDate'] == date]
        if not fomc_row.empty:
            return fomc_row.iloc[0]['FOMCAction'], fomc_row.iloc[0]['FOMCActualVSExpected']
    return None, None  # Return None if no matching date or date is NaT

# Apply the function to each row in 'data' to get 'FOMCAction' and 'FOMCActualVSExpected'
data[['FOMCAction', 'FOMCActualVSExpected']] = data.apply(lambda row: get_fomc_data(row['FOMCMeetingDate'], fomc_data), axis=1, result_type="expand")




new_file_path = 'SPY_ready_for_analysis_triple_witch_NFP_CSI_FOMC.csv'
data.to_csv(new_file_path, index=False)
