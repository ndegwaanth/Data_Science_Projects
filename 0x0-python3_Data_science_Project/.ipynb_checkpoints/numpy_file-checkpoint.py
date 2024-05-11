import pandas as pd

myfile = pd.read_excel("/home/anthony/data_science/Data_Science_Projects/0x0-python3_Data_science_Project/Historicaldata/Historicalinvesttemp.xlsx")
myfile1 = pd.read_csv("/home/anthony/data_science/Data_Science_Projects/0x0-python3_Data_science_Project/African/African-Nations-results.csv")
myfile2 = pd.read_excel("/home/anthony/data_science/Data_Science_Projects/0x0-python3_Data_science_Project/African/data.xlsx")
myfile2.drop_duplicates()
# del(myfile2[""])
for i in range(len(myfile1.columns)):
    if i == "NaN":
        del i
    print(myfile2)
# myfile2["Stocks"] = myfile2["Stocks"].apply(lambda x: int(x))
print(myfile2)