"""
============================================================
   Data Analysis & Visualization Program
   SalesDataAnalyzer — OOP-Based Menu-Driven Application
============================================================
"""

# ─────────────────────────────────────────
# IMPORTS
# ─────────────────────────────────────────
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings
warnings.filterwarnings('ignore')


# ─────────────────────────────────────────
# HELPER: Create Sample Dataset
# ─────────────────────────────────────────
def create_sample_dataset():
    """Create a sample sales_data.csv for demonstration."""
    os.makedirs('data', exist_ok=True)
    sample_data = {
        'SalesID':  [101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
                     111, 112, 113, 114, 115, 116, 117, 118, 119, 120],
        'Product':  ['Product A', 'Product B', 'Product C', 'Product D', 'Product E',
                     'Product A', 'Product B', 'Product C', 'Product D', 'Product E',
                     'Product A', 'Product B', 'Product C', 'Product D', 'Product E',
                     'Product A', 'Product B', 'Product C', 'Product D', 'Product E'],
        'Region':   ['North', 'East', 'West Coast', 'South', 'Central',
                     'North', 'East', 'West Coast', 'South', 'Central',
                     'North', 'East', 'West Coast', 'South', 'Central',
                     'North', 'East', 'West Coast', 'South', 'Central'],
        'Sales':    [500, 600, 700, 800, 550, 480, 620, 710, 830, 560,
                     510, 590, 690, 810, 540, 520, 610, 720, 820, 570],
        'Profit':   [100, 150, 200, 250, 120,  90, 160, 210, 260, 130,
                     110, 140, 190, 255, 115, 105, 155, 205, 245, 125],
        'Year':     [2022, 2022, 2022, 2022, 2022, 2023, 2023, 2023, 2023, 2023,
                     2024, 2024, 2024, 2024, 2024, 2022, 2023, 2024, 2022, 2023],
        'Quantity': [10, 12, 14, 16, 11,  9, 13, 15, 17, 12,
                     10, 11, 13, 16, 10, 11, 12, 14, 15, 11]
    }
    df = pd.DataFrame(sample_data)
    df.to_csv('data/sales_data.csv', index=False)
    print("Sample dataset created at: data/sales_data.csv")
    print(df.head())


