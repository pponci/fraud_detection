import os

from kaggle.api.kaggle_api_extended import KaggleApi

def download_dataset():
    """
    This function dowloads the dataset from kaggle and renames
    the file.
    """

    # config
    dataset = "ealaxi/paysim1"
    raw_dir = "./data/raw"
    target_file = "PS_20174392719_1491204439457_log.csv"
    new_filename = "raw_data.csv"

    # ensure directory exists
    os.makedirs(raw_dir, exist_ok = True)

    # authenticate kaggle api and download dataset
    api = KaggleApi()
    api.authenticate()

    api.dataset_download_files(dataset, path = raw_dir, unzip = True)

    # rename dataset
    old_path = os.path.join(raw_dir, target_file)
    new_path = os.path.join(raw_dir, new_filename)

    if os.path.exists(old_path):
        os.rename(old_path, new_path)

    else:
        print(f"File {target_file} not found")

if __name__ == "__main__":
    download_dataset()