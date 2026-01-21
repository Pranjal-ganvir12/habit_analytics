#Standardinzing the DataFrames - There will be a common term for all the words with the same meaning, ex. study_hours = {study_time , homework_time}
import pandas as pd 
from src.features.feature_mapping import TARGET_MAP, FEATURE_MAP


def standardize_df(df: pd.DataFrame, dataset_name: str, include_target: bool = True) ->pd.DataFrame:
    new_df = pd.DataFrame() 

    for canonical, actual in FEATURE_MAP[dataset_name].items():
        if actual is None:
            continue

        new_df[canonical] = df[actual]


    if include_target:
        target_col = TARGET_MAP[dataset_name]
        if target_col not in df.columns:
           raise ValueError(
                f"Target column '{target_col}' not found in raw df for dataset '{dataset_name}'. "
                f"Available columns: {list(df.columns)}"
            )
        new_df[target_col] = df[target_col]
    return new_df
