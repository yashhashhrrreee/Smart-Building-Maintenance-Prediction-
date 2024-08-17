import pandas as pd
import os

# Directory containing all CSV files
directory = r'D:\Study\Sem VI\Smart-Building-Maintenance-Prediction-\Modified_Dataset'

# List to store dataframes for each CSV
dfs = []

# Iterate over each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        try:
            # Read CSV file into a DataFrame
            df = pd.read_csv(os.path.join(directory, filename))
            # Add a new column for room id
            df['roomid'] = os.path.splitext(filename)[0]  # Extract room id from filename
            # Assume the first column is the timestamp
            df.rename(columns={df.columns[0]: 'timestamp'}, inplace=True)
            # Append DataFrame to list
            dfs.append(df)
        except Exception as e:
            print(f"Error reading file {filename}: {e}")

# Concatenate all DataFrames into a single DataFrame
if dfs:
    combined_df = pd.concat(dfs, ignore_index=True)
    
    # Reorder columns
    combined_df = combined_df[['timestamp', 'co2', 'humidity', 'light', 'pir', 'temperature', 'roomid']]
    
    # Save the combined DataFrame to a new CSV file
    combined_df.to_csv('Combined_Smart_Buldings.csv', index=False)
else:
    print("No CSV files found in the directory.")

