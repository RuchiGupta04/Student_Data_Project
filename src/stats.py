import pandas as pd

def statistical_analysis(dataset):
    print("\n--- Statistical Analysis ---")

    # Mean
    print("Mean:\n", dataset.mean(numeric_only=True))

    # Median
    print("\nMedian:\n", dataset.median(numeric_only=True))

    # Mode
    print("\nMode:\n", dataset.mode(numeric_only=True).iloc[0])

    # Standard Deviation
    print("\nStandard Deviation:\n", dataset.std(numeric_only=True))

    # Variance
    print("\nVariance:\n", dataset.var(numeric_only=True))

    # Correlation Matrix
    print("\nCorrelation Matrix:\n", dataset.corr(numeric_only=True))

