import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#-----------SalesDataAnalyzer class-----------
class SalesDataAnalyzer:

    locate_file = "sales_data.csv"
    data = pd.read_csv(locate_file)
    
    locate_file2 = "sales_data2.csv"
    data2 = pd.read_csv(locate_file2)
    
    combined_data = pd.concat([data, data2], ignore_index=True)
    
    class Load_Dataset:
        def __init__(self, csv_file):
            self.csv_file = csv_file
            try:
                self.data = pd.read_csv(csv_file)
                print("Sales data loaded successfully.")

            except FileNotFoundError:
                print(f"Error: The file '{csv_file}' was not found.")
                self.data = None

            except pd.errors.EmptyDataError:
                print(f"Error: The file '{csv_file}' is empty.")
                self.data = None
                
            except Exception as e:
                print(f"An unexpected error occurred while loading the data: {e}")
                self.data = None

    class Explore_Data:
        def __init__(self, data):
            self.data = data

    class Dataframe_Operations:
        def __init__(self, data):
            self.data = data

        def mathematical_operations(self):
            
            # Perform mathematical operations
            #calculate total sales
            total=self.data['Total_Sales'] = self.data['Quantity'] * self.data['Sales']
            print(f"Total Sales calculated for first 5 rows:\n{total.head()}")

            #Apply discount
            disc=self.data['Discounted_Price'] = self.data['Sales'] * 0.9  # 10% discount
            print(f"Discounted Price calculated for first 5 rows:\n{disc.head()}")
        
        def combine_dataframes(self):
            # Combine multiple dataframes
            print("Second sales data is loaded.")
            combined_data = pd.concat([self.data, SalesDataAnalyzer.data2], ignore_index=True)
            print(f"Combined DataFrame shape: {combined_data.shape}")
            print(f"Combined DataFrame:\n{combined_data}")


        def split_dataframes(self):
            # Split the dataframes
            split_data_region = self.data[self.data['Region'] == 'East']
            print(f"DataFrames split by East Region \n{split_data_region}")

    class clean_data:
        def __init__(self, dataframe):
            self.dataframe = dataframe

        def display_missing_rows(self):
            missing_rows = self.dataframe[self.dataframe.isnull().any(axis=1)]
            if missing_rows.empty:
                print("No missing values found in the DataFrame.")
            else:
                print(missing_rows)

        def fill_missing_with_mean(self):
            fill_values=self.dataframe.fillna(self.dataframe.mean(numeric_only=True))
            print(f"Missing values filled with mean:\n{fill_values}")

        def drop_missing_rows(self):
            drop=self.dataframe.dropna()
            print(f"Rows with missing values dropped.\n{drop}")

        def replace_missing_with_value(self, value=0):
            replace=self.dataframe.fillna(value)
            print(f"Replaced missing values with {value}:\n{replace}")

    class Statistics:
        def __init__(self, data):
            self.data = data

        def descriptive_stats(self):
            print("\n--- Descriptive Statistics ---")
            numeric_data = self.data.select_dtypes(include=[np.number])
            print(numeric_data.describe().to_string())

        def statistical_analysis(self):
            numeric_data = self.data.select_dtypes(include=[np.number])
            
            print("\n--- Standard Deviation ---")
            print(numeric_data.std().to_string())
            
            print("\n--- Variance ---")
            print(numeric_data.var().to_string())
            
            print("\n--- Skewness ---")
            print(numeric_data.skew().to_string())
            
            print("\n--- Kurtosis ---")
            print(numeric_data.kurtosis().to_string())
            
            print("\n--- Quantiles (25%, 50%, 75%) ---")
            print(numeric_data.quantile([0.25, 0.5, 0.75]).to_string())

        def aggregate_functions(self):
            numeric_cols = self.data.select_dtypes(include=[np.number]).columns.tolist()
            
            if not numeric_cols:
                print("No numeric columns found in the dataset.")
                return
            
            print("\n--- Aggregate Functions ---")
            for col in numeric_cols:
                print(f"\n{col}:")
                print(f"  Sum: {self.data[col].sum():.2f}")
                print(f"  Mean: {self.data[col].mean():.2f}")
                print(f"  Median: {self.data[col].median():.2f}")
                print(f"  Min: {self.data[col].min():.2f}")
                print(f"  Max: {self.data[col].max():.2f}")
                print(f"  Count: {self.data[col].count()}")

        def create_pivot_table(self):
            if 'Sales' in self.data.columns and 'Region' in self.data.columns and 'Product' in self.data.columns:
                pivot = pd.pivot_table(self.data, values='Sales', index='Region',
                                    columns='Product', aggfunc='sum', fill_value=0)
                print("\n--- Pivot Table (Sales by Region and Product) ---\n")
                print(pivot.to_string())
            else:
                print("Required columns (Sales, Region, Product) not found in the dataset.")

    class Visualization:

        def __init__(self, data):
            self.data = data
            self.current_figure = None

        def bar_plot(self, x_col, y_col):
            fig = plt.figure(figsize=(10, 6))
            self.data.plot(x=x_col, y=y_col, kind='bar')
            plt.title(f"{y_col} by {x_col}")
            plt.tight_layout()
            self.current_figure = fig
            plt.show()

        def line_plot(self, x_col, y_col):
            fig = plt.figure(figsize=(10, 6))
            self.data.plot(x=x_col, y=y_col, kind='line')
            plt.title(f"{y_col} Trend Over {x_col}")
            plt.tight_layout()
            self.current_figure = fig
            plt.show()

        def scatter_plot(self, x_col, y_col):
            fig = plt.figure(figsize=(10, 6))
            plt.scatter(self.data[x_col], self.data[y_col])
            plt.title(f"{x_col} vs {y_col}")
            plt.xlabel(x_col)
            plt.ylabel(y_col)
            plt.tight_layout()
            self.current_figure = fig
            plt.show()

        def histogram(self, x_col, y_col):
            fig = plt.figure(figsize=(10, 6))
            self.data[x_col].plot(kind='hist', bins=10)
            plt.title(f"Distribution of {x_col}")
            plt.tight_layout()
            self.current_figure = fig
            plt.show()

        def pie_chart(self, x_col, y_col):
            fig = plt.figure(figsize=(10, 6))
            self.data.set_index(x_col)[y_col].plot(kind='pie', autopct='%1.1f%%')
            plt.title(f"{y_col} Distribution by {x_col}")
            plt.tight_layout()
            self.current_figure = fig
            plt.show()

        def stack_plot(self, x_col, y_col):
            fig = plt.figure(figsize=(10, 6))
            self.data.plot(x=x_col, y=y_col, kind='area', stacked=True)
            plt.title(f"Stack Plot of {y_col} over {x_col}")
            plt.tight_layout()
            self.current_figure = fig
            plt.show()

        def seaborn_heatmap(self, x_col, y_col):
            fig = plt.figure(figsize=(10, 6))
            corr = self.data.corr(numeric_only=True)
            sns.heatmap(corr, annot=True, cmap="coolwarm",linewidths=0.5)
            plt.title("Correlation Heatmap")
            plt.tight_layout()
            self.current_figure = fig
            plt.show()

        def save_plot(self, filename):
            if self.current_figure is not None:
                self.current_figure.savefig(filename, dpi=300, bbox_inches='tight')
                print(f"Visualization saved as {filename} successfully!")
            else:
                print("Error: No plot to save. Please generate a plot first (Option 6).")




