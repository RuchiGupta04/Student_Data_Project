import pandas as pd

def clean_dataset(df):
    # Step 1: Missing values handle karo
    df['Marks'].fillna(df['Marks'].mean(), inplace=True)
    df['Attendance'].fillna(df['Attendance'].median(), inplace=True)
    df['StudyHours'].fillna(0, inplace=True)

    # Step 2: Duplicates remove karo
    df.drop_duplicates(inplace=True)

    # Step 3: Invalid values fix karo
    df['Attendance'] = df['Attendance'].clip(0, 100)
    df['StudyHours'] = df['StudyHours'].apply(lambda x: max(x, 0))

    # Step 4: Cleaned dataset save karo
    df.to_csv("output/cleaned_data.csv", index=False)
    print("✅ Cleaned dataset saved as output/cleaned_data.csv")

    return df
