import pandas as pd 

class ExcelDataAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path 
        self.df = self.read_file() 

    def read_file(self):
        try:
            df = pd.read_excel(self.file_path)
            print("File read successfully") 
            return df 
        except FileNotFoundError:
            print("File not found. Ensure the file path is correct and try again.")
        except Exception as e:
            print(f"An error occured while reading the file: {e}")
            return None 
        
    def clean_data(self):
        if self.df is not None:
            self.df["price"] = pd.to_numeric(self.df["price"], errors="coerce")
            self.df = self.df.dropna(subset=["price"])
        else:
            print("DataFrame is not loaded.")
        
    def find_top_dev(self):
        df = self.df 
        if df is not None and all(col in df.columns for col in ["developer_name", "external_id", "price"]):
            self.clean_data()
            developer_sales = df.groupby("developer_name").agg({"external_id": "count", "price": "sum"})\
            .rename(columns={"external_id": "total_units_sold", "price": "total_sales_revenue"})
            top_developer = developer_sales.sort_values(by="total_units_sold",ascending=False).head(1)
            print("\nTop developer by units sold:")
            print(top_developer) 
        else:
            print("Required columns for aggregation are missing or DateFrame is not loaded")

file_path = r"C:\Python Assignment\market-units-raw-sales-anonymized.xlsx"
reader = ExcelDataAnalyzer(file_path)
df_cleaned = reader.find_top_dev()

