import pandas as pd

def inspect_dataset(df):
    print("\n--- Missing Values ---")
    print(df.isnull().sum())

    print("\n--- Duplicate Records ---")
    print(df.duplicated().sum())

    print("\n--- Descriptive Statistics ---")
    print(df.describe())

    print("\n--- Memory Usage ---")
    print(df.memory_usage(deep=True))

    print("\n--- Summary Information ---")
    print(df.info())
