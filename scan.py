import os
from datetime import datetime, timedelta

def scan_folder_for_old_files(folder_path, months_old=3):
    # Calculate the cutoff date (current date minus 3 months)
    cutoff_date = datetime.now() - timedelta(days=months_old * 30)

    for file_name in os.listdir(folder_path):
        if file_name == ".gitignore" or file_name == ".gitkeep":
            continue

        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            # Get the creation time of the file
            creation_time = os.path.getctime(file_path)
            # Convert creation time to a datetime object
            creation_time_dt = datetime.fromtimestamp(creation_time)

            # Check if the file is older than the cutoff date
            if creation_time_dt < cutoff_date:
                # creation_time_str = creation_time_dt.strftime('%Y-%m-%d %H:%M:%S')
                # print(file_name + ": Created at " + creation_time_str + ", older than " + str(months_old) + " months.")
                os.remove(file_path)

# Example usage
folders = [
    '/home/upload_myessen/temp',
    '/home/upload_myessen/selfie',
    '/home/upload_myessen/visit',
    # '/home/upload_myessen/bd/resi',
    # '/home/upload_myessen/ebr',
    # '/home/upload_myessen/wh/packing',
    # '/home/upload_myessen/wh_daerah/packing',
    # '/home/upload_myessen/packing_so',
    # '/home/upload_myessen/packing_sm',
]

for folder in folders:
    scan_folder_for_old_files(folder)