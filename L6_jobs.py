import numpy as np
import pandas as pd

df = pd.read_csv("jobs/eda_data.csv")
print(df.head())
print(df["Job Title"].head())#prints first 5 job titles
print(df["Job Title"].tail())
print(df.columns) #tells us all the coloumns


print(df["python_yn"].tail())#prints the last 5 "python_yn"s
#print the sumarized report of the data frame
print(df.info())
print(df.size)#it counts the number of values in the data frame

print(df.shape)#givers number of rows and coloumns in data frame 

print(df[["avg_salary","Company Name"]])
print(df[["avg_salary","min_salary","max_salary"]])
print("the minimum salary width is :",df["min_salary"].min())
print("the maximum salary width is :",df["max_salary"].max())