import pandas as pd

def solution(df):
    df=df.loc[:,df.isnull().mean()<=0.5]
    df=df.loc[df.isnull().mean(axis=1)<=0.5]
    for col in df.columns:
        if(df[col].dtype=="object"):
            df[col]=df[col].fillna(df[col].mode()[0])
        else:
            df[col]=df[col].fillna(df[col].mean())
    df=df.reset_index(drop=True)
    return df            
    pass