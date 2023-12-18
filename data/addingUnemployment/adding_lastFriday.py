import pandas as pd
import calendar



file_path = 'SPY_ready_for_analysis_triple_witch_NFP_CSI_FOMC_with_month_withUnemployment_finished_electionMonthsAdded_FINAL.csv'
data = pd.read_csv(file_path) #ensure the first column is the header






data['PrecedingWeekFridayDate'] = pd.to_datetime(data['PrecedingWeekFridayDate'])

data['isItLastFridayOfTheMonth'] = 0


for index, row in data.iterrows():
    # Get the release_date from the row
    release_date = row['PrecedingWeekFridayDate']

    # Calculate the last day of the month
    last_day_of_month = pd.Timestamp(release_date.year, release_date.month, calendar.monthrange(release_date.year, release_date.month)[1])

    # Check if the release_date is the last Friday of the month
    if release_date == last_day_of_month - pd.Timedelta(days=(last_day_of_month.weekday() - 4 + 7) % 7):
        data.at[index, 'isItLastFridayOfTheMonth'] = 1





new_file_path = 'SPY_ready_for_analysis_triple_witch_NFP_CSI_FOMC_with_month_withUnemployment_finished_electionMonthsAdded_FINAL_lastFridayAdded.csv'
data.to_csv(new_file_path, index=False)
