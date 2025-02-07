import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees[:3]
    #employees.iloc[:3]
    #employees.head(3)
