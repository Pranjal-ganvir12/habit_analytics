from __future__ import annotations
from dataclasses import dataclass
import pandas as pd 

@dataclass
class DatasetLoader: 
    path:str 

    def load(self)->pd.DataFrame:
        df = pd.read_csv(self.path)
        return df