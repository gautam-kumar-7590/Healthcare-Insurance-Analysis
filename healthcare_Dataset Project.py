import pandas as pd 
import numpy as np

#Loading Dataset
print("loading Dataset")


df = pd.read_csv(r"C:\Excel Folder\insurance.csv")


#Inspect Data
print("Inspect Data")

print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df.shape)


#Checking Missing Values & Duplicates Value 
print("checking missing values & duplicates value ")


print(df.isnull().sum())
print(df.duplicated().sum())


#Removing Duplicate Value
print("removing duplicate values ")

df = df.drop_duplicates()
print(df.duplicated().sum())


#cleaning Columns
print("cleaning columns")


df["bmi"] = df["bmi"].round(0)
df["bmi"]=df["bmi"].astype(int)
df["charges"]=df["charges"].round().astype(int)
print(df.head())


print(df["region"].unique())
print(df["region"].value_counts())



#Correlation
print("Correlation")
print(df.corr(numeric_only=True))



#Top 10 Highest Charges
print("10 highest charges")
print(df.sort_values("charges",ascending=False).head(10))



#Maximum Insurance Charge
print("Maximum insurance charge")
print(df["charges"].max())



#Count of Male and Female 
print("Count of Male and Female")
print(df["sex"].value_counts())



#Average BMI
print("Average BMI")
print(df["bmi"].mean())



#Average Charges
print("Average charges")
print(df["charges"].mean())



#Average Charges on Smoker's
print("Average charges on smoker's")
print(df[df["smoker"]=="yes"]["charges"].mean())



#Average Count of Children
print("Average count of Childern")
print(df["children"].mean())



#Average Age 
print("Average age")
print(df["age"].mean())



#Average Changes on Male and Female 
print("Average charges on Male and Female")
print(df.groupby("sex")["charges"].mean())



#Region with Largest Number of Smokers
print("Region with Largest Number of Smokers")
print(df[df["smoker"]=="yes"]["region"].value_counts())


#Count of People with No child
print("Average Count of People with No Child")
print((df["children"] == 0).sum())


#Average Count of People with High BMI with NO Children
print("Average Count of People With High BMI with NO Children ")
print(df[df["children"]==0]["bmi"].mean())


#Average Charges by Region
print("Average Charges by Region")
print(df.groupby("region")["charges"].mean())


#Which Region have High Patients 
print("Which Region have High Patients")
print(df["region"].value_counts())



#Average Age of Smokers 
print("Average Age of Smokers ")
print(df[df["smoker"]=="yes"]["age"].mean())


df.to_csv("insurance_cleaned.csv", index=False)