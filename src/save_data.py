def save_dataset(df, filename="output/final_dataset.csv"):
    df.to_csv(filename, index=False)
    print(f"💾 Dataset saved successfully at {filename}")
