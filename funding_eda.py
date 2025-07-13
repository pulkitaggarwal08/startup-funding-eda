import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("startup_funding.csv")

column_mapping = {
    'SNo': 'Sr_No',
    'Date dd/mm/yyyy': 'Date',
    'Startup Name': 'Startup_Name',
    'Industry Vertical': 'Industry_Vertical',
    'SubVertical': 'SubVertical',
    'City  Location': 'City',
    'City Location': 'City',
    'Investors Name': 'Investors_Name',
    'InvestmentnType': 'Investment_Type',
    'Investment Type': 'Investment_Type',
    'Amount in USD': 'Amount_USD',
    'Remarks': 'Remarks'
}
df.rename(columns=column_mapping,inplace=True)

print(df.sample(10))