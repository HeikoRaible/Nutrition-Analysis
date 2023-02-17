import os
import pandas as pd
import matplotlib.pyplot as plt


# paths
data_path = os.path.join("..", "data")
diet_path = os.path.join(data_path, "diet")
weight_path = os.path.join(data_path, "weight")
workout_path = os.path.join(data_path, "workout")

# data
diet = pd.read_csv(os.path.join(diet_path, "history_9d9a9e10-0d94-4dc2-b5c0-84fdcfff3fdb.csv"), delimiter=";")

diet = diet.rename(columns={"Unnamed: 0": "date", "Calories (kcal)": "calories", "Fat (g)": "fats", "Carbohydrate (g)": "carbs", "Protein (g)": "proteins"})
diet = diet[["date", "calories", "fats", "carbs", "proteins"]]
print(diet.head())

# plot
plt.bar(diet.date, diet.calories)
plt.show()
