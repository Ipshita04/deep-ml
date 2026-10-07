import pandas as pd

def solution(df):
    df=df[df["status"]=="completed"]
    result=(
        df.groupby("region", as_index=False)
        ["amount"].sum()
        .sort_values("amount", ascending=False)
        .head(10)
        .reset_index(drop=True)
    )
    return result
    pass