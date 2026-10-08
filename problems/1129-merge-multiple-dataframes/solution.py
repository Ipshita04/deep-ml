import pandas as pd

def solution(df1, df2, df3):
    df1=df1.merge(df2,on='emp_id',how='inner')
    df1=df1.merge(df3,on='emp_id',how='left')
    df1.reset_index(drop=True)
    return df1
    pass