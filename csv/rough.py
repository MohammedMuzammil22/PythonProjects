# with open("./weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#     print(data)

# import csv
# 
# with open("./weather_data.csv") as data_file:
#     # data = data_file.readlines()
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if(row[1] != "temp"):
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("./weather_data.csv")
# print(type(data))#dataFrame -> 2d array
# print(type(data["temp"]))#series -> 1d array
data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# avg = sum(temp_list)/len(temp_list)
# print(avg)

# avg = data["temp"].mean()
# print(avg)

max_temp = data["temp"].max()
# print(max_temp)

# get data in column
# print(data.condition)
# print(data['condition'])

# to retrive rows
# print(data[data.day == 'Monday'])
# print(data[data.temp == 12])
# print(data[data.condition == "Sunny"])

# print(data[data.temp == max_temp])
# print("===================")
# monday = data[data.day == "Monday"]
# print(monday)
# print(monday.day)
# print(monday.condition)
# print(monday.temp)

# creating dataframes from scratch
data_dict = {
    'name':["muzammil","abu","arshad"],
    'age':[20,19,21]
}

dataframe_data = pandas.DataFrame(data_dict)
print(dataframe_data)

# to create csv 
dataframe_data.to_csv("./new_data.csv")
