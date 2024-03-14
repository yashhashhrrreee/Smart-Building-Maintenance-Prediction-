import pandas as pd
import os

def combine_csv_files(folder_path, output_folder):
    # Extract folder name
    folder_name = os.path.basename(folder_path)

    # Get list of CSV files in the folder
    csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

    # Initialize an empty DataFrame
    combined_df = None

    # Iterate over each CSV file
    for file in csv_files:
        # Read CSV file into a DataFrame without header
        df = pd.read_csv(os.path.join(folder_path, file), header=None)

        # Rename the first column to 'id'
        df.rename(columns={0: 'id'}, inplace=True)

        # Extract the name of the CSV file without extension
        file_name = os.path.splitext(file)[0]

        # Rename the remaining columns with the file name
        for i in range(len(df.columns)):
            df.rename(columns={i: f'{file_name}'}, inplace=True)

        # Merge the DataFrame with the combined DataFrame
        if combined_df is None:
            combined_df = df
        else:
            combined_df = pd.merge(combined_df, df, on='id', how='outer')

    # Handle missing values after merging
    combined_df.fillna(method='ffill', inplace=True)

    # Save the combined DataFrame as a CSV file
    output_file_path = os.path.join(output_folder, f'{folder_name}.csv')
    combined_df.to_csv(output_file_path, index=False)

    return output_file_path

# Provide the folder path where the CSV files are located
folder_path = r'D:\Study\Smart-Building-Maintenance-Prediction-\Dataset\776'
# Provide the output folder path where you want to save the combined CSV file
output_folder = r'D:\Study\Smart-Building-Maintenance-Prediction-\New Dataset'

# Call the function to combine CSV files
output_file_path = combine_csv_files(folder_path, output_folder)

# Print the path of the saved CSV file
print(f"Combined CSV file saved at: {output_file_path}")