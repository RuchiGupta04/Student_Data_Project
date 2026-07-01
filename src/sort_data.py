def sort_data(dataset):
    print("\n--- Sorting Dataset ---")

    # Sort by Marks
    print("\nSorted by Marks:\n", dataset.sort_values(by="Marks", ascending=False).head())

    # Sort by Attendance
    print("\nSorted by Attendance:\n", dataset.sort_values(by="Attendance", ascending=False).head())

    # Sort by Study Hours
    print("\nSorted by Study Hours:\n", dataset.sort_values(by="StudyHours", ascending=False).head())

