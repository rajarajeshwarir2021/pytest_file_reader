import os
import pandas as pd


def read_csv_file(filepath: str) -> pd.DataFrame:
    """
    Reads a CSV file and returns it as a pandas DataFrame.

    Parameters:
    -----------
    filepath : str
        The path to the CSV file to be read.

    Returns:
    --------
    pandas.DataFrame
        A DataFrame containing the data from the CSV file.

    Raises:
    -------
    Exception
        If the file does not exist at the given filepath, an exception is raised with the message "File does not exist".

    """
    if not os.path.exists(filepath):
        raise Exception("File does not exist")
    return pd.read_csv(filepath)

