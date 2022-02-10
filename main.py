# importing necessary packages

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

df = pd.read_csv("GB generation data.csv")
print(df.head(10))

# drop columns with no values
df.drop(["Fossil Brown coal/Lignite  - Actual Aggregated [MW]","Fossil Coal-derived gas  - Actual Aggregated [MW]","Fossil Oil shale  - Actual Aggregated [MW]","Fossil Peat  - Actual Aggregated [MW]","Geothermal  - Actual Aggregated [MW]","Hydro Water Reservoir  - Actual Aggregated [MW]","Marine  - Actual Aggregated [MW]","Other renewable  - Actual Aggregated [MW]","Waste  - Actual Aggregated [MW]","Hydro Pumped Storage  - Actual Consumption [MW]"],axis=1,inplace=True)

print(df.head(10))

#drop n/a

df2 = df.dropna()

print(df2.dtypes)
MTU = df2['MTU'].str.split('-', 1).str[0]
df2["MTU"] = MTU.astype(str)

df2['MTU'] = pd.to_datetime(df2.MTU)

data_list = []
for i in np.arange(0,len(df2),48):
  data_list.append(df2.iloc[i:i+48:])



#Custom fuction for the data cleaning
def cleaning(path_to_df):
  data = []
  df = pd.read_csv(path_to_df)
  df.drop(["Fossil Brown coal/Lignite  - Actual Aggregated [MW]","Fossil Coal-derived gas  - Actual Aggregated [MW]","Fossil Oil shale  - Actual Aggregated [MW]","Fossil Peat  - Actual Aggregated [MW]","Geothermal  - Actual Aggregated [MW]","Hydro Water Reservoir  - Actual Aggregated [MW]","Marine  - Actual Aggregated [MW]","Other renewable  - Actual Aggregated [MW]","Waste  - Actual Aggregated [MW]","Hydro Pumped Storage  - Actual Consumption [MW]"],axis=1,inplace=True)
  df.dropna()
  MTU = df['MTU'].str.split('-', 1).str[0]
  df["MTU"] = MTU.astype(str)
  df['MTU'] = pd.to_datetime(df.MTU)
  for i in np.arange(0,len(df),48):
    data.append(df.iloc[i:i+48:])
  return data

data_list_GB = cleaning("GB generation data.csv")
data_list_netherlands = cleaning("Netherlands Generation Data.csv")

# merging two chunks of dataframe seperated by time range of 15mins
# [0] & [1] => January 2 & 3 => February
new_df = pd.concat([data_list_netherlands[20],data_list_netherlands[21]]) # data_list_neteherlands[0] contains january up until mid-month of january data_list_netherlands[1] contains the remaining part of january
# Solar power Generation for Great Britain in November 2021
plt.style.use("Solarize_Light2")
plt.plot(data_list_GB[10]["Solar  - Actual Aggregated [MW]"],data_list_GB[10]["MTU"], label="Great Britain",color="red") # 0-January 1-Febuary 2-March 3- April ..
plt.plot(new_df["Solar  - Actual Aggregated [MW]"],new_df["MTU"],label="Netherlands",color="black")
plt.title("Solar Power Generated for GB and Netherlands in November 2021")
plt.xlabel("Solar Power Generated (MW)")
plt.ylabel("Date-Time")
plt.legend()
plt.show()

#Solar Power in February 2021 in Great Britain
plt.plot(data_list[1]["Solar  - Actual Aggregated [MW]"],data_list[1]["MTU"])
plt.title("Time VS Solar Power Generated for February 2021 at Great Britain")
plt.xlabel("Solar Power Generated (MW)")
plt.ylabel("Date-Time")
plt.show()

#Solar Power in March 2021 in Great Britain
plt.plot(data_list[2]["Solar  - Actual Aggregated [MW]"],data_list[2]["MTU"])
plt.title("Time VS Solar Power Generated for March 2021 at Great Britain")
plt.xlabel("Solar Power Generated (MW)")
plt.ylabel("Date-Time")
plt.show()

# Distribution of Solar Power in 2021 in Great Britain
plt.hist(data_list[10]["Solar  - Actual Aggregated [MW]"])
plt.title("Solar Power Distribution at GB in November 2021")
plt.ylabel("Frequency")
plt.xlabel("Solar Power Generated (MW)")
plt.show()

