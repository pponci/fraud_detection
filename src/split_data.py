import pandas as pd

def data_split(train_size : float = 0.7, val_size : float = 0.2, test_size : float = 0.1):
    """
    This function loads the raw data and then performs the split in train,
    validation, and test dataset. After it saves the datasets.
    """
    seed = 11

    # load raw data
    df = pd.read_csv("./data/raw/raw_data.csv")

    len_all = len(df)
    print("total data lenght :", len_all)

    # split data
    len_train = len(df) * train_size
    len_val = len(df) * val_size
    len_test = len(df) * test_size

    df_train = df.loc[0 : len_train - 1]
    df_val = df.loc[len_train : len_train + len_val - 1]
    df_test = df.loc[len_train + len_val: ]

    print("lenght train data :", len(df_train), "lenght validation data :", len(df_val), "lenght test data :", len(df_test))
    print(f"percentage train data : {round((len(df_train)/ len_all) * 100)}%, percentage validation data : {round((len(df_val)/ len_all) * 100)}%, percentage test data : {round((len(df_test)/len_all) * 100)}%")

    # save split data
    df_train.to_csv("./data/split/train_data.csv")
    df_val.to_csv("./data/split/validation_data.csv")
    df_test.to_csv("./data/split/test_data.csv")

if __name__ == "__main__":
    data_split()