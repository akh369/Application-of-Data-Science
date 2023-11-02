import pandas as pd

df = pd.read_csv("C:/Users/akh36/Documents/Macquarie/Semester 3/Application DS/data/Reddit_Data.csv")

df = df[df['category'] != 0]

df = df[df['category'] != 1]

df.to_csv('Reddit_Cleaned.csv', index=False)