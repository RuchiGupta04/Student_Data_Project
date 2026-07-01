import pandas as pd

def generate_report(dataset):
    print("\n--- Report Generation ---")

    total_students = len(dataset)
    passed_students = (dataset['Grade'] != "D").sum()
    failed_students = (dataset['Grade'] == "D").sum()
    highest_marks = dataset['Marks'].max()
    lowest_marks = dataset['Marks'].min()
    average_marks = dataset['Marks'].mean()
    average_attendance = dataset['Attendance'].mean()
    grade_distribution = dataset['Grade'].value_counts()

    report_data = {
        "Total Students": [total_students],
        "Passed Students": [passed_students],
        "Failed Students": [failed_students],
        "Highest Marks": [highest_marks],
        "Lowest Marks": [lowest_marks],
        "Average Marks": [average_marks],
        "Average Attendance": [average_attendance]
    }

    report_df = pd.DataFrame(report_data)
    report_df.to_csv("output/report.csv", index=False)

    # Optional: save grade distribution separately
    grade_distribution.to_csv("output/grade_distribution.csv")

    print("✅ Report saved as output/report.csv")



