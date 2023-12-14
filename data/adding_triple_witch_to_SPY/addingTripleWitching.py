import pandas as pd
import datetime as dt


file_path = 'SPY_ready_for_analysis.csv'
data = pd.read_csv(file_path)




# 1. from 1/6/2003 to 12/4/2023, get a list of dates that are third Friday of every March, June, September, and December and save it to a list called "tripleWitchDaysList"

def get_third_fridays(year):
    third_fridays = []
    for month in [3, 6, 9, 12]:  # March, June, September, December
        # Start from the first day of the month
        date = dt.date(year, month, 1)
        # Find the first Friday
        while date.weekday() != 4:  # Friday
            date += dt.timedelta(days=1)
        # Add 14 days (two weeks) to get the third Friday
        third_fridays.append(date + dt.timedelta(days=14))
    return third_fridays

# Generate list of third Fridays from 1/6/2003 to 12/4/2023
start_year = 2003
end_year = 2023
tripleWitchDaysList = []
for year in range(start_year, end_year + 1):
    tripleWitchDaysList.extend(get_third_fridays(year))





# 2. to data, add a new column called 'fridayWasATripleWitchDay' and initialize all of them as 0
data['fridayWasATripleWitchDay'] = 0




#3. now, for each row in data,  check if pd.to_datetime(data['PrecedingWeekFridayDate']) is in triplewitchDaysList. if yes, make that row's 'fridayWasATripleWitchDay' 1
for index, row in data.iterrows():
    if pd.to_datetime(row['PrecedingWeekFridayDate']).date() in tripleWitchDaysList:
        data.at[index, 'fridayWasATripleWitchDay'] = 1


        


new_file_path = 'SPY_ready_for_analysis_triple_witch.csv'
data.to_csv(new_file_path, index=False)