# ─────────────────────────────────────────
# CLASS: SalesDataAnalyzer
# ─────────────────────────────────────────
class SalesDataAnalyzer:
    """
    OOP-based Sales Data Analyzer.
    Encapsulates all data loading, exploration, manipulation,
    analysis, and visualization functionalities.
    """

    def __init__(self):
        self.df = None
        self.filepath = None
        self.last_fig = None

    # ──────────────────────────────────────
    # 1. LOAD DATASET
    # ──────────────────────────────────────
    def load_data(self, filepath):
        """Load sales data from a CSV file."""
        try:
            self.df = pd.read_csv(filepath)
            self.filepath = filepath
            print(f"\nDataset loaded successfully from '{filepath}'!")
            print(f"Shape: {self.df.shape[0]} rows x {self.df.shape[1]} columns")
        except FileNotFoundError:
            print(f"\nError: File '{filepath}' not found. Please check the path.")
        except Exception as e:
            print(f"\nAn error occurred while loading: {e}")

    # ──────────────────────────────────────
    # 2. EXPLORE DATA
    # ──────────────────────────────────────
    def explore_data(self, option):
        """Explore the dataset using various options."""
        if self.df is None:
            print("\nNo dataset loaded. Please load a dataset first.")
            return
        match option:
            case 1:
                print("\nFirst 5 rows:")
                print(self.df.head().to_string())
            case 2:
                print("\nLast 5 rows:")
                print(self.df.tail().to_string())
            case 3:
                print("\nColumn Names:")
                print(list(self.df.columns))
            case 4:
                print("\nData Types:")
                print(self.df.dtypes)
            case 5:
                print("\nBasic Info:")
                self.df.info()
            case _:
                print("\nInvalid option.")

    # ──────────────────────────────────────
    # 3. DATAFRAME OPERATIONS
    # ──────────────────────────────────────
    def dataframe_operations(self, option, column=None):
        """Perform various DataFrame operations."""
        if self.df is None:
            print("\nNo dataset loaded.")
            return

        num_cols = self.df.select_dtypes(include=np.number).columns.tolist()

        match option:
            case 1:
                col = column if column and column in self.df.columns else num_cols[0]
                arr = self.df[col].to_numpy()
                print(f"\nNumPy array from '{col}':")
                print(arr)
                print(f"Slice [0:5]: {arr[0:5]}")
                return arr
            case 2:
                print(f"\nElement-wise operations (x1.1) on numeric columns: {num_cols}")
                result = self.df[num_cols] * 1.1
                print("After multiplying all numeric values by 1.1 (10% increase):")
                print(result.head().to_string())
                return result
            case 3:
                df_copy = self.df.copy()
                combined = pd.concat([self.df, df_copy], ignore_index=True)
                print(f"\nCombined DataFrame (concat) shape: {combined.shape}")
                print(combined.head().to_string())
                return combined
            case 4:
                col = column if column and column in self.df.columns else 'Region'
                groups = {name: group for name, group in self.df.groupby(col)}
                print(f"\nSplit by '{col}':")
                for name, grp in groups.items():
                    print(f"  '{name}': {len(grp)} rows")
                return groups
            case _:
                print("\nInvalid option.")

    # ──────────────────────────────────────
    # 4. HANDLE MISSING DATA
    # ──────────────────────────────────────
    def handle_missing_data(self, option):
        """Handle missing values in the dataset."""
        if self.df is None:
            print("\nNo dataset loaded.")
            return

        match option:
            case 1:
                rows_with_na = self.df[self.df.isnull().any(axis=1)]
                if rows_with_na.empty:
                    print("\nNo missing values found in the dataset!")
                else:
                    print("\nRows with missing values:")
                    print(rows_with_na.to_string())
            case 2:
                num_cols = self.df.select_dtypes(include=np.number).columns
                self.df[num_cols] = self.df[num_cols].fillna(self.df[num_cols].mean())
                print("\nMissing values filled with column mean!")
            case 3:
                before = len(self.df)
                self.df.dropna(inplace=True)
                after = len(self.df)
                print(f"\nDropped rows with missing values. ({before} -> {after} rows)")
            case 4:
                fill_val = input("Enter the value to replace missing data with: ").strip()
                try:
                    fill_val = float(fill_val)
                except ValueError:
                    pass
                self.df.fillna(fill_val, inplace=True)
                print(f"\nMissing values replaced with '{fill_val}'!")
            case _:
                print("\nInvalid option.")

    # ──────────────────────────────────────
    # 5. DESCRIPTIVE STATISTICS
    # ──────────────────────────────────────
    def generate_statistics(self):
        """Generate descriptive statistics for the dataset."""
        if self.df is None:
            print("\nNo dataset loaded.")
            return

        print("\nDescriptive Statistics:")
        print(self.df.describe().to_string())

        num_cols = self.df.select_dtypes(include=np.number).columns
        print("\nAdditional Statistical Functions:")
        for col in num_cols:
            arr = self.df[col].to_numpy()
            print(f"\n  Column: {col}")
            print(f"    std       = {np.std(arr):.2f}")
            print(f"    variance  = {np.var(arr):.2f}")
            print(f"    25th pct  = {np.percentile(arr, 25):.2f}")
            print(f"    75th pct  = {np.percentile(arr, 75):.2f}")

        print("\nAggregating Functions:")
        print(f"  sum()   = {self.df[num_cols].sum().to_dict()}")
        print(f"  mean()  = {self.df[num_cols].mean().round(2).to_dict()}")
        print(f"  count() = {self.df[num_cols].count().to_dict()}")

    # ──────────────────────────────────────
    # 6. DATA VISUALIZATION
    # ──────────────────────────────────────
    def visualize_data(self, plot_type, x_col=None, y_col=None):
        """Create various visualizations using Matplotlib and Seaborn."""
        if self.df is None:
            print("\nNo dataset loaded.")
            return

        num_cols = self.df.select_dtypes(include=np.number).columns.tolist()
        if not x_col or x_col not in self.df.columns:
            x_col = num_cols[0] if num_cols else None
        if not y_col or y_col not in self.df.columns:
            y_col = num_cols[1] if len(num_cols) > 1 else num_cols[0]

        fig, ax = plt.subplots(figsize=(10, 6))

        match plot_type:
            case 1:  # Bar
                self.df.groupby('Product')[y_col].sum().plot(
                    kind='bar', ax=ax, color='steelblue', edgecolor='black')
                ax.set_title(f'Bar Plot: {y_col} by Product', fontsize=14)
                ax.set_xlabel('Product')
                ax.set_ylabel(y_col)
                ax.legend([y_col])
                print(f"\nGenerating bar plot...")
                print(f"Bar plot displayed successfully!")
            case 2:  # Line
                self.df.groupby('Year')[y_col].sum().plot(
                    kind='line', ax=ax, marker='o', color='tomato')
                ax.set_title(f'Line Plot: {y_col} over Year', fontsize=14)
                ax.set_xlabel('Year')
                ax.set_ylabel(y_col)
                ax.legend([y_col])
                print(f"\nGenerating line plot...")
                print(f"Line plot displayed successfully!")
            case 3:  # Scatter
                ax.scatter(self.df[x_col], self.df[y_col], color='purple', alpha=0.7)
                ax.set_title(f'Scatter Plot: {x_col} vs {y_col}', fontsize=14)
                ax.set_xlabel(x_col)
                ax.set_ylabel(y_col)
                print(f"\nGenerating scatter plot...")
                print(f"Scatter plot displayed successfully!")
            case 4:  # Pie
                pie_data = self.df.groupby('Product')[y_col].sum()
                ax.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=140)
                ax.set_title(f'Pie Chart: {y_col} by Product', fontsize=14)
                print(f"\nGenerating pie chart...")
                print(f"Pie chart displayed successfully!")
            case 5:  # Histogram
                ax.hist(self.df[x_col], bins=10, color='green', edgecolor='black')
                ax.set_title(f'Histogram: {x_col}', fontsize=14)
                ax.set_xlabel(x_col)
                ax.set_ylabel('Frequency')
                print(f"\nGenerating histogram...")
                print(f"Histogram displayed successfully!")
            case 6:  # Stack Plot
                pivot = self.df.pivot_table(
                    values=y_col, index='Year', columns='Product',
                    aggfunc='sum', fill_value=0)
                pivot.plot(kind='bar', stacked=True, ax=ax)
                ax.set_title(f'Stacked Bar: {y_col} by Year and Product', fontsize=14)
                ax.set_xlabel('Year')
                ax.set_ylabel(y_col)
                print(f"\nGenerating stack plot...")
                print(f"Stack plot displayed successfully!")
            case _:
                print("\nInvalid plot type.")
                plt.close(fig)
                return

        plt.tight_layout()
        self.last_fig = fig
        plt.show()

    # ──────────────────────────────────────
    # SEABORN VISUALIZATIONS
    # ──────────────────────────────────────
    def seaborn_visualizations(self):
        """Create enhanced visualizations using Seaborn."""
        if self.df is None:
            print("\nNo dataset loaded.")
            return

        num_df = self.df.select_dtypes(include=np.number)
        fig, axes = plt.subplots(1, 2, figsize=(16, 6))

        sns.heatmap(num_df.corr(), annot=True, cmap='coolwarm', ax=axes[0], fmt='.2f')
        axes[0].set_title('Correlation Heatmap', fontsize=13)

        if 'Sales' in self.df.columns and 'Product' in self.df.columns:
            sns.boxplot(data=self.df, x='Product', y='Sales', palette='Set2', ax=axes[1])
            axes[1].set_title('Box Plot: Sales by Product', fontsize=13)
        else:
            sns.boxplot(data=num_df, ax=axes[1])
            axes[1].set_title('Box Plot', fontsize=13)

        plt.tight_layout()
        self.last_fig = fig
        plt.show()
        print("\nSeaborn visualizations displayed successfully!")

    # ──────────────────────────────────────
    # MULTI-SUBPLOTS
    # ──────────────────────────────────────
    def multi_subplots(self):
        """Display multiple plots in a single figure."""
        if self.df is None:
            print("\nNo dataset loaded.")
            return

        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        fig.suptitle('Sales Data - Multi-Plot Overview', fontsize=16, fontweight='bold')

        self.df.groupby('Product')['Sales'].sum().plot(
            kind='bar', ax=axes[0, 0], color='steelblue', edgecolor='black')
        axes[0, 0].set_title('Total Sales by Product')
        axes[0, 0].set_ylabel('Sales')

        self.df.groupby('Year')['Sales'].sum().plot(
            kind='line', ax=axes[0, 1], marker='o', color='tomato')
        axes[0, 1].set_title('Total Sales by Year')
        axes[0, 1].set_ylabel('Sales')

        axes[1, 0].hist(self.df['Sales'], bins=10, color='green', edgecolor='black')
        axes[1, 0].set_title('Sales Distribution')
        axes[1, 0].set_xlabel('Sales')
        axes[1, 0].set_ylabel('Frequency')

        if 'Profit' in self.df.columns:
            axes[1, 1].scatter(self.df['Sales'], self.df['Profit'], color='purple', alpha=0.7)
            axes[1, 1].set_title('Sales vs Profit')
            axes[1, 1].set_xlabel('Sales')
            axes[1, 1].set_ylabel('Profit')
        else:
            axes[1, 1].axis('off')

        plt.tight_layout()
        self.last_fig = fig
        plt.show()
        print("\nMulti-subplot figure displayed successfully!")

    # ──────────────────────────────────────
    # 7. SAVE VISUALIZATION
    # ──────────────────────────────────────
    def save_visualization(self, filename='visualization.png'):
        """Save the last generated plot to a file."""
        if self.last_fig is None:
            print("\nNo visualization to save. Please generate a plot first.")
            return
        self.last_fig.savefig(filename, dpi=150, bbox_inches='tight')
        print(f"\nVisualization saved as '{filename}' successfully!")

    # ──────────────────────────────────────
    # AGGREGATE FUNCTIONS
    # ──────────────────────────────────────
    def aggregate_functions(self, group_col='Product', agg_col='Sales'):
        """Apply aggregating functions like sum, mean, etc."""
        if self.df is None:
            print("\nNo dataset loaded.")
            return
        print(f"\nAggregations of '{agg_col}' grouped by '{group_col}':")
        result = self.df.groupby(group_col)[agg_col].agg(['sum', 'mean', 'min', 'max', 'count'])
        print(result.to_string())
        return result

    # ──────────────────────────────────────
    # STATISTICAL ANALYSIS
    # ──────────────────────────────────────
    def statistical_analysis(self):
        """Perform statistical computations."""
        if self.df is None:
            print("\nNo dataset loaded.")
            return
        num_cols = self.df.select_dtypes(include=np.number).columns
        print("\nStatistical Analysis:")
        for col in num_cols:
            arr = self.df[col].to_numpy()
            print(f"\n  {col}:")
            print(f"    std()      -> {np.std(arr):.4f}")
            print(f"    var()      -> {np.var(arr):.4f}")
            print(f"    quantile() -> Q1={np.quantile(arr, 0.25):.2f}, Q3={np.quantile(arr, 0.75):.2f}")

    # ──────────────────────────────────────
    # PIVOT TABLE
    # ──────────────────────────────────────
    def create_pivot_table(self, values='Sales', index='Region', columns='Product'):
        """Generate pivot tables for data summarization."""
        if self.df is None:
            print("\nNo dataset loaded.")
            return
        pivot = pd.pivot_table(
            self.df, values=values, index=index,
            columns=columns, aggfunc='sum', fill_value=0)
        print(f"\nPivot Table ({values} by {index} x {columns}):")
        print(pivot.to_string())
        return pivot

    # ──────────────────────────────────────
    # SEARCH / SORT / FILTER
    # ──────────────────────────────────────
    def search_records(self, column, value):
        """Search for specific records."""
        if self.df is None:
            print("\nNo dataset loaded.")
            return
        result = self.df[self.df[column] == value]
        print(f"\nSearch '{value}' in '{column}': {len(result)} records found")
        print(result.to_string())
        return result

    def sort_data(self, column, ascending=False):
        """Sort data by a column."""
        if self.df is None:
            print("\nNo dataset loaded.")
            return
        sorted_df = self.df.sort_values(by=column, ascending=ascending)
        order = 'ascending' if ascending else 'descending'
        print(f"\nSorted by '{column}' ({order}):")
        print(sorted_df.head(10).to_string())
        return sorted_df

    def filter_data(self, column, condition, value):
        """Filter data based on a condition."""
        if self.df is None:
            print("\nNo dataset loaded.")
            return
        ops = {'>': '__gt__', '<': '__lt__', '==': '__eq__', '>=': '__ge__', '<=': '__le__'}
        if condition not in ops:
            print("\nUnsupported condition. Use >, <, ==, >=, <=")
            return
        result = self.df[getattr(self.df[column], ops[condition])(value)]
        print(f"\nFilter '{column} {condition} {value}': {len(result)} records found")
        print(result.to_string())
        return result


