import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

DATA_PATH = "1_Data/New Raw/"

files = [
    "attendance.csv",
    "events.json",
    "registrations.csv",
    "sponsors.parquet"
]

VISUAL_PATH = "2_Visualizations/"
os.makedirs(VISUAL_PATH, exist_ok=True)


def analyze_dataset(file_path):

    print(f"\n{'='*70}")
    print(f"ANALYZING FILE: {os.path.basename(file_path)}")
    print(f"{'='*70}")

    file_name = os.path.basename(file_path).split('.')[0]

    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    if file_path.endswith(".csv"):
        df = pd.read_csv(file_path)

    elif file_path.endswith(".json"):
        df = pd.read_json(file_path)

    elif file_path.endswith(".parquet"):
        df = pd.read_parquet(file_path)

    else:
        print("Unsupported File Format")
        return

    print("\nSHAPE OF DATASET")
    print(df.shape)

    print("\nDATA TYPES")
    print(df.dtypes)

    print("\nMISSING VALUES (COLUMN-WISE)")
    print(df.isnull().sum())

    total_missing = df.isnull().sum().sum()

    print(f"\nTOTAL MISSING VALUES: {total_missing}")

    if total_missing == 0:
        print("No Missing Values Found")
    else:
        print("Missing Values Present")

    duplicate_count = df.duplicated().sum()

    print(f"\nDUPLICATE ROWS: {duplicate_count}")

    if duplicate_count == 0:
        print("No Duplicate Rows Found")
    else:
        print("Duplicate Rows Present")

    print("\nUNIQUE VALUES PER COLUMN")
    print(df.nunique())

    print("\nSTATISTICAL SUMMARY")
    print(df.describe(include='all'))

    numeric_cols = df.select_dtypes(include=np.number).columns

    if len(numeric_cols) == 0:
        print("\nNo Numerical Columns Found")
        return

    print("\nOUTLIER DETECTION (IQR METHOD)")

    for col in numeric_cols:

        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)

        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        outliers = df[
            (df[col] < lower_bound) |
            (df[col] > upper_bound)
        ]

        print(f"{col}: {len(outliers)} outliers")

    for col in numeric_cols:

        plt.figure(figsize=(8, 5))

        plt.hist(df[col].dropna(), bins=20)

        plt.title(f"Histogram - {col}")
        plt.xlabel(col)
        plt.ylabel("Frequency")

        hist_path = os.path.join(
            VISUAL_PATH,
            f"{file_name}_{col}_histogram.png"
        )

        plt.savefig(hist_path)
        plt.close()

        print(f"Histogram Saved: {hist_path}")

        mean = df[col].mean()
        std = df[col].std()

        x = np.linspace(df[col].min(), df[col].max(), 100)

        y = (1 / (std * np.sqrt(2 * np.pi))) * \
            np.exp(-0.5 * ((x - mean) / std) ** 2)

        plt.figure(figsize=(8, 5))

        plt.hist(
            df[col].dropna(),
            bins=20,
            density=True
        )

        plt.plot(x, y)

        plt.title(f"Normal Distribution Curve - {col}")
        plt.xlabel(col)
        plt.ylabel("Density")

        normal_curve_path = os.path.join(
            VISUAL_PATH,
            f"{file_name}_{col}_normal_curve.png"
        )

        plt.savefig(normal_curve_path)
        plt.close()

        print(f"Normal Curve Saved: {normal_curve_path}")

        plt.figure(figsize=(8, 5))

        plt.boxplot(
            df[col].dropna(),
            vert=False
        )

        plt.title(f"Boxplot - {col}")
        plt.xlabel(col)

        boxplot_path = os.path.join(
            VISUAL_PATH,
            f"{file_name}_{col}_boxplot.png"
        )

        plt.savefig(boxplot_path)
        plt.close()

        print(f"Boxplot Saved: {boxplot_path}")

    print("\nANALYSIS COMPLETE")


print("\nFILES INSIDE RAW FOLDER:")
print(os.listdir(DATA_PATH))

for file in files:

    file_path = os.path.join(DATA_PATH, file)

    analyze_dataset(file_path)

print("\nCOMPLETE DATA ANALYSIS FINISHED!")