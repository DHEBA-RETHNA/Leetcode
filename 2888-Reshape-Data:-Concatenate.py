import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1,df2], ignore_index = True, axis = 0)
    #return df1._append(df2).reset_index(drop=True)
