import numpy as pd
import pandas as pd

# load CSV file data into DataFrame
pokemon = pd.read_csv("pokemon_data.csv")

print(pokemon) # displays first 5 rows and last 5 rows
print(pokemon.columns) # see column labels

# access one column (Series) of data 
print(pokemon["Type 1"])

# shorthand way of referencing column
print(pokemon.HP)

# create new column for Attack/Special Attack
pokemon["Attack Ratio"] = pokemon["Attack"] / pokemon["Sp. Atk"]
print(pokemon["Attack Ratio"])

# you can replace indices (0...end) with strings from a column
poke = pokemon.set_index("Name")

# access a specific cell
print(poke.loc["Pikachu", "Type 1"])

# access a range of rows
print(poke.loc[["Bulbasaur", "Squirtle", "Charmander"]])

# for if you want to print every row with a certain col
for index, row in poke.iterrows():
    print(index, "-", row["Type 1"])