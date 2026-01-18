#Standardinzing the DataFrames - There will be a common term for all the words with the same meaning, ex. study_hours = {study_time , homework_time}
import pandas as pd 
from src.features.feature_mapping import FEATURE_MAP


def standardize_df(df: pd.DataFrame, dataset_name: str) ->pd.DataFrame:
    new_df = pd.DataFrame() 

    for canonical, actual in FEATURE_MAP[dataset_name].items():
        if actual is None:
            continue

        new_df[canonical] = df[actual]
    return new_df
