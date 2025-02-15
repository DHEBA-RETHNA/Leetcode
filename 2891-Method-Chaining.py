import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[animals['weight'] > 100].sort_values('weight', ascending=False)[['name']]
    #Double brackets [['name']] makes the result to be a DataFrame with a single 'name' column.