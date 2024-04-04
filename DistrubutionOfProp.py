import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

class VizualiseData:
    def __init__(self, file_path):
        self.file_path = file_path 
        self.df = self.load_file() 
    
    def load_file(self):
        try:
            df = pd.read_excel(self.file_path)
            print("File loaded successfully")
            return df
        except Exception as e:
            print(f"An error occured while displaying file: {e}")
            return None
        
    def plot_layout_distribution(self):
        if self.df is not None:
            sns.set_style("whitegrid")

            plt.figure(figsize=(10,6), facecolor="white")
            layout_distribution = sns.countplot (
                x = "layout", 
                data = self.df,
                order = self.df["layout"].value_counts().index
            )

            layout_distribution.set_title("Distibution of Properties by Number of Rooms", fontsize=16)
            layout_distribution.set_xlabel("Number of Rooms (Layout)", fontsize=14)
            layout_distribution.set_ylabel("Number of Properties", fontsize=14)

            plt.xticks(rotation=45) 

            plt.show()
        else:
            print("DataFrame is not loaded")

file_path = r"C:\Python Assignment\market-units-raw-sales-anonymized.xlsx"
visualizer = VizualiseData(file_path)
visualizer.plot_layout_distribution()
