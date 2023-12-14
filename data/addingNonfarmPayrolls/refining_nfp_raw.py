import pandas as pd



file_path = 'nfp_raw.csv'
data = pd.read_csv(file_path) #ensure the first column is the header




#1. go through all rows, and for each value in Actual, Forecast, and Previous columns, get rid of commas and convert instances of K's into times 1000
def convert_k_and_remove_commas(value):
    if isinstance(value, str):
        if 'K' in value:
            return float(value.replace('K', '').replace(',', '')) * 1000
        else:
            return float(value.replace(',', ''))
    return value

# Apply the function to the specified columns
for column in ['Actual', 'Forecast', 'Previous']:
    data[column] = data[column].apply(convert_k_and_remove_commas)

        
#2. go through all rows, and convert 'ReleaseDate' into pd.datetimes?
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


new_file_path = 'nfp_refined.csv'
data.to_csv(new_file_path, index=False)
