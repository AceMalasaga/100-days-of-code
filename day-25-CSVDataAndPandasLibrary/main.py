import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = data["Primary Fur Color"].replace({"Gray": "grey", "Cinnamon": "red", "Black": "black"})
squirrel_count = fur_color.value_counts().reset_index().rename(columns={"Primary Fur Color": "Fur Color", "count": "Count"})
print(squirrel_count)
