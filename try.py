# import pandas as pd
# import os

# # Path to the folder containing CSV files
# folder_path = "D:\Study\Sem VI\Smart-Building-Maintenance-Prediction-\Individual_Dataset"

# # Initialize an empty dictionary to store dataframes
# dfs = {}

# # Iterate over each file in the folder
# for file_name in os.listdir(folder_path):
#     if file_name.endswith(".csv"):
#         # Read the CSV file into a dataframe
#         df = pd.read_csv(os.path.join(folder_path, file_name))
        
#         # Exclude the first column if it exists
#         if df.columns[0] == 'Unnamed: 0':
#             df = df.drop(columns=[df.columns[0]])
        
#         # Calculate mean of each column (room) and round to 2 decimal places
#         mean_values = df.mean().round(2).to_dict()
        
#         # Extract CSV name without extension
#         csv_name = os.path.splitext(file_name)[0]
        
#         # Add mean values to the dictionary with CSV name as key
#         dfs[csv_name] = mean_values

# # Create a dataframe from the dictionary
# result_df = pd.DataFrame.from_dict(dfs, orient='index')

# # Save the dataframe to a CSV file
# result_df.to_csv("mean_values.csv")

# print("CSV file saved successfully.")


# import csv

# # Data from 412 to 564
# data = [
#     (413, 0.22, 0.18, 0.16, 0.07, 0.18, 0.08, 0.38, 0.31, 0.30, 0.14, 0.32, 0.20, 0.61, 0.69, 0.72, 0.87, 0.68, 0.86),
#     (415, 0.16, 0.09, 0.09, 0.04, 0.07, 0.03, 0.30, 0.21, 0.21, 0.11, 0.20, 0.04, 0.33, 0.61, 0.63, 0.84, -0.05, 0.85),
#     (417, 0.16, 0.09, 0.09, 0.04, 0.07, 0.03, 0.30, 0.21, 0.21, 0.11, 0.20, 0.04, 0.33, 0.61, 0.63, 0.84, -0.05, 0.85),
#     (419, 20273.99, 20236.73, 20199.63, 21868.32, 20269.47, 20003.83, 72.58, 72.38, 72.35, 65.85, 70.87, 71.88, 0.00, 0.00, 0.01, -0.08, 0.00, 0.02),
#     (421, 0.22, 0.18, 0.16, 0.07, 0.18, 0.08, 0.38, 0.31, 0.30, 0.14, 0.32, 0.20, 0.61, 0.69, 0.72, 0.87, 0.68, 0.86),
#     (422, 0.20, 0.12, 0.12, 0.05, 0.21, 0.05, 0.35, 0.24, 0.24, 0.12, 0.38, 0.15, 0.29, 0.59, 0.59, 0.82, 0.28, 0.82),
#     (423, 0.07, 0.03, 0.03, 0.02, 0.05, 0.02, 0.20, 0.11, 0.11, 0.05, 0.17, 0.08, 0.81, 0.93, 0.93, 0.95, 0.86, 0.95),
#     (424, 0.07, 0.02, 0.02, 0.02, 0.06, 0.01, 0.20, 0.10, 0.10, 0.04, 0.19, 0.01, 0.69, 0.91, 0.91, 0.93, 0.74, 0.94),
#     (442, 0.04, 0.03, 0.03, 0.02, 0.06, 0.02, 0.17, 0.12, 0.12, 0.08, 0.19, 0.05, 0.60, 0.73, 0.73, 0.84, 0.49, 0.84),
#     (446, 11.07, 22.13, 15.89, 13.06, 11.09, 17.32, 0.13, 0.13, 0.12, 0.09, 0.18, 0.11, 0.00, -0.99, -0.43, -0.18, 0.00, -0.56),
#     (448, 0.02, 0.01, 0.01, 0.01, 0.06, 0.01, 0.10, 0.06, 0.06, 0.04, 0.21, 0.01, 0.50, 0.75, 0.75, 0.80, -0.79, 0.82),
#     (452, 0.02, 0.01, 0.03, 0.01, 0.03, 0.01, 0.10, 0.07, 0.03, 0.05, 0.12, 0.01, 0.45, 0.69, 0.69, 0.78, 0.22, 0.79),
#     (454, 0.02, 0.01, 0.01, 0.01, 0.03, 0.01, 0.11, 0.09, 0.09, 0.05, 0.12, 0.06, 0.53, 0.69, 0.69, 0.79, 0.41, 0.81),
#     (456, 0.03, 0.02, 0.02, 0.01, 0.03, 0.01, 0.14, 0.10, 0.10, 0.06, 0.14, 0.07, 0.69, 0.82, 0.82, 0.88, 0.69, 0.88),
#     (458, 0.27, 0.12, 0.12, 0.09, 0.18, 0.09, 0.40, 0.19, 0.18, 0.13, 0.27, 0.15, 0.79, 0.90, 0.91, 0.93, 0.86, 0.93),
#     (462, 0.09, 0.06, 0.05, 0.04, 0.09, 0.04, 0.22, 0.17, 0.16, 0.12, 0.24, 0.13, 0.11, 0.44, 0.45, 0.56, 0.07, 0.58),
#     (510, 0.37, 0.23, 0.22, 0.11, 0.18, 0.12, 0.47, 0.35, 0.35, 0.17, 0.29, 0.22, 0.78, 0.87, 0.87, 0.94, 0.90, 0.93),
#     (511, 0.24, 0.12, 0.12, 0.07, 0.72, 0.04, 0.37, 0.22, 0.21, 0.11, 0.65, 0.09, 0.48, 0.74, 0.75, 0.84, -0.55, 0.91),
#     (513, 5.75, 5.68, 5.67, 5.87, 5.73, 5.62, 0.34, 0.25, 0.25, 0.15, 0.33, 0.18, 0.01, 0.02, 0.02, -0.01, 0.01, 0.03),
#     (552, 0.08, 0.06, 0.06, 0.03, 0.09, 0.03, 0.24, 0.17, 0.17, 0.10, 0.24, 0.11, 0.68, 0.79, 0.79, 0.87, 0.65, 0.88),
#     (554, 0.10, 0.05, 0.05, 0.02, 0.07, 0.02, 0.26, 0.18, 0.18, 0.07, 0.20, 0.10, 0.58, 0.76, 0.76, 0.90, 0.70, 0.90),
#     (556, 0.09, 0.07, 0.07, 0.04, 0.10, 0.04, 0.25, 0.18, 0.18, 0.11, 0.25, 0.12, 0.67, 0.77, 0.77, 0.85, 0.64, 0.85),
#     (558, 0.22, 0.18, 0.16, 0.07, 0.18, 0.08, 0.38, 0.31, 0.30, 0.14, 0.32, 0.20, 0.61, 0.69, 0.72, 0.87, 0.68, 0.86),
#     (562, 0.09, 0.42, 0.54, 0.28, 0.10, 2.46, 0.24, 0.19, 0.19, 0.13, 0.26, 0.17, 0.73, -0.30, -0.67, 0.14, 0.70, -6.62),
#     (564, 0.13, 0.09, 0.09, 0.06, 0.10, 0.06, 0.29, 0.22, 0.22, 0.14, 0.25, 0.16, 0.69, 0.78, 0.79, 0.86, 0.76, 0.86)
# ]

# # Write data to CSV
# with open('model_comparison.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['RoomID', 'Linear Regression MSE', 'Decision Tree MSE', 'Random Forest MSE', 
#                      'K-NN MSE', 'MLP MSE', 'Gradient Boosting MSE', 'Linear Regression MAE', 
#                      'Decision Tree MAE', 'Random Forest MAE', 'K-NN MAE', 'MLP MAE', 
#                      'Gradient Boosting MAE', 'Linear Regression R-squared', 'Decision Tree R-squared', 
#                      'Random Forest R-squared', 'K-NN R-squared', 'MLP R-squared', 'Gradient Boosting R-squared'])
#     for row in data:
#         writer.writerow(row)

import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('model_comparison.csv')

# Select only the 'CSV File' and 'R-squared' columns
selected_columns = df[['RoomID', 'Linear Regression R-squared', 'Decision Tree R-squared', 
                       'Random Forest R-squared', 'K-NN R-squared', 'MLP R-squared', 
                       'Gradient Boosting R-squared']]

# Print the selected columns
print(selected_columns)

# Save the selected columns to a new CSV file
selected_columns.to_csv('R-squared_Values.csv', index=False)