def main():
    analyzer = None
    print("\n========== Data Analysis & Visualization Program ==========")
    while True:
        print("\nPlease select an option:")
        print("1. Load Dataset")
        print("2. Explore Data")
        print("3. Perform Dataframes Operations")
        print("4. Handle Missing Data")
        print("5. Generate Descriptive Statistics")
        print("6. Data visualization")
        print("7. Save visualizations")
        print("8. Exit")
        print("============================================================")
        
        choice = input("\nEnter your choice: ")

        if choice == '1':
            print("\n== Load Dataset ==")
            locate_file = input("\nEnter the path to your CSV file [sales_data.csv available]: ")  
            analyzer = SalesDataAnalyzer.Load_Dataset(locate_file)

        elif choice == '2':
            print("== Explore Data ==")
            print("1. Display first 5 rows")
            print("2. Display last 5 rows")
            print("3. Display column names")
            print("4. Display data types")
            print("5. Display basic info")

            sub_choice = input("\nEnter your choice: ")
            if analyzer is not None and analyzer.data is not None:
                explorer = SalesDataAnalyzer.Explore_Data(analyzer.data)
                if sub_choice == '1':
                    print(explorer.data.head())
                elif sub_choice == '2':
                    print(explorer.data.tail())
                elif sub_choice == '3':
                    print("Columns:",list(explorer.data.columns))
                elif sub_choice == '4':
                    print(explorer.data.dtypes)
                elif sub_choice == '5':
                    print(explorer.data.info())
                else:
                    print("\nInvalid choice. Please try again.")
            else:
                print("No data loaded. Please load a dataset first (Select option 1).")

        elif choice == '3':
            print("\n== Perform Dataframe Operations ==")
            print("1. Perform mathematical operations")
            print("2. Combine Multiple DataFrames")
            print("3. Split DataFrames")

            sub_choice = input("\nEnter your choice: ")

            if analyzer is not None and analyzer.data is not None:
                df_ops = SalesDataAnalyzer.Dataframe_Operations(analyzer.data)

                if sub_choice == '1':
                    print("Performing mathematical operations...")
                    df_ops.mathematical_operations()
                elif sub_choice == '2':
                    print("Combining multiple DataFrames...")
                    df_ops.combine_dataframes()
                elif sub_choice == '3':
                    print("Splitting DataFrames...")
                    df_ops.split_dataframes()
                else:
                    print("\nInvalid choice. Please try again.")
            else:
                print("No data loaded. Please load a dataset first.")

        elif choice == '4':
            # Handle missing data operations
            print("\n== Handle Missing Data ==")
            print("1. Display rows with missing values")
            print("2. Fill missing values with mean")
            print("3. Drop rows with missing values")
            print("4. Replace missing values with a specific value")

            data = {
            "Date": ["2024-01-01","2024-01-02","2024-01-03","2024-01-04","2024-01-05"],
            "Product": ["Mobile","Laptop","Chair","Table","Headphones"],
            "Region": ["North","South", np.nan,"East","North"],  
            "Sales": [25000,55000,7000,12000, np.nan],          
            "Profit": [5000,8000,1500,2500,800],
            "Quantity": [5,2,10,4,6]
            }

            df = pd.DataFrame(data)

            sub_choice = input("\nEnter your choice: ")
            cleaner = SalesDataAnalyzer.clean_data(df)

            if sub_choice == '1':
                cleaner.display_missing_rows()
            elif sub_choice == '2':
                cleaner.fill_missing_with_mean()
            elif sub_choice == '3':
                cleaner.drop_missing_rows()
            elif sub_choice == '4':
                cleaner.replace_missing_with_value()
            else:
                print("\nInvalid choice. Please try again.")
        
        elif choice == '5':
            print("\n== Generate Descriptive Statistics ==")
            if analyzer is not None and analyzer.data is not None:
                stats = SalesDataAnalyzer.Statistics(analyzer.data)
                print("\n1. Show Descriptive Statistics (Summary)")
                print("2. Show Statistical Analysis (Std, Var, Skewness, Kurtosis, Quantiles)")
                print("3. Show Aggregate Functions (Sum, Mean, Median, Min, Max, Count)")
                print("4. Show Pivot Table (Sales by Region and Product)")

                sub_choice = input("\nEnter your choice: ")
                try:
                    if sub_choice == '1':
                        stats.descriptive_stats()
                    elif sub_choice == '2':
                        stats.statistical_analysis()
                    elif sub_choice == '3':
                        stats.aggregate_functions()
                    elif sub_choice == '4':
                        stats.create_pivot_table()
                    else:
                        print("Invalid choice. Please enter a number between 1 and 4.")
                except Exception as e:
                    print(f"Error occurred while generating statistics: {e}")
            else:
                print("No data loaded. Please load a dataset first (Select option 1).")

        elif choice == '6':
            print("\n== Data Visualization ==")
            if analyzer is not None and analyzer.data is not None:
                # Get x and y columns upfront
                print("\nAvailable columns:", list(analyzer.data.columns))
                x_col = input("Enter x-axis column name: ")
                y_col = input("Enter y-axis column name: ")
                
                # Validate columns exist
                if x_col not in analyzer.data.columns or y_col not in analyzer.data.columns:
                    print("Invalid column name(s). Please try again.")
                else:
                    viz = SalesDataAnalyzer.Visualization(analyzer.data)
                    analyzer.viz_instance = viz  # Store for option 7
                    print("\n1. Bar Plot")
                    print("2. Line Plot")
                    print("3. Scatter Plot")
                    print("4. Pie Chart")
                    print("5. Histogram")
                    print("6. Stack Plot")
                    print("7. Heatmap")

                    sub_choice = input("\nEnter your choice: ")
                    try:
                        if sub_choice == '1':
                            viz.bar_plot(x_col, y_col)
                            print("Bar plot displayed successfully!")
                        elif sub_choice == '2':
                            viz.line_plot(x_col, y_col)
                            print("Line plot displayed successfully!")
                        elif sub_choice == '3':
                            viz.scatter_plot(x_col, y_col)
                            print("Scatter plot displayed successfully!")
                        elif sub_choice == '4':
                            viz.pie_chart(x_col, y_col)
                            print("Pie chart displayed successfully!")
                        elif sub_choice == '5':
                            viz.histogram(x_col, y_col)
                            print("Histogram displayed successfully!")
                        elif sub_choice == '6':
                            viz.stack_plot(x_col, y_col)
                            print("Stack plot displayed successfully!")
                        elif sub_choice == '7':
                            viz.seaborn_heatmap(x_col, y_col)
                            print("Heatmap displayed successfully!")
                        else:
                            print("Invalid choice.")
                    except Exception as e:
                        print(f"Error creating plot: {e}")
            else:
                print("No data loaded. Please load a dataset first.")

        elif choice == '7':
            print("\n== Save Visualization ==")
            if hasattr(analyzer, 'viz_instance') and analyzer.viz_instance is not None:
                filename = input("Enter file name to save the plot (e.g., sales_plot.png or jpeg): ")
                if filename:
                    analyzer.viz_instance.save_plot(filename)
                else:
                    print("Invalid filename. Please try again.")
            else:
                print("No plot to save. Please generate a plot first using Option 6.")

        elif choice == '8':
            print("\nExiting the program. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please try again.")

        
if __name__ == "__main__":
    main()