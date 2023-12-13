import pandas as pd

# Load the data
file_path = 'SPY_modified1.csv'  
data = pd.read_csv(file_path)

# Group the data by 'WeekOf'
grouped = data.groupby('WeekOf')

# Define a custom function to include the first, second to last, and last entry for groups of size 3 or more
def include_specific_entries(group):
    if len(group) >= 3:
        return group.iloc[[0, -2, -1]]  # Include the first, second to last, and last entries
    return pd.DataFrame()  # Return an empty DataFrame for groups smaller than 3

# Apply the custom function to each group
filtered_data = grouped.apply(include_specific_entries).reset_index(drop=True)

# Convert 'Date' to datetime and sort the data
filtered_data['Date'] = pd.to_datetime(filtered_data['Date'])
filtered_data.sort_values(by='Date', inplace=True)

# Save the filtered data to a new CSV file
filtered_data.to_csv('SPY_modified2.csv', index=False)


print(".csv file created")