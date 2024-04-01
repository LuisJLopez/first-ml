import pandas as pd

def main():
    data = pd.read_csv("../data/insurance.csv")

    # first row
    data.head()

    # dataset information
    data.info()

    # see missing data
    data.isnull()

    # sum missing data
    data.isnull().sum()

    # column types
    data.dtypes

    # covert objects to category types
    data['sex'] = data['sex'].astype('category')
    data['region'] = data['region'].astype('category')
    data['smoker'] = data['smoker'].astype('category')

    # transpose statistics
    data.describe().T

    # get the mean for smokers
    # smoke_data = data.groupby("smoker").mean().round(2)

if __name__ == "__main__":
    main()