import pandas as pd


file_path = 'SPY_modified2.csv'
data = pd.read_csv(file_path)


data['Date'] = pd.to_datetime(data['Date'])


new_df = pd.DataFrame(columns=[
    'PrecedingWeekToFollowingWeek', 'PrecedingWeekFridayDate', 'PrecedingWeekFridayOpen', 'PrecedingWeekFridayHigh', 
    'PrecedingWeekFridayLow', 'PrecedingWeekFridayClose', 'PrecedingWeekFridayVolume',
    'PrecedingWeekFridayDayOfTheWeek', 'FollowingWeekMondayDate', 'FollowingWeekMondayOpen', 'FollowingWeekMondayHigh', 
    'FollowingWeekMondayLow', 'FollowingWeekMondayClose', 'FollowingWeekMondayVolume', 
    'FollowingWeekMondayDayOfTheWeek', 'WasMondayOpenHigherThanFridayClose', 'MondayOpenComparedToFridayCloseChangeInPercent','WasMondayCloseHigherThanFridayClose', 'MondayCloseComparedToFridayCloseChangeInPercent'
])

rows = [] 

for i in range(1, len(data), 2):  # Step by 2 as we're looking at pairs of rows
    # Assigning values from the 'Friday' row
    friday_row = data.iloc[i]
    # Assigning values from the 'Monday' row of the following week
    monday_row = data.iloc[i + 1]


    was_monday_open_higher = int(monday_row['Open'] > friday_row['Close'])
    open_change_percent = ((monday_row['Open'] - friday_row['Close']) / friday_row['Close']) * 100
    was_monday_close_higher = int(monday_row['Close'] > friday_row['Close'])
    close_change_percent = ((monday_row['Close'] - friday_row['Close']) / friday_row['Close']) * 100

    
    # Construct the new row for our new DataFrame
    new_row = {
        'PrecedingWeekToFollowingWeek': f"{friday_row['WeekOf']} to {monday_row['WeekOf']}",
        'PrecedingWeekFridayDate': friday_row['Date'].date(),
        'PrecedingWeekFridayOpen': friday_row['Open'],
        'PrecedingWeekFridayHigh': friday_row['High'],
        'PrecedingWeekFridayLow': friday_row['Low'],
        'PrecedingWeekFridayClose': friday_row['Close'],
        'PrecedingWeekFridayVolume': friday_row['Volume'],
        'PrecedingWeekFridayDayOfTheWeek': friday_row['DayOfTheWeek'],
        'FollowingWeekMondayDate': monday_row['Date'].date(),
        'FollowingWeekMondayOpen': monday_row['Open'],
        'FollowingWeekMondayHigh': monday_row['High'],
        'FollowingWeekMondayLow': monday_row['Low'],
        'FollowingWeekMondayClose': monday_row['Close'],
        'FollowingWeekMondayVolume': monday_row['Volume'],
        'FollowingWeekMondayDayOfTheWeek': monday_row['DayOfTheWeek'],
        'WasMondayOpenHigherThanFridayClose': was_monday_open_higher,
        'MondayOpenComparedToFridayCloseChangeInPercent': open_change_percent,
        'WasMondayCloseHigherThanFridayClose': was_monday_close_higher,
        'MondayCloseComparedToFridayCloseChangeInPercent': close_change_percent,
    }

    rows.append(new_row)


new_df = pd.concat([new_df, pd.DataFrame(rows)], ignore_index=True)


new_df.to_csv('SPY_ready_for_analysis.csv', index=False)
print("new .csv file saved")