# ─────────────────────────────────────────
# MENU DISPLAY
# ─────────────────────────────────────────
def display_menu():
    print("\n" + "=" * 60)
    print("========== Data Analysis & Visualization Program ==========")
    print("Please select an option:")
    print("1. Load Dataset")
    print("2. Explore Data")
    print("3. Perform DataFrame Operations")
    print("4. Handle Missing Data")
    print("5. Generate Descriptive Statistics")
    print("6. Data Visualization")
    print("7. Save Visualization")
    print("8. Exit")
    print("=" * 60)


# ─────────────────────────────────────────
# MAIN PROGRAM
# ─────────────────────────────────────────
def main():
    analyzer = SalesDataAnalyzer()

    while True:
        display_menu()

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        match choice:
            # ── 1. Load Dataset ──────────────────────
            case 1:
                print("\n== Load Dataset ==")
                path = input("Enter the path of the dataset (CSV file): ").strip()
                analyzer.load_data(path)

            # ── 2. Explore Data ──────────────────────
            case 2:
                print("\n== Explore Data ==")
                print("1. Display the first 5 rows")
                print("2. Display the last 5 rows")
                print("3. Display column names")
                print("4. Display data types")
                print("5. Display basic info")
                try:
                    sub = int(input("Enter your choice: "))
                    analyzer.explore_data(sub)
                except ValueError:
                    print("Invalid input.")

            # ── 3. DataFrame Operations ───────────────
            case 3:
                print("\n== Perform DataFrame Operations ==")
                print("1. Convert column to NumPy array & slice")
                print("2. Element-wise mathematical operations")
                print("3. Combine DataFrames (concat)")
                print("4. Split DataFrame by Region")
                try:
                    sub = int(input("Enter your choice: "))
                    match sub:
                        case 1:
                            col = input("Enter column name to convert: ").strip()
                            analyzer.dataframe_operations(sub, column=col)
                        case _:
                            analyzer.dataframe_operations(sub)
                except ValueError:
                    print("Invalid input.")

            # ── 4. Handle Missing Data ────────────────
            case 4:
                print("\n== Handle Missing Data ==")
                print("1. Display rows with missing values")
                print("2. Fill missing values with mean")
                print("3. Drop rows with missing values")
                print("4. Replace missing values with a specific value")
                try:
                    sub = int(input("Enter your choice: "))
                    analyzer.handle_missing_data(sub)
                except ValueError:
                    print("Invalid input.")

            # ── 5. Descriptive Statistics ─────────────
            case 5:
                print("\n== Generate Descriptive Statistics ==")
                analyzer.generate_statistics()

            # ── 6. Data Visualization ─────────────────
            case 6:
                print("\n== Data Visualization ==")
                print("1. Bar Plot")
                print("2. Line Plot")
                print("3. Scatter Plot")
                print("4. Pie Chart")
                print("5. Histogram")
                print("6. Stack Plot")
                try:
                    sub = int(input("Enter your choice: "))
                    match sub:
                        case 3:
                            x = input("Enter x-axis column name: ").strip()
                            y = input("Enter y-axis column name: ").strip()
                            analyzer.visualize_data(sub, x_col=x, y_col=y)
                        case 1 | 2 | 4 | 5 | 6:
                            analyzer.visualize_data(sub)
                        case _:
                            print("Invalid plot option.")
                except ValueError:
                    print("Invalid input.")

            # ── 7. Save Visualization ─────────────────
            case 7:
                print("\n== Save Visualization ==")
                fname = input("Enter file name to save the plot (e.g., scatter_plot.png): ").strip()
                analyzer.save_visualization(fname)

            # ── 8. Exit ───────────────────────────────
            case 8:
                print("\nExiting the program. Goodbye!")
                break

            # ── Default ───────────────────────────────
            case _:
                print("\nInvalid choice. Please select 1-8.")


# ─────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────
if __name__ == "__main__":
    # Uncomment the line below to auto-generate a sample dataset:
    # create_sample_dataset()
    main()
