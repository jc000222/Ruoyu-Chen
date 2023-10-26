import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import warnings
class EDA:
    def __init__(self,df):
        self.df = df
        print("dataframe accepted")
        # Filter out UserWarnings
        pd.options.mode.chained_assignment = None
        warnings.filterwarnings("ignore", category=UserWarning)

    def overview(self):
        '''
        parameter
        return

        '''

        (lin_n,col_n) = self.df.shape
        columns = self.df.columns.tolist()
        print("In this dataset there are {0} lines, {1} columns.".format(lin_n,col_n))
        
        df_overview = pd.DataFrame()
        df_overview['Insights'] = ['Count','Unique_num','top','freq']
        for i in range(col_n):
            df_overview[columns[i]] = [
            self.df[columns[i]].count(),self.df[columns[i]].nunique(),self.df[columns[i]].value_counts().index[0],self.df[columns[i]].value_counts().iloc[0]
            ]
        return df_overview.head()
    def null_check(self):
        plt.rcParams['figure.figsize'] = (15,6)
        sns.heatmap(self.df.isnull(),yticklabels = False, cbar = False)
        plt.title("Missing null values")
        plt.xticks(rotation=30)
        return self.df.isnull().sum().sort_values(ascending = False)

    def delete_columns(self,columns_to_exclude):
        # Replace with the columns you want to exclude

        # Create a new DataFrame with only the columns you want to keep
        self.df = self.df[[col for col in self.df.columns if col not in columns_to_exclude]]
        return self.df.columns.tolist()
    
    def ID_fix(self):
        original = self.df['ID'].value_counts(dropna=False)
        self.df['ID'].fillna('Unknown', inplace=True)
        self.df['ID'] = self.df['ID'].replace('Identity Unknown', 'Unknown')
        return original
    
    def ALIGN_fix(self):
        original = self.df['ALIGN'].value_counts(dropna=False)
        self.df['ALIGN'].fillna('Unknown', inplace=True)
        return original
    
    def SEX_fix(self):
        original = self.df['SEX'].value_counts(dropna=False)
        self.df['SEX'].fillna('Unknown', inplace=True)
        return original

    def GSM_fix(self):
        original = self.df['GSM'].value_counts(dropna=False)
        self.df['GSM'].fillna('No GSM', inplace=True)
        return original
    
    def ALIVE_fix(self):
        original = self.df['ALIVE'].value_counts(dropna=False)
        self.df = self.df.dropna(subset=['ALIVE'])
        return original

    def APPEARANCES_fix(self):
        original = self.df['APPEARANCES'].value_counts(dropna=False)
        # Fill null values in column A with values from column B where B is not null
        self.df['APPEARANCES'].fillna(self.df['YEAR'], inplace=True)
        

        # Drop rows where both A and B are null
        self.df.dropna(subset=['APPEARANCES', 'YEAR'], how='all', inplace=True)
        self.df = self.df.dropna(subset=['YEAR'])
        self.df['APPEARANCES'] = self.df['APPEARANCES'].astype(int)
        self.df['YEAR'] = self.df['YEAR'].astype(int)
        return original
    
    def ID(self):
        # Create the value counts
        value_counts = self.df['ID'].value_counts()

        # Create a figure with two subplots
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

        # Original Matplotlib plot
        ax1.bar(value_counts.index, value_counts.values, alpha=0.8)
        ax1.set_title("Freq Distribution of ID of heroes (Matplotlib)")
        

        # Adding labels to the bars
        for i, v in enumerate(value_counts):
            ax1.text(i, v, str(v), ha='center', va='bottom', fontsize=8)

        # Rotate x-axis labels
        ax1.set_xticklabels(value_counts.index, rotation=30)

        # Seaborn plot
        sns.barplot(x=value_counts.index, y=value_counts.values, ax=ax2, alpha=0.8)
        ax2.set_title("Freq Distribution of ID of heroes (Seaborn)")
        

        for i, v in enumerate(value_counts):
            ax2.text(i, v, str(v), ha='center', va='bottom', fontsize=8)
        # Rotate x-axis labels
        ax2.set_xticklabels(value_counts.index, rotation=30)
        plt.xlabel('')
        # Display the plot
        plt.tight_layout()
        plt.show()
    
    def ALIGN(self):
        value_counts = self.df['ALIGN'].value_counts()

        # Create a figure with two subplots
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

        # Original Matplotlib horizontal bar plot
        value_counts.plot(kind='barh', ax=ax1)
        ax1.set_title("Freq Distribution of ALIGN of heroes (Matplotlib)")
        ax1.set_xlabel('')

        # Adding labels to the bars
        for i, v in enumerate(value_counts):
            ax1.text(v, i, str(v), ha='left', va='center', fontsize=8)

        # Seaborn horizontal bar plot
        sns.barplot(x=value_counts.values, y=value_counts.index, ax=ax2)
        ax2.set_title("Freq Distribution of ALIGN of heroes (Seaborn)")
        ax2.set_xlabel('Frequency')

        for i, v in enumerate(value_counts):
            ax2.text(v, i, str(v), ha='left', va='center', fontsize=8)
        # Display the plot
        plt.tight_layout()
        plt.show()
    
    def SEX(self):
        # Create the value counts
        value_counts = self.df['SEX'].value_counts()

        # Create a figure with two subplots
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

        # Original Matplotlib plot
        ax1.bar(value_counts.index, value_counts.values, alpha=0.8)
        ax1.set_title("Freq Distribution of SEX of heroes (Matplotlib)")
        

        # Adding labels to the bars
        for i, v in enumerate(value_counts):
            ax1.text(i, v, str(v), ha='center', va='bottom', fontsize=8)

        # Rotate x-axis labels
        ax1.set_xticklabels(value_counts.index, rotation=30)

        # Seaborn plot
        sns.barplot(x=value_counts.index, y=value_counts.values, ax=ax2, alpha=0.8)
        ax2.set_title("Freq Distribution of SEX of heroes (Seaborn)")
        

        for i, v in enumerate(value_counts):
            ax2.text(i, v, str(v), ha='center', va='bottom', fontsize=8)
        # Rotate x-axis labels
        ax2.set_xticklabels(value_counts.index, rotation=0)
        plt.xlabel('')
        # Display the plot
        plt.tight_layout()
        plt.show()


    def GSM(self):
        # Create the value counts
        value_counts = self.df['GSM'].value_counts()

        # Create a figure with two subplots
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

        # Original Matplotlib plot
        ax1.bar(value_counts.index, value_counts.values, alpha=0.8)
        ax1.set_title("Freq Distribution of GSM of heroes (Matplotlib)")
        

        # Adding labels to the bars
        for i, v in enumerate(value_counts):
            ax1.text(i, v, str(v), ha='center', va='bottom', fontsize=8)

        # Rotate x-axis labels
        ax1.set_xticklabels(value_counts.index, rotation=30)

        # Seaborn plot
        sns.barplot(x=value_counts.index, y=value_counts.values, ax=ax2, alpha=0.8)
        ax2.set_title("Freq Distribution of GSM of heroes (Seaborn)")
        

        for i, v in enumerate(value_counts):
            ax2.text(i, v, str(v), ha='center', va='bottom', fontsize=8)
        # Rotate x-axis labels
        ax2.set_xticklabels(value_counts.index, rotation=0)
        plt.xlabel('')
        # Display the plot
        plt.tight_layout()
        plt.show()
    
    def APPEARANCES(self):
        # Create subplots
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

        # Original Matplotlib Histogram
        ax1.hist(self.df['APPEARANCES'], bins=20)
        ax1.set_xlabel("Value")
        ax1.set_ylabel("Frequency")
        ax1.set_title("Histogram of APPEARANCES (Matplotlib)")
        ax1.set_ylim([0, max(ax1.get_yticks()) + 1])

        # Get the counts for each bin
        counts, bins, _ = ax1.hist(self.df['APPEARANCES'], bins=20)

        # Annotate the bars with their counts
        for count, bin_edge in zip(counts, bins):
            ax1.text(bin_edge, count, count, ha='center', va='bottom')

        # Seaborn Histogram
        sns.histplot(data=self.df, x='APPEARANCES', bins=20, ax=ax2)
        ax2.set_xlabel("Value")
        ax2.set_ylabel("Frequency")
        ax2.set_title("Histogram of APPEARANCES (Seaborn)")
        for count, bin_edge in zip(counts, bins):
            ax2.text(bin_edge, count, count, ha='center', va='bottom')

        # Adjust subplot layout
        plt.tight_layout()

        # Show the subplots
        plt.show()

    def YEAR(self):
        year_counts = self.df['YEAR'].value_counts().sort_index()

        # Create subplots
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

        # Original Matplotlib Line Plot
        ax1.plot(year_counts.index, year_counts.values, marker='o', linestyle='-')
        ax1.set_xlabel("Year")
        ax1.set_ylabel("Frequency")
        ax1.set_title("Line Plot of Year Frequencies (Matplotlib)")
        ax1.grid(True)

        # Seaborn Line Plot
        sns.lineplot(data=year_counts, ax=ax2)
        ax2.set_xlabel("Year")
        ax2.set_ylabel("Frequency")
        ax2.set_title("Line Plot of Year Frequencies (Seaborn)")

        # Adjust subplot layout
        plt.tight_layout()

        # Show the subplots
        plt.show()
    def dataframe(self):
        return self.df



