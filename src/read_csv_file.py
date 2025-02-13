import os
import pandas as pd


def read_csv_file(filepath: str):
    if not os.path.exists(filepath):
        raise Exception("File does not exist")
    return pd.read_csv(filepath)

