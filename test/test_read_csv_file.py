import pandas as pd

from src.read_csv_file import read_csv_file
from unittest.mock import MagicMock


def test_read_csv_file_return_correct_dataframe(monkeypatch):
    # Create a mock DataFrame to return
    mock_df = pd.DataFrame({
        "Name": ["Alice", "Bob"],
        "Age": [30, 25],
        "City": ["New York", "Los Angeles"]
    })

    # Mock pandas.read_csv to return the mock DataFrame
    mock_read_csv = MagicMock(return_value=mock_df)

    # Use monkeypatch to replace the pandas.read_csv with the mock
    monkeypatch.setattr(pd, "read_csv", mock_read_csv)

    # Call the function under test
    result = read_csv_file("sample_file.csv")

    # Assert that the mock was called correctly
    mock_read_csv.assert_called_once_with("sample_file.csv")

    # Assert that the result is the DataFrame we mocked
    pd.testing.assert_frame_equal(result, mock_df)
