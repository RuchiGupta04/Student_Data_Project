def analyze_data(dataset):
    print("\n--- Data Analysis ---")

    # Average Marks
    print("Average Marks:", dataset['Marks'].mean())

    # Highest Marks
    print("Highest Marks:", dataset['Marks'].max())

    # Lowest Marks
    print("Lowest Marks:", dataset['Marks'].min())

    # Average Attendance
    print("Average Attendance:", dataset['Attendance'].mean())

    # Average Study Hours
    print("Average Study Hours:", dataset['StudyHours'].mean())

    # Pass/Fail Percentage
    pass_count = (dataset['Grade'] != "D").sum()
    fail_count = (dataset['Grade'] == "D").sum()
    total = len(dataset)

    print("Pass Percentage:", (pass_count / total) * 100)
    print("Fail Percentage:", (fail_count / total) * 100)

    # Grade Distribution
    print("\nGrade Distribution:\n", dataset['Grade'].value_counts())
def analyze_data(dataset):
    print("\n--- Data Analysis ---")

    # Average Marks
    print("Average Marks:", dataset['Marks'].mean())

    # Highest Marks
    print("Highest Marks:", dataset['Marks'].max())

    # Lowest Marks
    print("Lowest Marks:", dataset['Marks'].min())

    # Average Attendance
    print("Average Attendance:", dataset['Attendance'].mean())

    # Average Study Hours
    print("Average Study Hours:", dataset['StudyHours'].mean())

    # Pass/Fail Percentage
    pass_count = (dataset['Grade'] != "D").sum()
    fail_count = (dataset['Grade'] == "D").sum()
    total = len(dataset)

    print("Pass Percentage:", (pass_count / total) * 100)
    print("Fail Percentage:", (fail_count / total) * 100)

    # Grade Distribution
    print("\nGrade Distribution:\n", dataset['Grade'].value_counts())

