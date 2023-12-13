import pandas as pd
import datetime as dt


file_path = 'SPY.csv'
data = pd.read_csv(file_path)


data['Date'] = pd.to_datetime(data['Date'])


def get_week_of(date):

    day_difference = date.weekday()

    week_of = date - dt.timedelta(days=day_difference)
    return week_of

data['DayOfTheWeek'] = data['Date'].dt.day_name()
data['WeekOf'] = data['Date'].apply(get_week_of)


new_file_path = 'SPY_modified.csv'
data.to_csv(new_file_path, index=False)
