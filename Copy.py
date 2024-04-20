import os
import shutil

def copy_ipynb_to_csv_folder(ipynb_file, csv_folder, output_folder):
    # Check if provided paths exist
    if not os.path.isfile(ipynb_file):
        print(f"Error: IPYNB file '{ipynb_file}' does not exist.")
        return
    if not os.path.isdir(csv_folder):
        print(f"Error: CSV folder '{csv_folder}' does not exist.")
        return
    
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # List CSV files in the folder
    csv_files = [f for f in os.listdir(csv_folder) if f.endswith('.csv')]
    
    # Copy IPYNB file to the output folder
    shutil.copy(ipynb_file, output_folder)
    print(f"Copied {ipynb_file} to {output_folder}")
    
    # Move CSV files to the output folder
    for csv_file in csv_files:
        shutil.move(os.path.join(csv_folder, csv_file), os.path.join(output_folder, csv_file))
        print(f"Moved {csv_file} to {output_folder}")

# Example usage
ipynb_file_path = r'D:\Study\Sem VI\Smart-Building-Maintenance-Prediction-\Individual_Room\413.ipynb'
csv_folder_path = 'D:\Study\Sem VI\Smart-Building-Maintenance-Prediction-\Modified_Dataset'
output_folder_path = 'D:\\Study\\Sem VI\\Smart-Building-Maintenance-Prediction-\\New_Individual_Room'

copy_ipynb_to_csv_folder(ipynb_file_path, csv_folder_path, output_folder_path)
