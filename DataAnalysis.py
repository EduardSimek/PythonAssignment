

import pandas as pd

class ExcelDataReader:
    def __init__(self, file_path):
        self.file_path = file_path 

    def read_and_clean_file(self):
        try:
            df = pd.read_excel(self.file_path) 
            print("File read successfully. Here are the first few rows:")
            print(df.head())
            print(df.info())

            #Identify and remove empty columns
            empty_columns = [col for col in df.columns if df[col].isnull().all()]
            print("Empty columns:", empty_columns)

            #Removing empty columns
            print("Removing all empty columns: ") 
            columns_to_remove = ['category', 'cellar_area', 'currency', 'date_added', 'date_construction_completion', 'date_reserved', 
                                 'date_sale_completion', 'date_sold', 'energy_efficiency', 'equipment', 'phase', 
                               'files', 'images', 'bath_count', 'garages', 'baths']
            df = df.drop(columns=columns_to_remove, errors='ignore')

            print("\nDataFrame after removing specified columns:")
            print(df.head())
            
            #Removing duplicate rows
            print("\nDuplicate rows before removal:", df.duplicated().sum())
            df = df.drop_duplicates()
            print("Duplicate rows after removal:", df.duplicated().sum())

            print("\nData after cleaning:")
            print(df.head())
            print(df.info())

            cleaned_file_path = r"C:\Python Assignment\cleaned_data.xls"
            df.to_csv(cleaned_file_path, index=False)
            print(f"Cleaned data saved to {cleaned_file_path}")

            #Group data by developer name, aggregate and identify top dev
            self.find_top_dev(df)

        except FileNotFoundError:
            print("File not found. Ensure the file path is correct and try again.")
        except PermissionError:
            print("Permission denied. Check your file permissions or try running with elevated privileges.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def aggregate_and_find_top_developer(self, df):
        # Ensure 'developer_name', 'external_id', and 'price' columns exist before proceeding
        if all(col in df.columns for col in ['developer_name', 'external_id', 'price']):
            developer_sales = df.groupby('developer_name').agg({'external_id': 'count', 'price': 'sum'}) \
                                .rename(columns={'external_id': 'total_units_sold', 'price': 'total_sales_revenue'})

            top_developer = developer_sales.sort_values(by='total_units_sold', ascending=False).head(1)
            print("\nTop developer by units sold:")
            print(top_developer)
        else:
            print("Required columns for aggregation are missing.")


file_path = r"C:\Python Assignment\market-units-available-anonymized.xls"
reader = ExcelDataReader(file_path)
df_cleaned = reader.read_and_clean_file()