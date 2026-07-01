def filter_data(dataset):
    print("\n--- Filtering Dataset ---")

    # Toppers: Grade A students
    toppers = dataset[dataset['Grade'] == "A"]
    toppers.to_csv("output/toppers.csv", index=False)

    # Failed students: Grade D students
    failed = dataset[dataset['Grade'] == "D"]
    failed.to_csv("output/failed_students.csv", index=False)

    # Students with attendance below 75%
    low_attendance = dataset[dataset['Attendance'] < 75]
    low_attendance.to_csv("output/low_attendance.csv", index=False)

    # Students studying more than 8 hours
    hard_workers = dataset[dataset['StudyHours'] > 8]
    hard_workers.to_csv("output/hard_workers.csv", index=False)

    print("✅ Filtered datasets saved in output folder.")



    
