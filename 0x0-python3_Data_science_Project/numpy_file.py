import pandas as pd

myfile = pd.read_excel("/home/anthony/data_science/Data_Science_Projects/0x0-python3_Data_science_Project/Historicaldata/Historicalinvesttemp.xlsx")
myfile1 = pd.read_csv("/home/anthony/data_science/Data_Science_Projects/0x0-python3_Data_science_Project/African/African-Nations-results.csv")
myfile2 = pd.read_excel("/home/anthony/data_science/Data_Science_Projects/0x0-python3_Data_science_Project/African/data.xlsx")
myfile2.drop_duplicates()
# myfile1["tournament"] = myfile1["tournament"].str.replace("Friendly", "Anthony")
print(myfile1)
