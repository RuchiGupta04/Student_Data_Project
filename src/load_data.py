import pandas as pd

def load_dataset():
    # CSV file ko read karo
    df = pd.read_csv("data/student_dataset_v2.csv")
    print(" Dataset loaded successfully")
    return df
