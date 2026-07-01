def transform_dataset(dataset):
    print("\n--- Transforming Dataset ---")

    # Grade column
    def grade(marks):
        if marks >= 85:
            return "A"
        elif marks >= 70:
            return "B"
        elif marks >= 55:
            return "C"
        else:
            return "D"
    dataset['Grade'] = dataset['Marks'].apply(grade)

    # Performance Category
    def performance(row):
        if row['Attendance'] >= 80 and row['StudyHours'] >= 6:
            return "High"
        elif row['Attendance'] >= 60 and row['StudyHours'] >= 4:
            return "Medium"
        else:
            return "Low"
    dataset['Performance'] = dataset.apply(performance, axis=1)

    # Custom Performance Score
    dataset['Performance_Score'] = (
        (dataset['Marks'] * 0.6) + (dataset['Attendance'] * 0.2) + (dataset['StudyHours'] * 0.2)
    )

    print("✅ Transformation complete (Grade, Performance, Performance_Score added)")
    return dataset



