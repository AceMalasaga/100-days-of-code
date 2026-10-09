import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = data["Primary Fur Color"].replace({"Gray": "grey", "Cinnamon": "red", "Black": "black"})
squirrel_count = fur_color.value_counts().reset_index().rename(columns={"Primary Fur Color": "Fur Color", "count": "Count"})

df_squirrel = pandas.DataFrame(squirrel_count)
df_squirrel.to_csv("squirrel_count.csv")

#This is Angela Code and mine is at the top
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
# # print(f"Total Gray: {gray_squirrels}\n Total Red: {red_squirrels}\n Total Black: {black_squirrels}")
#
# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [gray_squirrels, red_squirrels, black_squirrels]
# }
# df_squirrel = pandas.DataFrame(data_dict)
# df_squirrel.to_csv("data_squirrel.csv")