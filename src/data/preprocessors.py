import pandas as pd

def split_features_target(
        df: pd.DataFrame,
        target_column: str)->tuple[pd.DataFrame, pd.Series]:
    if target_column not in df.columns:
        raise ValueError(
            f"Target column '{target_column}' not found. Available columns: {list(df.columns)}"
        )
    X = df.drop(columns=[target_column])
    y = df[target_column]

    return X,y
    
