import matplotlib.pyplot as plt

def generate_visualizations(dataset):
    print("\n--- Generating Visualizations ---")

    # Grade distribution pie chart
    grade_counts = dataset['Grade'].value_counts()
    plt.figure(figsize=(6,6))
    plt.pie(grade_counts, labels=grade_counts.index, autopct='%1.1f%%', startangle=90)
    plt.title("Grade Distribution")
    plt.savefig("output/grade_distribution_pie.png")
    plt.close()

    # Pass/Fail bar chart
    pass_fail = {
        "Passed": (dataset['Grade'] != "D").sum(),
        "Failed": (dataset['Grade'] == "D").sum()
    }
    plt.figure(figsize=(6,4))
    plt.bar(pass_fail.keys(), pass_fail.values(), color=['green','red'])
    plt.title("Pass vs Fail Students")
    plt.savefig("output/pass_fail_bar.png")
    plt.close()

    print("✅ Visualizations saved in output folder.")
