import pandas as pd

df = pd.read_excel("https://www.gairuo.com/file/data/dataset/team.xlsx")
print(df.sample)
print(df.shape)