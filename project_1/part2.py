import pandas as pd
class read_data:
    def __init__(self,path):
        self.path= path
    def read_data(self):
        # Read CSV files
        self.df1 = pd.read_csv(self.path[0])
        self.df2 = pd.read_csv(self.path[1])
        print(self.path[0],':\n',self.df1.head(5).to_string(index=False, header=False),'\n---------------------------------------------------------')
        
        print(self.path[1],':\n',self.df2.head(5).to_string(index=False, header=False),'\n---------------------------------------------------------')
    
    def combine(self):
        # Add a new column to indicate the source
        self.df1['Comic'] = 'DC'
        self.df2['Comic'] = 'MARVEL'

        # Assign the new column names to the DataFrame
        self.df2.columns = self.df1.columns

        # Concatenate DataFrames
        combined_df = pd.concat([self.df1, self.df2], ignore_index=True)
        return combined_df