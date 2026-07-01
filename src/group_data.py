def group_data(dataset):
    print("\n--- Grouping Dataset ---")

    # Average Marks by Grade
    print("\nAverage Marks by Grade:\n", dataset.groupby("Grade")["Marks"].mean())

    # Average Marks by Performance Category
    print("\nAverage Marks by Performance:\n", dataset.groupby("Performance")["Marks"].mean())

    # Average Performance_Score by Grade
    print("\nAverage Performance_Score by Grade:\n", dataset.groupby("Grade")["Performance_Score"].mean())

