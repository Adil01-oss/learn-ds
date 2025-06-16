import pandas as pd

df = pd.read_csv("data/movies.csv")
avg_rating = df["rating"].mean()

print(f"Средний рейтинг фильмов: {avg_rating:.2f}")
