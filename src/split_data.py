import pandas as pd
from sklearn.model_selection import train_test_split

seed = 11

# load raw data
df = pd.read_csv("./data/raw/raw_data.csv")

# split data
df_train, df_val = train_test_split(df, test_size = 0.3, random_state = seed, stratify = df.isFraud)
df_val, df_test = train_test_split(df_val, test_size = 1/3, random_state = seed, stratify = df_val.isFraud)

# save split data
df_train.to_csv("./data/processed/train_data.csv")
df_val.to_csv("./data/processed/validation_data.csv")
df_test.to_csv("./data/processed/test_data.csv")