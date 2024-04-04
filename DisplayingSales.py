import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

class DataInitializer:
    def __init__(self, file_path):
        self.file_path = file_path 
        self.df = self.load_file()
        self.top_5_project_names = []

    def load_file(self):
        try:
            df = pd.read_excel(self.file_path) 
            print("File was loaded successfully") 
            return df 
        except FileNotFoundError:
            print("File was not found. Try again")
            return None 
        except Exception as e:
            print(f"An error occured while loading the file: {e}")
            return None 
        
    def identify_top_5_projects_by_units(self):
        if self.df is not None:
            project_sales = self.df.groupby("project_name").agg({"external_id": "count"}).rename(columns={"external_id": "total_units_sold"})
            top_5_projects = project_sales.sort_values(by="total_units_sold", ascending=False).head(5)
            print("\nTop 5 projects by units sold: ")
            print(top_5_projects) 
            self.top_5_project_names = top_5_projects.index.tolist()
        else:
            print("DataFrame is not loaded") 
            return None 
        
    def calculate_project_revenue(self):
        if self.df is not None:
            project_revenue = self.df.groupby("project_name").agg({"price": "sum"}) 
            return project_revenue
        else:
            print("DataFrame is not loaded")
            return None
        
    def displaying_top_5_projects_revenue(self):
        project_revenue = self.calculate_project_revenue() 
        if project_revenue is not None and self.top_5_project_names:
            top_5_projects_revenue = project_revenue.loc[self.top_5_project_names] 
            top_5_projects_revenue['price'] = top_5_projects_revenue['price'].round(2)
            top_5_projects_revenue_sorted = top_5_projects_revenue.sort_values(by="price", ascending=False) 
            print("\nTop 5 projects by revenue: ")
            print(top_5_projects_revenue_sorted)
        else:
            print("Top 5 projects have not been identified or DataFrame is not loaded.")

    def visualize_top_5_projects_revenue(self):
        project_revenue = self.calculate_project_revenue() 
        if project_revenue is not None and self.top_5_project_names:
            top_5_projects_revenue = project_revenue.loc[self.top_5_project_names] 
            top_5_projects_revenue_sorted = top_5_projects_revenue.sort_values(by="price", ascending=False) 

            sns.set_style("whitegrid") 
            plt.figure(figsize=(10,6), facecolor="white") 
            revenue_plot = sns.barplot(
                x = top_5_projects_revenue_sorted.index,
                y="price",
                data=top_5_projects_revenue_sorted.reset_index()
                #palette="viridis"
            )

            revenue_plot.set_title("Top 5 projects By Revenue", fontsize=16) 
            revenue_plot.set_xlabel("Project Name", fontsize=14)
            revenue_plot.set_ylabel("Total Revenue", fontsize=14) 

            plt.xticks(rotation=45) 

            plt.show()
        else:
            print("Top 5 projects have not been identified or DataFrame is not loaded.")

           


file_path = r"C:\Python Assignment\market-units-raw-sales-anonymized.xlsx"
analyzer = DataInitializer(file_path)
analyzer.identify_top_5_projects_by_units()  
analyzer.displaying_top_5_projects_revenue()    
analyzer.visualize_top_5_projects_revenue()      
