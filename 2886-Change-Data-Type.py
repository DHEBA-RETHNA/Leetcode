import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students = students.astype({'grade':'int'})
    #students['grade']=students['grade'].astype(int)
    return students
