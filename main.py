from src import load_data, clean_data, transform, save_data, report, filter_data
from src import analyze, sort_data, group_data, stats, visualizations

def main():
    dataset = load_data.load_dataset()
    dataset = clean_data.clean_dataset(dataset)
    dataset = transform.transform_dataset(dataset)
    save_data.save_dataset(dataset)
    report.generate_report(dataset)
    filter_data.filter_data(dataset)
    analyze.analyze_data(dataset)
    sort_data.sort_data(dataset)
    group_data.group_data(dataset)
    stats.statistical_analysis(dataset)

    # Bonus task: Visualizations only
    visualizations.generate_visualizations(dataset)

    print("🎉 Bonus task (Visualizations) completed successfully!")

if __name__ == "__main__":
    main()












