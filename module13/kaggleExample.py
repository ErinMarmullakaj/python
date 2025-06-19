import pandas as pd
df=pd.read_csv("avgIQpercountry.csv")
print(df.info()) #we see the column of dataset
print(df.head()) #we see the first 5 rows

country_data=df["country"]
print(country_data)

subset=df[["Country", "Avereage IQ"]]
filtered_DF=subset[subset["Avereage IQ"]>100]
print(filtered_DF)

#null_mask fining the null rows
null_mask=df.insull()
null_count=null_mask.sum()
print(null_count)

#removing dupes
df.drop_duplicates(keep="first",inplace=True)

