import pandas as pd 
import glob

files = glob.glob('data/*.csv')
df_list = []
for file in files:
    df = pd.read_csv(file)
    df_list.append(df)
data = pd.concat(df_list, ignore_index=True)

data = data[data["product"] == "pink morsel"]
data["Sales"] = data["quantity"] * data["price"]

final = data[["Sales", "date", "region"]]
final = final.rename(columns={"date": "Date", "region": "Region"})

final.to_csv("final_sales.csv", index=False)
print("Done! File created.")

