
import matplotlib.pyplot as plt
import seaborn as sns

class infer:
    def __init__(self,df):
        self.df = df
    def task1(self):
        grouped_df = self.df.groupby(['ID', 'SEX'])
        counts = grouped_df.size().unstack()

        # Create a figure
        plt.figure(figsize=(10, 6))

        # Male bar chart
        plt.bar(counts.index, counts['Male Characters'], label='Male', alpha=0.5)
        plt.title('DC Character Alignment by Gender (Male)')
        plt.legend()

        # Female bar chart (shifted to the right)
        # Adjust the shift value as needed
        plt.bar(counts.index, counts['Female Characters'], label='Female', alpha=0.5)
        plt.title('DC Character Alignment by Gender (Female)')
        plt.legend()

        # Set the x-axis labels
        plt.xticks(rotation=45)

        # Display the plot
        plt.show()
    def task2(self):
        # Create a violin plot to compare the distribution of hero IDs by gender
        plt.figure(figsize=(8, 6))
        plt.title("Impact of Gender on Hero ID")
        plt.xlabel("Gender")
        plt.ylabel("APPEARANCES")
        plt.xticks(rotation=0)

        # Use Seaborn to create a violin plot
        sns.violinplot(data=self.df, x='APPEARANCES', y='SEX')

        # Display the plot
        plt.show()
    def task3(self):
        # Create a violin plot to compare the distribution of hero IDs by gender
        plt.figure(figsize=(8, 6))
        plt.title("Impact of Gender on Hero ID")
        plt.xlabel("GSM")
        plt.ylabel("YEAR")
        plt.xticks(rotation=0)

        # Use Seaborn to create a violin plot
        sns.boxplot(data=self.df, x='YEAR', y='GSM')

        # Display the plot
        plt.show()