import pandas as pd



file_path = 'umich_raw.csv'
data = pd.read_csv(file_path) #ensure the first column is the header




#1. go through all rows, and convert 'ReleaseDate' into pd.datetimes?
def parse_date(date_str):
    if isinstance(date_str, str):
        try:
            # First, try parsing in 'Dec 08, 2023 (Nov)' format
            date_part = date_str.split(' (')[0]
            return pd.to_datetime(date_part, format='%b %d, %Y')
        except ValueError:
            # If the above fails, try parsing in '2-Oct-09' format
            return pd.to_datetime(date_str, format='%d-%b-%y')
    return date_str

# Convert 'ReleaseDate' to datetime
data['ReleaseDate'] = data['ReleaseDate'].apply(parse_date)

#2. now, go through all rows, and if data['ReleaseDate'] is not a Friday, drop that row
data = data[data['ReleaseDate'].dt.dayofweek == 4]


new_file_path = 'umich_dates_refined.csv'
data.to_csv(new_file_path, index=False)
