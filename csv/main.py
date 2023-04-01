import pandas

data = pandas.read_csv("./squirrel_data.csv")
fur_colour = ['grey','red','black']


# count = (data["Primary Fur Color"].value_counts())
# print(count)
# no_of_grey = count.Gray
# no_of_red = count.Cinnamon
# no_of_black = count.Black
no_of_grey = len(data[data["Primary Fur Color"] == "Gray"])
no_of_red = len(data[data["Primary Fur Color"] == "Cinnamon"])
no_of_black = len(data[data["Primary Fur Color"] == "Black"])
# print(count)


squirrel_data = {
    "Fur Color": ['grey','red','black'],
    "Count":[no_of_grey,no_of_red,no_of_black]
}

s_data = pandas.DataFrame(squirrel_data)
s_data.to_csv("./formated squirrel data.csv")

