import pandas as pd

# Load butterfly species dataset
df = pd.read_csv("butterfly_species.csv")

# Show the most beautiful or unique ones (assuming we have a 'beauty_score' or similar)
marvels = df.sort_values(by="beauty_score", ascending=False).head(10)

print("Top 10 Marvelous Butterfly Species:")
print(marvels[['species_name', 'region', 'color_pattern', 'beauty_score']])
