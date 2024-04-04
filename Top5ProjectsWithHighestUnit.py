import pandas as pd 

class Top5ProjectsWithMaxUnits:
    def __init__(self, file_path):
        self.file_path = file_path 
        self.df = self.read_file()

    def read_file(self):
        try:
            df = pd.read_excel(self.file_path)
            print("Read file successfully") 
            return df 
        except FileNotFoundError:
            print("File not found. Ensure that file path is correct and try again")
        except Exception as e:
            print(f"An error occured: {e}")
            return None 
        
    def totalNumOfUnits(self):
        if self.df is not None:
            project_sales = self.df.groupby("project_name").agg({"external_id": "count"})\
                                    .rename(columns={"external_id": "total_units_sold"})
            return project_sales
                                    
        else:
            print("DataFrame is not loaded")
            return None
        
    def identify_top_5_projects(self):
        project_sales = self.totalNumOfUnits()
        if project_sales is not None:
            top_5_projects = project_sales.sort_values(by="total_units_sold", ascending=False).head(5)
            print("\nTop 5 projects by units sold ordering in DESC order: ")
            print(top_5_projects)           
        else:
            print("Project sales data is not available")


file_path = r"C:\Python Assignment\market-units-raw-sales-anonymized.xlsx"
analyzer = Top5ProjectsWithMaxUnits(file_path)
analyzer.identify_top_5_projects()

